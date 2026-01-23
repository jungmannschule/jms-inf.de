from flask import Blueprint, render_template, request

bp = Blueprint('cybersec8', __name__)

@bp.route('/cybersec8', methods=['GET'])
def index():
    return render_template('cybersec8/index.html')