#Programe to change the Temprature into Kelvin ferienheit and celcius

def CelsiusToKelvin(tempValue):
	response = tempValue + 273.15    # celcius to kelvin
	return response

def KelvinToCelsius(tempValue):      # kelvin to celsius
	response = tempValue - 273.15
	return response

def CelsiusToFahrenheit(tempValue):    # celsius to fahrenheit
	response = ((( 9/5 ) * tempValue ) + 32)
	return response

def FahrenheitToCelsius(tempValue):	  # Fahrenheit to celsius
	response = ((tempValue - 32) * (5 / 9))
	return response


value,temp = input("Enter Temprature ::  ").split(" ")   # input values and temprature notations
changetemp = input("Enter the Change Notation ::  ")

value = eval(value)     # Explicit type casting
temp = temp.lower()    # convert notations to lower form
changetemp = changetemp.lower()
changetemp = changetemp.strip()

# celsius to kelvin check condition.
if ((temp == 'c' or temp == 'celcius') and (changetemp == 'k' or changetemp == 'kelvin')):
	temprature = CelsiusToKelvin(value)
	print(temprature,"Kelvin")
else :
	if ((temp == 'k' or temp == 'kelvin') and (changetemp == 'c' or changetemp == 'celsius')):
		temprature = KelvinToCelsius(value)
		print(temprature,"Celsius")
	else:
		if ((temp == 'c' or temp == 'celsius') and (changetemp == 'f' or changetemp == 'fahrenheit')):
			temprature = CelsiusToFahrenheit(value)
			print(temprature,"Fahrenheit")
		else:
			if ((temp == 'c' or temp == 'celsius') and (changetemp == 'c' or changetemp == 'celsius')):
				temprature = value
				print(temprature,'Celsius')
			else:
				if ((temp == 'k' or temp == 'kelvin') and (changetemp == 'f' or changetemp == 'fahrenheit')):
					temprature = KelvinToCelsius(value)
					temprature = CelsiusToFahrenheit(temprature)
					print(temprature,'Fahrenheit')
				else:
					if ((temp == 'k' or temp == 'kelvin') and (changetemp == 'k' or changetemp == 'kelvin')):
						temprature = value
						print(temprature,'Kelvin')
					else:
						if ((temp == 'f' or temp == 'fahrenheit') and (changetemp == 'f' or changetemp == 'fahrenheit')):
							temprature = value
							print(temprature,'Fahrenheit')
						else:
							if ((temp == 'f' or temp == 'fahrenheit') and (changetemp == 'k' or changetemp == 'kelvin')):
								temprature = FahrenheitToCelsius(value)
								temprature = CelsiusToKelvin(temprature)
								print(temprature,'Kelvin')
							else:
								temprature = FahrenheitToCelsius(value)
								print(temprature,'Celsius')



