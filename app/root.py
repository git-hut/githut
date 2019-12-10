from flask import Flask, render_template

app = Flask("Jumanji", template_folder="app", static_folder="app")

@app.route("/")
def root():
    return render_template("templates/index.html")

@app.route("/donate")
def root():
    return render_template("templates/donate.html")

if __name__ == "__main__":
    app.run()
