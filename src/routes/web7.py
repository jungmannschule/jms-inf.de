import os

from flask import Blueprint, render_template
from gitea import *

from src.models import Repository, Branch, Issue, Star
from src.students.students_2024_7c import students, repo_names

bp = Blueprint('web7', __name__)
gitea = Gitea('https://jms-inf.de/git', os.getenv('GITEA_API'))

@bp.route('/web7', methods=['GET'])
def webseiten():
    org = Organization.request(gitea, '7inf')
    team = org.get_team('7c')
    repos = team.get_repos()
    return render_template('web7/overview.html', repos=[repo.name for repo in repos])


def get_repo(user, repo):
    return Repository.get(owner_name=user, lower_name=repo)


def get_forks(fork_id):
    return Repository.select(lambda r: r.fork_id == fork_id)


def get_latest_commit(repo_id):
    main = Branch.get(repo_id=repo_id, name='main')
    return main.commit_id


def get_issues(repo_id):
    return Issue.select(lambda i: i.repo_id == repo_id)
