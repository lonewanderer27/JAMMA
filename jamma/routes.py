from jamma import app
from flask import render_template
from jamma.sites.signup.routes import signup_bp
from jamma.sites.login.routes import login_bp
from jamma.other_sites.legal import legal_bp
from jamma.other_sites.seller_centre import seller_centre_bp
from jamma.other_sites.help_center import help_center_bp
from jamma.other_sites.about import about_bp
from jamma.other_sites.careers import careers_bp
from jamma.other_sites.blog import blog_bp

# Register main websites
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(signup_bp, url_prefix='/signup')

# Register minor websites
app.register_blueprint(about_bp, url_prefix='/about')
app.register_blueprint(blog_bp, url_prefix='/blog')
app.register_blueprint(legal_bp, url_prefix='/legal')
app.register_blueprint(seller_centre_bp, url_prefix='/seller_centre')
app.register_blueprint(help_center_bp, url_prefix='/help_center')
app.register_blueprint(careers_bp, url_prefix='/careers')



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')
