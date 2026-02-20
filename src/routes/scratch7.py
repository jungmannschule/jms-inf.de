from os import name

from flask import Blueprint, render_template

bp = Blueprint('scratch7', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('scratch7/index.html')

@bp.route('/2025', methods=['GET'])
def index_2025():
    return render_template('scratch7/index-2025.html')

@bp.route('/p5js', methods=['GET'])
def index_p5js():
    return render_template('scratch7/index-p5js.html')

@bp.route('/p5js/<acc>', methods=['GET'])
def student_page(acc):
    scratchid = None
    file = f'js/p5js/{acc}.js'
    match acc:
        case 'kingjulienbam':       scratchid = 1149369178
        case 'lfcombo':             scratchid = 1148291057
        case 'roma_universita12':   scratchid = 1147065837
        case 'gurkiundpotatoe':     scratchid = 1148293075
        case 'peter_tuerlich':      scratchid = 1149368917
        case 'primesilxncx':        scratchid = 1149372452
        case 'bienenschildkroeten': scratchid = 1152259111
        case 'ichwilleineisteee':   scratchid = 1155034887
        case 'itsonlyfinjanelly':   scratchid = 1147066015
        case 'todesstern13':        scratchid = 1149369189
    return render_template(f'scratch7/single_template.html', acc=acc, scratchid=scratchid, file=file)