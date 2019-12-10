from flask import Flask, render_template

app = Flask("Jumanji", template_folder="app", static_folder="app")

@app.route("/")
def home():
    return render_template("templates/home.html")

@app.route("/donate")
def donate():
    return render_template("templates/donate.html")

if __name__ == "__main__":
    app.run(debug=True)
