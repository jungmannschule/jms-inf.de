from flask import Blueprint, render_template

from src.models import Repository, Branch, Issue, Star
from src.students.students_9inf import students as inf_9_list

bp = Blueprint('python', __name__)


def get_repo(user, repo):
    return Repository.get(owner_name=user, lower_name=repo)


def get_forks(fork_id):
    return Repository.select(lambda r: r.fork_id == fork_id)


def get_latest_commit(repo_id):
    main = Branch.get(repo_id=repo_id, name='main')
    return main.commit_id


def get_issues(repo_id):
    return Issue.select(lambda i: i.repo_id == repo_id)


@bp.route('/python', methods=['GET'])
def python_course():
    repos = ['python_01', 'python_02', 'python_03', 'python_04', 'python_05_1', 'python_05_2', 'python_05_3']
    students = [{'login': s['login']} for s in inf_9_list]
    for repo in repos:
        root = get_repo(user='9inf', repo=repo)
        root_latest_commit = get_latest_commit(root.id)
        forks = get_forks(fork_id=root.id)
        fork_owners = [f.owner_name for f in forks]

        for student in students:
            if student['login'] in fork_owners:
                student_repo = get_repo(user=student['login'], repo=repo)
                issues = get_issues(student_repo.id)
                if Star.get(uid=1, repo_id=student_repo.id):
                    circle = 'success'
                elif len(issues) > 0:
                    circle = 'warning'
                    if all(i.is_closed for i in issues):
                        circle = 'ready'
                elif root_latest_commit != get_latest_commit(student_repo.id):
                    circle = 'ready'
                else:
                    circle = 'warning'
                url = f'https://jms-inf.de/git/{student["login"]}/{repo}'
            else:
                circle = 'error'
                url = f'https://jms-inf.de/git/repo/fork/{root.id}'

            student.update({repo: {'circle': circle, 'url': url}})

    return render_template('python/01.html', repos=repos, students=students)

