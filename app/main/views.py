from flask import (render_template, redirect,
                   url_for, request, flash)

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET'])
def redirection_index():
    return redirect(url_for('main.index'))


@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')
