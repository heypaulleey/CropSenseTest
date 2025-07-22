from flask import Flask, render_template, request, redirect, session, jsonify
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-adminsdk.json")  # Replace with your key filename
    firebase_admin.initialize_app(cred)

@app.route("/")
def index():
    if "uid" in session:
        return render_template("index.html")
    return redirect("/login")
@app.route("/login")
def login():
    if "uid" in session:
        return redirect("/dashboard")  # Prevent access to login if already logged in
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/recent-reports")
def recent_reports():
    return render_template("recent_reports.html")

@app.route("/soil-reports")
def soil_reports():
    return render_template("soil_reports.html")

@app.route("/dashboard")
def dashboard():
    if "uid" in session:
        return render_template("index.html")
    return redirect("/login")

@app.route("/sessionLogin", methods=["POST"])
def session_login():
    id_token = request.json.get("idToken")
    try:
        decoded_token = auth.verify_id_token(id_token)
        session["uid"] = decoded_token["uid"]
        return jsonify({"message": "Login success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route("/logout")
def logout():
    session.clear()  # Clears all session data, not just uid
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
