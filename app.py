
import sqlite3
import os
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "kenduri-secret-key"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

# =============================
# VENDOR SIGNUP
# =============================
@app.route("/vendor/signup", methods=["GET", "POST"])
def vendor_signup():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        min_pax = int(request.form["min_pax"])
        max_pax = int(request.form["max_pax"])
        price_per_pax = int(request.form["price_per_pax"])
        whatsapp = request.form["whatsapp"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        db = get_db()
        db.execute("""
            INSERT INTO vendors 
            (name, location, min_pax, max_pax, price_per_pax, whatsapp, email, password)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, location, min_pax, max_pax, price_per_pax, whatsapp, email, hashed_password))
        db.commit()
        db.close()

        return redirect("/vendor/login")

    return render_template("vendor_signup.html")

# =============================
# LOGIN
# =============================
@app.route("/vendor/login", methods=["GET", "POST"])
def vendor_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        vendor = db.execute("SELECT * FROM vendors WHERE email=?", (email,)).fetchone()
        db.close()

        if vendor and check_password_hash(vendor["password"], password):
            session["vendor_id"] = vendor["id"]
            return redirect("/vendor/dashboard")
        else:
            return "Invalid login"

    return render_template("vendor_login.html")

# =============================
# DASHBOARD
# =============================
@app.route("/vendor/dashboard")
def vendor_dashboard():
    if "vendor_id" not in session:
        return redirect("/vendor/login")

    db = get_db()
    vendor = db.execute("SELECT * FROM vendors WHERE id=?", (session["vendor_id"],)).fetchone()
    db.close()

    return render_template("vendor_dashboard.html", vendor=vendor)

# =============================
# IMAGE UPLOAD
# =============================
@app.route("/vendor/upload", methods=["GET", "POST"])
def vendor_upload():
    if "vendor_id" not in session:
        return redirect("/vendor/login")

    if request.method == "POST":
        file = request.files["image"]

        if file and file.filename != "":
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)

            db = get_db()
            db.execute("UPDATE vendors SET image=? WHERE id=?", (filename, session["vendor_id"]))
            db.commit()
            db.close()

            return redirect("/vendor/dashboard")

    return render_template("vendor_upload.html")

# =============================
# SEARCH
# =============================
@app.route("/search", methods=["POST"])
def search():
    location = request.form["location"]
    pax = int(request.form["pax"])

    db = get_db()
    vendors = db.execute(
        "SELECT * FROM vendors WHERE location=? AND min_pax<=? AND max_pax>=?",
        (location, pax, pax)
    ).fetchall()
    db.close()

    return render_template("results.html", vendors=vendors)

@app.route("/vendor/logout")
def vendor_logout():
    session.clear()
    return redirect("/vendor/login")

if __name__ == "__main__":
    app.run(debug=True)

import sqlite3
import os
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "kenduri-secret-key"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

# =============================
# VENDOR SIGNUP
# =============================
@app.route("/vendor/signup", methods=["GET", "POST"])
def vendor_signup():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        min_pax = int(request.form["min_pax"])
        max_pax = int(request.form["max_pax"])
        price_per_pax = int(request.form["price_per_pax"])
        whatsapp = request.form["whatsapp"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        db = get_db()
        db.execute("""
            INSERT INTO vendors 
            (name, location, min_pax, max_pax, price_per_pax, whatsapp, email, password)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, location, min_pax, max_pax, price_per_pax, whatsapp, email, hashed_password))
        db.commit()
        db.close()

        return redirect("/vendor/login")

    return render_template("vendor_signup.html")

# =============================
# LOGIN
# =============================
@app.route("/vendor/login", methods=["GET", "POST"])
def vendor_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        vendor = db.execute("SELECT * FROM vendors WHERE email=?", (email,)).fetchone()
        db.close()

        if vendor and check_password_hash(vendor["password"], password):
            session["vendor_id"] = vendor["id"]
            return redirect("/vendor/dashboard")
        else:
            return "Invalid login"

    return render_template("vendor_login.html")

# =============================
# DASHBOARD
# =============================
@app.route("/vendor/dashboard")
def vendor_dashboard():
    if "vendor_id" not in session:
        return redirect("/vendor/login")

    db = get_db()
    vendor = db.execute("SELECT * FROM vendors WHERE id=?", (session["vendor_id"],)).fetchone()
    db.close()

    return render_template("vendor_dashboard.html", vendor=vendor)

# =============================
# IMAGE UPLOAD
# =============================
@app.route("/vendor/upload", methods=["GET", "POST"])
def vendor_upload():
    if "vendor_id" not in session:
        return redirect("/vendor/login")

    if request.method == "POST":
        file = request.files["image"]

        if file and file.filename != "":
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)

            db = get_db()
            db.execute("UPDATE vendors SET image=? WHERE id=?", (filename, session["vendor_id"]))
            db.commit()
            db.close()

            return redirect("/vendor/dashboard")

    return render_template("vendor_upload.html")

# =============================
# SEARCH
# =============================
@app.route("/search", methods=["POST"])
def search():
    location = request.form["location"]
    pax = int(request.form["pax"])

    db = get_db()
    vendors = db.execute(
        "SELECT * FROM vendors WHERE location=? AND min_pax<=? AND max_pax>=?",
        (location, pax, pax)
    ).fetchall()
    db.close()

    return render_template("results.html", vendors=vendors)

@app.route("/vendor/logout")
def vendor_logout():
    session.clear()
    return redirect("/vendor/login")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

