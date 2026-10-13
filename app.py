from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    age = request.form.get("age")
    college = request.form.get("college")
    Email = request.form.get("Email")
    AdmissionID = request.form.get("AdmissionID")

    return render_template(
        "profile.html",
        name=name,
        age=age,
        college=college,
        Email = Email,
        AdmissionID = AdmissionID
    )

if __name__ == "__main__":
    app.run(debug=True)