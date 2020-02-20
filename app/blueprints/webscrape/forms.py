from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DataForm(FlaskForm):
    search = StringField()
    submit = SubmitField('Scrape Data')

class SessionForm(FlaskForm):
    submit = SubmitField('CLEAR SESSION')

class CSVForm(FlaskForm):
    submit = SubmitField('Save to CSV')
    
class CronjobForm(FlaskForm):
    submit = SubmitField("SET CRONJOB")