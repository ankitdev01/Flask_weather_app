import requests
from flask import Flask, render_template,request,redirect


app = Flask(__name__)

@app.route('/')
def page():
	weather={
			'city' : 'N/A',
			'temperature' : 'N/A',
			'description' : 'N/A',
		     }
	return render_template('home.html',weather=weather)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		city = request.form['city']
		# print(city)
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=42b9eed7b043ca54cb3231dc33db2c69'
		r = requests.get(url.format(city)).json()
		print(r)

		# Code for conversion
		temperature=  r['main']['temp']
		temperature = float((float(temperature)-273.15)*(9/5)+32)
		print(temperature)
		weather={
			'city' : city,
			'temperature' : str(temperature),
			'description' : (r['weather'][0]['description']).title(),
			'icon' : r['weather'][0]['icon']
		     }
		print(weather)
		return render_template('home.html',weather=weather)
	else:
		print('Mistaken')
		return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)