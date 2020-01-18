from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import pandas as pd
import numpy as np
bp = Blueprint('calculations', __name__)

@bp.route('/')
def index():

	currentHour = 0
	Starting = []
	current = []
	df1 = pd.read_csv('C:/Users/100707158/Documents/Visual Studio 2019/Oec 2020/inputFile.csv')
	arr = df1.to_numpy()

	#skip the first three arrays scince they are initial values
	previousNuc = arr[1][4]
	current = arr[currentHour + 3]
	#for x in arr:
		#if x[0] ==0:
			#Starting.append(x)
		#else:
			#current = x
			#break


	Energyarr = current[3:10]
	temperature = current[10]
	demand = current[2]
	colvals = ["Solar","Nuclear","Wind","Hydro","Coal","Biofuel","Neighbor"]

	energyUsable= dict(zip(colvals,Energyarr))
	energyUsable["Nuclear"] = previousNuc

	#energy used in order of least to most CO2 production
	energyUsed = {
		"Hydro": 0,
		"Nuclear": 0,
		"Wind": 0,
		"Biofuel":0,
		"Solar": 0,
		"Neighbor": 0,
		"Coal": 0
		}

	for key in energyUsed:
		energyUsed[key] = energyUsable[key]
		used = get_energy_used(energyUsed)
	#energyUsed["Hydro"] = energyUsable["Hydro"]
	
		if used > demand:
			difference = used - demand
			energyUsed[key] -= difference
			used = get_energy_used(energyUsed)
			break

	return render_template('index.html', display = energyUsed, usable = energyUsable, demand = demand, used = used)

def get_energy_used(used_dict):
	total = 0
	for value in used_dict.values():
		total += int(value)

	return total
