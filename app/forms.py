from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL


class URLForm(FlaskForm):
    original_url = StringField('Вставьте ссылку',
                               validators=[DataRequired(message='Это поле не должно быть пустым'), Length(1, 255),
                                           URL(message='Неверная ссылка')])
    submit = SubmitField('Получить короткую ссылку')