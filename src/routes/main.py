import os
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, flash, request, make_response, current_app, send_file, \
    send_from_directory
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from src.forms import LoginForm

bp = Blueprint('main', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if not check_password_hash('pbkdf2:sha256:600000$UDTKm83SP2K0c4fv$8e761271860df15736c60886e1a3652f68dc0562b8fbb9a1b7ef317f1805bff5', form.password.data):
            flash(f'Login oder Passwort ungültig.')
            return redirect(url_for('main.login'))
        resp = make_response(redirect(url_for('main.steckbriefe_index')))
        resp.set_cookie('user')
        return resp
    return render_template('login.html', form=form)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/odp')
def upload_odp():
    return send_from_directory('static', 'social-media-unter-14.odp')


@bp.route('/steckbriefe')
def steckbriefe_index():
    if request.cookies.get('user') is None:
        return redirect(url_for('main.login'))
    return render_template('steckbriefe/index.html')


@bp.route('/steckbriefe/<string:student>')
def steckbrief(student):
    if request.cookies.get('user') is None:
        return redirect(url_for('main.login'))
    return render_template(f'steckbriefe/{student}')


@bp.route('/farben')
def farben_index():
    dez = range(0, 33)
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, '1a', '1b', '1c', '1d', '1e', '1f', 20]
    bin = [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111, 100000]
    return render_template('farben/index.html', hex=hex, dez=dez, bin=bin)


@bp.route('/flexbox')
def flexbox_index():
    return render_template('flexbox/odin.html')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'zip', 'gzip', 'gz', '7z', 'rar'}


@bp.route('/projekt', methods=['GET', 'POST'])
def projekt_index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Fehler: Keine Datei ausgewählt.')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Fehler: Keine Datei ausgewählt.')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('Fehler: Es werden nur ZIP-Dateien akzeptiert.')
        if file and allowed_file(file.filename):
            unique = datetime.utcnow().strftime('%y%m%d-%H%M%S')
            filename = f'{unique}-{secure_filename(file.filename)}'
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            flash('Datei erfolgreich hochgeladen!')
    return render_template('projekt/index.html')

@bp.route('/mac')
def mac_on_google_sheets():
    return redirect('https://docs.google.com/spreadsheets/d/1u1RwwwOthMlUt4nvrCw1qHDb7vpYRwPb5PpvfO6zJ7U/edit?gid=0#gid=0')

@bp.route('/hack')
def hacking_lab():
    return redirect('https://node-xejd.onrender.com/')

@bp.route('/robot')
def not_a_robot():
    return redirect('https://neal.fun/not-a-robot/')

@bp.route('/go')
def go_lab():
    return redirect('https://golab.gg/')

