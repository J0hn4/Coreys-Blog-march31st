from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class AddCafeForm(FlaskForm):
    cafename = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    url_name = StringField('Email',
                        validators=[DataRequired(), Email()])
    opening_time = PasswordField('Password', validators=[DataRequired()])
    closing_time = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    coffee_rating = PasswordField('Confirm Password',
                                 validators=[DataRequired(), EqualTo('password')])
    wifi_rating = PasswordField('Confirm Password',
                                 validators=[DataRequired(), EqualTo('password')])
    power_rating = PasswordField('Confirm Password',
                                 validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit New Cafe')


