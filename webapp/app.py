import os
from flask import Flask, render_template, request
from converter import Inputs, Parser, Converter

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from wtforms import ValidationError

app = Flask(__name__)


class ConvertForm(FlaskForm):
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Convert')


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")

