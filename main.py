# Make imports
from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, TextAreaField, SubmitField)

# Create flask object & secret key
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

# Create form


class SimpleForm(FlaskForm):
    name = StringField("Name")
    learning = SelectField("Today, my learning felt: ", choices=[(
        "strong", "Strong"), ("neutral", "Neutral"), ("not helpful", "Not helpful")])
    future_class = TextAreaField("Next class, I want to: ")
    submit = SubmitField("Submit")

# Route to pages


@app.route("/", methods=["POST", "GET"])
def index():
    # Create an SimpleForm object
    form = SimpleForm()

    if form.validate_on_submit():
        session["name"] = form.name.data
        session["learning"] = form.learning.data
        session["future_class"] = form.future_class.data

        return redirect(url_for("success"))

    return render_template("index.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
