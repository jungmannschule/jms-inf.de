from flask import Blueprint, render_template

bp = Blueprint('office6', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('office6/index.html')
