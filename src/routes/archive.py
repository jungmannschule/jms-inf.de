from flask import Blueprint, render_template

bp = Blueprint('archive', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('archive.html')
