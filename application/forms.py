from flask.ext.wtf import Form
from wtforms import TextField, validators, SelectField, SubmitField, IntegerField, StringField
#from wtforms_sqlalchemy.fields import QuerySelectField


CUISINE_CHOICES = [(' ',' '), ('Mexican', 'Mexican') , ('Italian', 'Italian'), ('Indian', 'Indian'), ('French', 'French'), ('Thai', 'Thai'), ('Russian', 'Russian'), ('Spanish', 'Spanish'), ('Japanese', 'Japanese'), ('British', 'British'), ('Korean', 'Korean'), ]
CALORIES_PROTEIN_CHOICES = [(' ',' '), ('High Protein', 'High Protein'), ('Low Protein', 'Low Protein'), ('High Calories', 'High Calories'), ('Low Calories', 'Low Calories')]
PATTERNS = [('Mexican', 'Mexican') , ('Italian', 'Italian'), ('Indian', 'Indian'), ('French', 'French'), ('Thai', 'Thai'), ('Russian', 'Russian'), ('Spanish', 'Spanish'), ('Japanese', 'Japanese'), ('British', 'British'), ('Korean', 'Korean'), ]
TOWNS = [('Edison,NJ', 'Edison,NJ'), ('SouthPlainfield,NJ', 'SouthPlainfield,NJ'), ('Piscataway,NJ', 'Piscataway,NJ'), ('NewBrunswick,NJ', 'NewBrunswick,NJ')]
class complexForm(Form):
    cuisine = SelectField(label='Filter by Cuisine: ', choices=CUISINE_CHOICES)
    calories_protein = SelectField(label='Sort By: ', choices=CALORIES_PROTEIN_CHOICES)

    submit = SubmitField("Submit")

class moreInformation(Form):
    moreInfo = IntegerField('Search By ID', validators = [validators.NumberRange(min=1, max=11866)])
    zipCode = SelectField('Enter your City', choices=TOWNS)
    submit = SubmitField('Submit')

class patternVerf(Form):
    cuisine = SelectField(label='Pick Cuisine for Pattern Verification: ', choices=PATTERNS)
    submit = SubmitField('Submit')

class addFridge(Form):
    ing = StringField(label='Add to Fridge:')
    quan = IntegerField('Quantity: ',validators = [validators.NumberRange(min=1, max=11866)])
    submit = SubmitField('Submit')
