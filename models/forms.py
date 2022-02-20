from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired('No title no post!')])
    # body = TextAreaField('B1ody', validators=[DataRequired('No text no post!')])