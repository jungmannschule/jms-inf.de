from flask import Blueprint, render_template, redirect, url_for, flash, request, make_response
from werkzeug.security import check_password_hash

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
    return render_template('farben/index.html')


@bp.route('/farben/hex')
def farben_hex():
    dez = range(0,31)
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 9, 'A', 'B', 'C', 'D', 'E', 'F', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, '?', '?', '?', '?', '?', '?']
    bin = ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '10000']
    return render_template('farben/hex.html', hex=hex, dez=dez, bin=bin)
