from flask import Blueprint, render_template, request

bp = Blueprint('project10', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('project10/index.html')

@bp.route('/partials', methods=['GET'])
def test():
    keys = [k for k in request.args.keys()]
    if keys:
        return render_template(f'project10/{keys[0]}.partial')
    return render_template('project10/welcome.partial')