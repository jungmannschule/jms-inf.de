from flask import Blueprint, render_template

from src.models import Repository
from src.students.students_9inf import students as inf_9_list

bp = Blueprint('python', __name__)


async def get_repo(user, repo):
    return await Repository.get(owner_name=user, lower_name=repo)


async def get_forks(fork_id):
    return await Repository.filter(fork_id=fork_id)


@bp.route('/python', methods=['GET'])
async def python_course():
    repos = ['python_01', 'python_02']
    students = [{'login': s['login']} for s in inf_9_list]
    for repo in repos:
        root = await get_repo(user='9inf', repo=repo)
        forks = await get_forks(fork_id=root.id)
        fork_owners = [f.owner_name for f in forks]

        for student in students:
            if student['login'] in fork_owners:
                student_repo = await get_repo(user=student['login'], repo=repo)
                print(student['login'])
                print(f'{student_repo.updated_unix=}')
                print(f'{root.updated_unix=}')
                print()
                if student_repo.num_stars > 0:
                    circle = 'success'
                else:
                    circle = 'warning'
                url = f'https://jms-inf.de/git/{student["login"]}/{repo}'
            else:
                circle = 'error'
                url = f'https://jms-inf.de/git/repo/fork/{root.id}'

            student.update({repo: {'circle': circle, 'url': url}})

    return render_template('python/01.html', repos=repos, students=students)
