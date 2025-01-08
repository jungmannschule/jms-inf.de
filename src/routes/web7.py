import os
from functools import lru_cache

from flask import Blueprint, render_template
from gitea import *

from src.models import Repository, Branch, Issue

bp = Blueprint('web7', __name__)
gitea = Gitea('https://jms-inf.de/git', os.getenv('GITEA_API'))

@lru_cache()
def get_repo_contents(repo):
    print(repo.name)
    commits = repo.get_commits()
    return commits[0]


@bp.route('/web7', methods=['GET'])
def webseiten():
    org = Organization.request(gitea, '7inf')
    team = org.get_team('7c')
    team_repos = team.get_repos()
    repos = {}
    # for repo in team_repos:
        # c = get_repo_contents(repo)
        # repos[repo.name] =
    criteria = [
        'Eine insgesamt stimmig umgesetzte Idee',
        'Mindestens 3 HTML-Seiten, die korrekt benannt sind',
        'Fehlerfreies HTML',
        'Alle Seiten sind miteinander verlinkt',
        'Mindestens eine Liste (ul/ol-Element) vorhanden',
        '15 verschiedene CSS-Anweisungen',
        # '5 verschiedene CSS-Selektoren',
        'Mindestens zwei Bilder, per img-Element eingebunden',
        'Den Workflow mit Git/Browser/Texteditor verstanden'
    ]
    return render_template('web7/overview.html', repos=[repo.name for repo in team_repos], criteria=criteria)


def get_repo(user, repo):
    return Repository.get(owner_name=user, lower_name=repo)


def get_forks(fork_id):
    return Repository.select(lambda r: r.fork_id == fork_id)


def get_latest_commit(repo_id):
    main = Branch.get(repo_id=repo_id, name='main')
    return main.commit_id


def get_issues(repo_id):
    return Issue.select(lambda i: i.repo_id == repo_id)
