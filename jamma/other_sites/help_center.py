from flask import Blueprint, render_template

help_center_bp = Blueprint('help_center', __name__)


@help_center_bp.route('/')
def help_center():
    return render_template('help_center.html')
