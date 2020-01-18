from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import pandas as pd
import numpy as np
import time
#from calculations import currentHour
bp = Blueprint('calculations', __name__)


global currentHour 
currentHour = 0

global previousNuc
previousNuc = 0
@bp.route('/', methods=('GET', 'POST'))
def index():
	global currentHour 
	global previousNuc

	error = ""
	
	Starting = []
	current = []
	df1 = pd.read_csv('C:/Users/100707158/Documents/Visual Studio 2019/Oec 2020/inputFile.csv')
	arr = df1.to_numpy()

	#skip the first three arrays scince they are initial values
	initial = arr[1][4]
	current = arr[currentHour + 3]


	Energyarr = current[3:10]
	temperature = current[10]
	demand = current[2]
	colvals = ["Solar","Nuclear","Wind","Hydro","Coal","Biofuel","Neighbor"]

	energyUsable= dict(zip(colvals,Energyarr))

	if currentHour == 0:
		energyUsable["Nuclear"] = initial
		previousNuc = energyUsable["Nuclear"]
		
	else:
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
	
		if used > demand:
			difference = used - demand
			energyUsed[key] -= difference
			used = get_energy_used(energyUsed)
			break

	#totalCost = calculatecost(energyUsed)
	
	currentHour += 1
	
		

	return render_template('index.html', display = energyUsed, usable = energyUsable, demand = demand, used = used, error = error)

def get_energy_used(used_dict):
	total = 0

	for value in used_dict.values():
		total += float(value)

	return total

def calculate_cost(energy):
    result = 0
    

    ts = energy['Solar'] * cost
    result += ts/1000
    ns = energy['Nuclear'] * cost
    result += ns/1000
    hs = energy['Hydro'] * cost
    result += hs/1000
    gs = energy['Gas/oil'] * cost
    result += gs/1000
    bs = energy['Biofuel'] * cost
    result += bs/1000
    neis = energy['Neighboor'] * cost
    result += neis/1000

    return result

def calculate_revenue(temp, time):
	cost = 0
	if 10 <= temp <= 50:
		if 7 <= time < 11:
			cost = 0.094
		elif 11 <= time < 17:
			cost = 0.134
		elif 17 <= time < 19:
			cost = 0.094
		elif 19 <= time <= 23:
			cost = 0.065
		elif 0 <= time < 7:
			cost = 0.065

	elif -50 <= temp < 10:
		if 7 <= time < 11:
			cost = 0.134
		elif 11 <= time < 17:
			cost = 0.094
		elif 17 <= time < 19:
			cost = 0.134
		elif 19 <= time <= 23:
			cost = 0.065
		elif 0 <= time < 7:
			cost = 0.065
	return cost

def update_current_hour(hour):
	hour += 1
	return hour