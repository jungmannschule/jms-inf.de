from flask import Blueprint, render_template

bp = Blueprint('scratch7', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('scratch7/index.html')
