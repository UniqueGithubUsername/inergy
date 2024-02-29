from django import forms
from pymongo import MongoClient

CHOICES = [('','Please select...')]

client = MongoClient()
client = MongoClient('131.154.97.22', 27017, username="root", password="inergySt0rag32oo22!")
db = client['inergy_prod_db']
collections = db.list_collection_names()

for c in collections:
	CHOICES.append((c,c))

class PredictiveMaintenanceForm(forms.Form):
	collection = forms.ChoiceField(choices=CHOICES, required=True)