from flask import Blueprint, render_template


careers_bp = Blueprint('careers', __name__)


@careers_bp.route('/')
def careers():
    return render_template('index.html')
