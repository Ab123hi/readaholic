from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField, URLField, FileField
from wtforms.validators import Email, Length, EqualTo, DataRequired

class AdminRegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
                                     
    submit = SubmitField("Register")

class AdminLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    
    submit = SubmitField("Login")

class AdminAddBooksForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    isbn = IntegerField("ISBN", validators=[DataRequired()])
    genre = SelectField("Genre", validators=[DataRequired()], choices=[('book1', 'Fiction'), ('book2', 'Mystery'), ('book3', 'Politics'),('book4', 'History')])
    shop_link = URLField("Shop Link", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    upload_cover_image = FileField("Upload Cover Image", validators=[DataRequired()])
    tiny_summary = StringField("Tiny Summary", validators=[DataRequired()])

    submit = SubmitField("Save")
    