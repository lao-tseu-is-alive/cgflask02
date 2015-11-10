from wtforms import Form, BooleanField, DateTimeField
from wtforms import TextAreaField, StringField
from wtforms.validators import Length, required


class AppointmentForm(Form):
    title = StringField('Title', [Length(max=255)])
    start = DateTimeField('Start', [required()])
    end = DateTimeField('End')
    allday = BooleanField('All Day')
    location = StringField('Location', [Length(max=255)])
    description = TextAreaField('Description')
