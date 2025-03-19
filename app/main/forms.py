from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired()])
    submit = SubmitField('提交')
    password = PasswordField('密码', validators=[DataRequired()])
