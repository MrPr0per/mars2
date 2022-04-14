from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField('Главнокомандующий (id)')
    job = TextAreaField("Что нужно сделать")
    work_size = IntegerField('объем работ в часах')
    collaborators = StringField('колоборационисты (их id)')
    submit = SubmitField('Применить')