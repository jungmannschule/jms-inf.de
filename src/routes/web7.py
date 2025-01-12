import base64
import json
import os
from functools import lru_cache

import requests
from flask import Blueprint, render_template, request

from src.models import Repository, Branch, Issue

bp = Blueprint('web7', __name__)
gitea_url = 'https://jms-inf.de/git/api/v1/'
headers = {'Authorization': 'token ' + os.getenv('GITEA_API')}

@lru_cache()
def get_repo_contents(repo):
    print(repo.name)
    commits = repo.get_commits()
    return commits[0]

def check_pages(repo):
    errors = []
    sources = {}
    for file in ['index', 'about', 'pricing']:
        r = requests.get(f"{gitea_url}repos/7inf/{repo}/contents/{file}.html", headers=headers)
        if r.status_code != 200:
            errors.append(f'Konnte {file}.html nicht finden.')
        else:
            gitea_response = json.loads(r.text)
            bytes = base64.b64decode(gitea_response['content'])
            html = bytes.decode('windows-1251') # .decode() uses utf-8 and failed here for 7c!
            sources[file] = html
    if errors:
        return 'danger', errors, None
    return 'success', None, sources

def check_idea(sources):
    print(sources)


def check_valid_html(sources):
    html_headers = {'Content-Type': 'text/html; charset=utf-8'}
    url = 'https://validator.w3.org/nu/?out=json'
    r = requests.post(url, sources['index'], headers=html_headers)
    errors = json.loads(r.text)
    error_count = len(errors['messages'])
    if error_count > 1:
        return 'danger', [f'Es wurden {error_count} Fehler gefunden. Prüft euren Code mit einem <a href="https://validator.w3.org/nu/#textarea">Validator</a>.']
    return 'success', None

def check_linked(sources):
    errors = []
    for filename in sources.keys():
        targets = ['index', 'about', 'pricing']
        targets.remove(filename)
        for t in targets:
            s = f'href="{t}.html"'
            if s not in sources[filename]:
                errors.append(f'Kein Link zu {t}.html in {filename}.html.')
    if errors:
        return 'danger', errors
    return 'success', None

def check_tabular(sources):
    for html in sources.values():
        for s in ['<ul>', '<ol>', '<table>']:
            if s in html:
                return 'success'
    return 'danger'

def check_css(sources):
    pass

def check_img(sources):
    count = 0
    for html in sources.values():
        count += html.count('<img src="')
        if count > 1:
            return 'success'
    return 'danger'


@bp.route('/criteria', methods=['POST'])
def htmx_criteria():
    linked = tabular = css = img = 'disabled'
    html = html_errors = linked_errors = tabular_errors = css_errors = img_errors = None
    repo = request.form.get('repo')
    pages, pages_errors, sources = check_pages(repo)
    if not pages_errors:
        idea = check_idea(sources)
        try:
            html, html_errors = check_valid_html(sources)
        except Exception as e:
            html = 'danger'
            html_errors = [e]
        linked, linked_errors = check_linked(sources)
        tabular = check_tabular(sources)
        css = check_css(sources)
        img = check_img(sources)

    criteria = [
        {'descr': 'Eine insgesamt stimmig umgesetzte Idee', 'status': None, 'errors': None},
        {'descr': 'Mindestens 3 HTML-Seiten, die korrekt benannt sind', 'status': pages, 'errors': pages_errors},
        {'descr': 'Fehlerfreies HTML', 'status': html, 'errors': html_errors},
        {'descr': 'Alle Seiten sind miteinander verlinkt', 'status': linked, 'errors': linked_errors},
        {'descr': 'Mindestens eine Liste (ul/ol-Element) oder Tabelle vorhanden', 'status': tabular, 'errors': tabular_errors},
        {'descr': '15 verschiedene CSS-Anweisungen', 'status': css, 'errors': css_errors},
        # '5 verschiedene CSS-Selektoren',
        {'descr': 'Mindestens zwei Bilder, per img-Element eingebunden', 'status': img, 'errors': img_errors},
        {'descr': 'Den Workflow mit Git/Browser/Texteditor verstanden', 'status': None, 'errors': None},
    ]
    return render_template('web7/criteria.partial', criteria=criteria)

@bp.route('/web7', methods=['GET'])
def webseiten():
    team_repos = {
        '7a': ['Chairy', 'FootShop', 'German-Fly-Xpress', 'HappyJacket', 'Hockey-Psycho-Print', 'JMJT-games', 'Lach-Merch-Industries', 'RandomBazaar'],
        '7b': ['Backi-Socki', 'Baumschokolade', 'Big-Arrow-Balls', 'FruityBeach', 'Gigachat-333', 'Juwelier-FEP', 'Magic-Pets', 'Panzer-Kleinanzeigen', 'Plushclothes', 'Povtorialka', 'Vivi'],
        '7c': ['12-Months-Idea', 'Alberts-Markt', 'Coldwar-Lifestyle', 'Explain-Redstone', 'Flight-Height-2100', 'Help-the-World', 'Housemonkey', 'Krasse-Knaller', 'Lion-Esports', 'Mathe-Nachhilfe', 'Roblox-Accounts', 'Visa-Kitchen'],
        '7d': ['AI-BookWriter', 'Astroloom', 'Bijou-DAmour', 'Brillion', 'Carrier24', 'FlexiGaming-PC', 'Hannes-Fanshop', 'Kuschel-Minis', 'Operation-Deep-Down', 'PferdeShop', 'UiA'],
    } # ids: 8, 10, 11, 9

    return render_template('web7/overview.html', team_repos=team_repos)
