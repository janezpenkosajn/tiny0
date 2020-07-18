from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length

# Validates a URL
def validate_URL(form, field):
	# Make sure the url is not too short or long
	if len(field.data) < 4 or len(field.data) > 2000:
		# Raise a ValidationError
		raise ValidationError()

	# If the url contains spaces or does not have any dots
	if field.data.count(" ") > 0 or field.data.count(".") == 0:
		# Raise a ValidationError
		raise ValidationError()

	# If the URL does not start with http:// and https://
	if not(field.data.startswith("http://")) and not(field.data.startswith("https://")):
		# Add https:// to the beginning of the URL
		field.data = "https://" + field.data


class URLForm(FlaskForm):
	url = StringField(validators=[DataRequired(), Length(min=4, max=2000), validate_URL])

	submit = SubmitField("Shorten URL")
