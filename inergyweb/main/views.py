from django.shortcuts import render

import pymongo
from pymongo import MongoClient
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

from .forms import PredictiveMaintenanceForm

# Create your views here.
def index(request):
	if request.method == "POST":
		prform = PredictiveMaintenanceForm(request.POST)
		if prform.is_valid():
			collectionname = prform.cleaned_data['collection']

			client = MongoClient()
			client = MongoClient('131.154.97.22', 27017, username="root", password="inergySt0rag32oo22!")
			print("Connected to Mongo Client")
			db = client['inergy_prod_db']
			print("GOT DB")
			collection = db[collectionname]
			print("GOT COLLECTION")
			df = pd.DataFrame(list(collection.find()))
			print("GOT DATAFRAME:")
			#print(df.columns)
			#print(df)
			df = pd.DataFrame(df['calculations'])
			#print(df[0].keys())

			context = {'form':prform,'collection':collectionname,'df':df.to_html()}

			return render(request, 'main/index.html', context);
	else:
		prform = PredictiveMaintenanceForm()

	context = {'form':prform}
	return render(request, 'main/index.html', context);