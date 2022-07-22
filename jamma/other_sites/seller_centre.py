from flask import Blueprint, render_template

seller_centre_bp = Blueprint('seller_centre', __name__)


@seller_centre_bp.route('/')
def seller_centre():
    return render_template('index.html')
