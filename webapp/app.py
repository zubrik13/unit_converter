import os
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from converter import Parser, Converter, arg_check

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


class ConvertForm(FlaskForm):
    amount = IntegerField("Amount")
    from_unit = StringField("Unit from")
    to_unit = StringField("Unit to")
    submit = SubmitField("Convert")


@app.route("/", methods=["GET", "POST"])
def index():
    form = ConvertForm()
    if form.validate_on_submit():

        amount = form.amount.data
        arg1 = form.from_unit.data
        arg2 = form.to_unit.data
        text = "==>"

        if arg_check(arg1):
            pass
        else:
            flash(f"Please enter valid unit, {arg1} is not supported", "danger")

        if arg_check(arg2):
            pass
        else:
            flash(f"Please enter valid unit, {arg2} is not supported", "danger")

        if arg_check(arg1) and arg_check(arg2):

            input_str = f"{amount} {arg1} {arg2}"
            inp = Parser().parse(input_str)
            result = Converter().result(inp)

            if result is None:
                flash(f"Units must be from same category!", "danger")
                return render_template("index.html", form=form)

            return render_template("index.html", amount=amount, arg1=arg1, \
                                    text=text, arg2=arg2, result=result, form=form)
        else:
            render_template("index.html", form=form)

    return render_template("index.html", form=form)

