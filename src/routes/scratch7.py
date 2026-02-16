from flask import Blueprint, render_template

bp = Blueprint('scratch7', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('scratch7/index.html')

@bp.route('/2025', methods=['GET'])
def index_2025():
    return render_template('scratch7/index-2025.html')
