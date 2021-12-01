from __main__ import app

@app.route("/admin")
def admin_home():
    return "Admin Page"