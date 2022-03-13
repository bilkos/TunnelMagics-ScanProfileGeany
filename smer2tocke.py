# Program za izračun smeri (azimuta) vektorja iz koordinat dveh točk
# Izdelal: Boris Bilc, Radohova vas 14B, 1296 Šentvid pri Stični, Slovenija
# Datum: 2022/03/02

import numpy as np
import math
from colorama import init, Fore, Back, Style


def direction_lookup(destination_x, origin_x, destination_y, origin_y):
	deltaX = destination_x - origin_x
	deltaY = destination_y - origin_y
	degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180
	if degrees_temp < 0:
		degrees_final = 360 + degrees_temp
	else:
		degrees_final = degrees_temp
    # compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    # compass_lookup = round(degrees_final / 45)
    # return compass_brackets[compass_lookup], degrees_final

	return(degrees_final)


def azimut_vektor(x, y):
	print(Fore.CYAN + "Vnos koordinat za 2. točko na osi")
	
	print(Fore.CYAN + "Decimalno ločilo je lahko '.' (pika) ali ',' (vejica).")

	print("\n" + Fore.YELLOW + "Koordinata E:")
	x2 = input(">>> ")
	if x2 == "":
		x2 = float(1)
	else:
		x2 = float(x2.replace(",", "."))

	print(Fore.YELLOW + "Koordinata N:")
	y2 = input(">>> ")
	if y2 == "":
		y2 = float(1)
	else:
		y2 = float(y2.replace(",", "."))

	azimut = direction_lookup(x2, x, y2, y)
	
	print("\n" + Fore.CYAN + "Izračun azimuta:")
	print(Style.BRIGHT + Fore.BLUE + "Točka 1\n E: " + str(x) + "m\n N: " + str(y) + "m")
	print(Style.BRIGHT + Fore.BLUE + "Točka 2\n E: " + str(x2) + "m\n N: " + str(y2) + "m")
	print("\n" + Style.BRIGHT + Fore.BLUE + "Izračunan azimut OSI: " + str(azimut))
	
	return(azimut)
