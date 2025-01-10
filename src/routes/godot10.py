from flask import Blueprint, render_template, request

bp = Blueprint('godot10', __name__)

@bp.route('/godot10', methods=['GET'])
def index():
    return render_template('godot10/index.html')