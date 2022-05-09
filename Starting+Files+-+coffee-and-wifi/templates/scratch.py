<div class="form-group">
                              {{ form.coffee_rating.label(class="form-control-label") }}

                              {% if form.coffee_rating.errors %}
                                  {{ form.coffee_rating(class="form-control form-control-lg is-invalid") }}
                                  <div class="invalid-feedback">
                                      {% for error in form.coffee_rating.errors %}
                                          <span>{{ error }}</span>
                                      {% endfor %}
                                  </div>
                              {% else %}
                                  {{ form.coffee_rating(class="form-control form-control-lg") }}
                              {% endif %}
                          </div>


 url_name = StringField('Location', validators=[DataRequired()])
    opening_time = StringField('Open', validators=[DataRequired()])
    closing_time = StringField('Location', validators=[DataRequired()])



<!DOCTYPE html>
<html>
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}">

    {% if title %}
        <title>Flask Blog - {{ title }}</title>
    {% else %}
        <title>Flask Blog</title>
    {% endif %}
</head>

import <link rel="stylesheet" type="text/css" href="custom.css">