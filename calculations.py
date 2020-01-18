from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import pandas as pd
import numpy as np
bp = Blueprint('calculations', __name__)

@bp.route('/')
def index():
	df1 = pd.read_csv('C:/Users/100707158/Documents/Visual Studio 2019/Oec 2020/inputFile.csv')
	arr = df1.to_numpy()
	line = arr[6]
	#print(arr[0])

	#display index page and send patients data to it
	return render_template('index.html', display = line)
