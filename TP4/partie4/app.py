from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenue sur le TP Flask !"

@app.route("/newuser/", methods=["GET", "POST"])
def newuser():
    message = ""
    if request.method == "POST":
        username = request.form["username"]

        # Critères de validation
        if len(username) < 6:
            message = "L'identifiant doit contenir au moins 6 caractères."
        elif not re.search(r"\d", username):
            message = "L'identifiant doit contenir au moins un chiffre."
        elif not re.search(r"[A-Z]", username):
            message = "L'identifiant doit contenir au moins une majuscule."
        elif not re.search(r"[a-z]", username):
            message = "L'identifiant doit contenir au moins une minuscule."
        elif not re.search(r"[#%{}@]", username):
            message = "L'identifiant doit contenir au moins un caractère spécial parmi : #%{}@"
        else:
            message = "Identifiant valide !"

    return render_template("newuser.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

