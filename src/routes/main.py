from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/steckbriefe')
def steckbriefe_index():
    return render_template('steckbriefe/index.html')


@bp.route('/steckbriefe/<string:student>')
def steckbrief(student):
    return render_template(f'steckbriefe/{student}')