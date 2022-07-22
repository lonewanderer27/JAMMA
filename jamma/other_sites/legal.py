from flask import render_template, Blueprint

legal_bp = Blueprint('legal', __name__)


@legal_bp.route('/terms_of_service')
def terms_of_service():
    return render_template('index.html')


@legal_bp.route('/privacy_policy')
def privacy_policy():
    return render_template('index.html')
