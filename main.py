# Program za generiranje merjenega profila
# Izdelal: Boris Bilc, Radohova vas 14B, 1296 Šentvid pri Stični, Slovenija
# Datum: 2022/03/13
# Verzija: 0.1 (beta)


import os
import math
import random
import time
import datetime
import smer2tocke
import numpy as np
from colorama import init, Fore, Back, Style

init(autoreset=True)


# Vnos koordinat točke v osi profila
def vnos_koo():
	global os_x, os_y, os_z, azi_os, azi_prof
	print("\n" + Fore.CYAN + "Vnos koordinat točke v osi profila in azimut osi")
	print(Fore.CYAN + "Decimalno ločilo je lahko '.' (pika) ali ',' (vejica).")
	print(Fore.YELLOW + "Koordinata E:")
	os_x = input(">>> ")
	if os_x == "":
		os_x = float(0)
	else:
		os_x = float(os_x.replace(",", "."))
	print(Fore.YELLOW + "Koordinata N:")
	os_y = input(">>> ")
	if os_y == "":
		os_y = float(0)
	else:
		os_y = float(os_y.replace(",", "."))
	print(Fore.YELLOW + "Višina H:")
	os_z = input(">>> ")
	if os_z == "":
		os_z = float(0)
	else:
		os_z = float(os_z.replace(",", "."))
	
	potrdi_vektor = ""
	print(Fore.CYAN + "(" + Style.BRIGHT + "Enter" + Style.NORMAL + ") vnos azimuta / (" + Style.BRIGHT + "I" + Style.NORMAL + ") " + Style.BRIGHT + "I" + Style.NORMAL + "zračun azimuta")
	potrdi_vektor = input()
	if potrdi_vektor == "I" or potrdi_vektor == "i":
		potrdi_vektor == ""
		azi_os = smer2tocke.azimut_vektor(os_x, os_y)
	elif potrdi_vektor == "":
		print(Fore.YELLOW + "Azimus OS:")
		azi_os = input(">>> ")
		azi_os = azi_os.replace(",", ".")
	
	if azi_os == "":
		azi_os = float(0)
		azi_prof = float(90)
	elif float(azi_os) < 270:
		azi_prof = float(azi_os) + 90
	else:
		azi_prof = float(azi_os) - 360 + 90
	
	# Izpis vnešenih podatkov
	print("\n" + Style.BRIGHT + Fore.GREEN + "Koordinate profila v OSI\n E: " + str(os_x) + "m\n N: " + str(os_y) + "m\n H: " + str(os_z) + "m")
	print(Style.BRIGHT + Fore.GREEN + "Azimut\n OS: " + str(azi_os) + "\n PROFIL: " + str(azi_prof))
	
	potrdi = ""
	print(Fore.MAGENTA + "Potrditev vnosa: (" + Style.BRIGHT + "Enter" + Style.NORMAL + ") OK / (" + Style.BRIGHT + "P" + Style.NORMAL + ") " + Style.BRIGHT + "P" + Style.NORMAL + "onovi / (" + Style.BRIGHT + "Z" + Style.NORMAL + ") I" + Style.BRIGHT + "z" + Style.NORMAL + "hod")
	potrdi = input()
	if potrdi == "P" or potrdi == "p":
		potrdi == ""
		vnos_koo()
	elif potrdi == "Z" or potrdi == "z":
		quit()



# Izbira tipa profila po katerem se računajo nove koordinate
def izbira_prof():
	global tip_profila
	global dat_profila
	print("\n" + Fore.CYAN + "Možni tipi profilov: ")
	arr = next(os.walk('profili/'))[2]
	stdat = 0
	for dat in arr:
		dat = dat.replace(".txt", "")
		print("> " + Fore.RED + Style.BRIGHT + str(stdat) + Style.NORMAL + " - " + dat.upper())
		stdat = stdat + 1
	print("\n" + Fore.YELLOW + "Vnesi številko profila >>>")
	tip_profila = input(">>> ")
	if tip_profila != "":
		dat_profila = arr[int(tip_profila)]
		print("\n" + Fore.GREEN + "Izbran tip profila: " + Style.BRIGHT + tip_profila + " - " + arr[int(tip_profila)].replace(".txt", "").upper())
	else:
		tip_profila = "0"
		dat_profila = arr[int(tip_profila)]
		print("\n" + Fore.GREEN + "Izbran je prvi profil iz seznama: " + Style.BRIGHT + tip_profila + " - " + arr[int(tip_profila)].replace(".txt", "").upper())
	
	potrdi = ""
	print(Fore.MAGENTA + "Potrditev vnosa: (" + Style.BRIGHT + "Enter" + Style.NORMAL + ") OK / (" + Style.BRIGHT + "P" + Style.NORMAL + ") " + Style.BRIGHT + "P" + Style.NORMAL + "onovi / (" + Style.BRIGHT + "Z" + Style.NORMAL + ") I" + Style.BRIGHT + "z" + Style.NORMAL + "hod")
	potrdi = input()
	if potrdi == "P" or potrdi == "p":
		potrdi == ""
		izbira_prof()
	elif potrdi == "Z" or potrdi == "z":
		quit()



def vnos_odstopanja():
	global raz_min, raz_max
	print("\n" + Fore.YELLOW + "Vnesi minimalno vrednost za raztros (v mm):")
	raz_min = input(">>> ")
	if raz_min == "":
		raz_min = 0
	print(Fore.YELLOW + "Vnesi maksimalno vrednost za raztros (v mm):")
	raz_max = input(">>> ")
	if raz_max == "":
		raz_max = 0

	raz_min_t = float(raz_min) / 1000
	raz_max_t = float(raz_max) / 1000
	print("\n" + Fore.GREEN + "Odstopanje - " + Style.BRIGHT + "MIN= " + str(raz_min_t) + "m / MAX= " + str(raz_max_t) + "m")
	
	potrdi = ""
	print(Fore.MAGENTA + "Potrditev vnosa: (" + Style.BRIGHT + "Enter" + Style.NORMAL + ") OK / (" + Style.BRIGHT + "P" + Style.NORMAL + ") " + Style.BRIGHT + "P" + Style.NORMAL + "onovi / (" + Style.BRIGHT + "Z" + Style.NORMAL + ") I" + Style.BRIGHT + "z" + Style.NORMAL + "hod")
	potrdi = input()
	if potrdi == "P" or potrdi == "p":
		potrdi == ""
		vnos_odstopanja()
	elif potrdi == "Z" or potrdi == "z":
		quit()


# Datoteka v katero bomo zapisali koordinate izračunanih točk
def datoteka_out():
	global datoteka_ime
	global datoteka_ime2
	global datoteka
	global datoteka2
	global time_dat
	time_dat = datetime.datetime.now()
	print("\n" + Fore.YELLOW + "Ime datoteke (brez končnice) >>>")
	datoteka_ime = input(">>> ")
	if datoteka_ime == "":
		datoteka_ime = dat_profila.replace(".txt", "_") + time_dat.strftime("%y%m%d-%H%M") + "_kontrola"
		datoteka_ime2 = dat_profila.replace(".txt", "_") + time_dat.strftime("%y%m%d-%H%M") + "_generiran"
	else:
		datoteka_ime = datoteka_ime + "_" + dat_profila.replace(".txt", "_") + time_dat.strftime("%y%m%d-%H%M") + "_kontrola"
		datoteka_ime2 = datoteka_ime + "_" + dat_profila.replace(".txt", "_") + time_dat.strftime("%y%m%d-%H%M") + "_generiran"
	print(Fore.GREEN + "Izhodna mapa/datoteka: ../izvoz-txt/" + Style.BRIGHT + datoteka_ime + ".txt")
	print(Fore.GREEN + "Izhodna mapa/datoteka: ../izvoz-txt/" + Style.BRIGHT + datoteka_ime2 + ".txt")
	
	potrdi = ""
	print(Fore.MAGENTA + "Potrditev vnosa: (" + Style.BRIGHT + "Enter" + Style.NORMAL + ") OK / (" + Style.BRIGHT + "P" + Style.NORMAL + ") " + Style.BRIGHT + "P" + Style.NORMAL + "onovi / (" + Style.BRIGHT + "Z" + Style.NORMAL + ") I" + Style.BRIGHT + "z" + Style.NORMAL + "hod")
	potrdi = input()
	if potrdi == "P" or potrdi == "p":
		potrdi == ""
		datoteka_out()
	elif potrdi == "Z" or potrdi == "z":
		quit()

	datoteka = open("izvoz-txt/" + datoteka_ime + ".txt", "a")
	datoteka2 = open("izvoz-txt/" + datoteka_ime2 + ".txt", "a")


# Računanje koordinat glede na izbrani projektiran profil
def racunanje_matrike():
	f = open("profili/" + dat_profila, "r")
	mat_x = f.readline().strip("\n").split(", ")
	mat_z = f.readline().strip("\n").split(", ")
	time.sleep(1)
	d = 0  # Števec podatkov
	i = 1  # Števec točk
	for data in mat_x:
		
  		# Pripravi vrednosti za razmet
		if raz_min == 0 and raz_max == 0:
			ods_rand_xz = float(0)
			ods_rand_xy = float(0)
		else:
			ods_rand_xz = float(random.randrange(int(raz_min), int(raz_max))) / 1000
			ods_rand_xy = float(random.randrange(int(raz_min), int(raz_max))) / 1000
	
 		# Izračun matrike z rotacijo
		izr_x = float(mat_x[d]) * math.sin(math.radians(float(azi_prof)))
		izr_y = float(mat_x[d]) * math.cos(math.radians(float(azi_prof)))
		izr_z = float(mat_z[d])
		# Koordinate profila po matriki
		koo_x = izr_x + float(os_x)
		koo_y = izr_y + float(os_y)
		koo_z = izr_z + float(os_z)
		# Izračun D, D2 in faktorja za smeri XZ
		dist_xz = math.sqrt((izr_x * izr_x) + (izr_z * izr_z))
		dist2_xz = math.sqrt((izr_x * izr_x) + (izr_z * izr_z)) + ods_rand_xz
		if dist_xz < 1:
			dist_xz = dist_xz + 1
			dist2_xz = dist2_xz + 1
		fakt_xz = dist2_xz / dist_xz
		# Izračun D, D2 in faktorja za smeri Y
		dist_y = math.sqrt((izr_x * izr_x) + (izr_y * izr_y))
		dist2_y = math.sqrt((izr_x * izr_x) + (izr_y * izr_y)) + ods_rand_xy
		if dist_y < 1:
			dist_y = dist_y + 1
			dist2_y = dist2_y + 1
		fakt_y = dist2_y / dist_y
		# Izračun matrike z raztrosom
		izr_n_x = izr_x * fakt_xz
		izr_n_y = izr_y * fakt_y
		izr_n_z = izr_z * fakt_xz
		# Koordinate profila z raztrosom
		koo_xp = izr_n_x + float(os_x)
		koo_yp = izr_n_y + float(os_y)
		koo_zp = izr_n_z + float(os_z)
		# IZVOZ PODATKOV V DATOTEKE
		# print(str(i) + "\t" + "{:.3f}".format(izr_x) + "\t" + "{:.3f}".format(izr_y) + "\t" + "{:.3f}".format(izr_z) + "\t|\t" + "{:.3f}".format(izr_n_x) + "\t" + "{:.3f}".format(izr_n_y) + "\t" + "{:.3f}".format(izr_n_z))
		print(str(i) + "\t" + "{:.3f}".format(koo_x) + "\t" + "{:.3f}".format(koo_y) + "\t" + "{:.3f}".format(koo_z) + "\t|\t" + "{:.3f}".format(koo_xp) + "\t" + "{:.3f}".format(koo_yp) + "\t" + "{:.3f}".format(koo_zp))

		datoteka.write(str(i) + "\t" + "{:.3f}".format(koo_x) + "\t" + "{:.3f}".format(koo_y) + "\t" + "{:.3f}".format(koo_z) + "\n")
		datoteka2.write(str(i) + "\t" + "{:.3f}".format(koo_xp) + "\t" + "{:.3f}".format(koo_yp) + "\t" + "{:.3f}".format(koo_zp) + "\n")

		# Inkrementacija števcev
		d = d + 1
		i = i + 1
		time.sleep(0.025)


def zacni_procesiranje():
	print(Fore.GREEN + Style.BRIGHT + "\nZa pričetek procesiranja pritisni " + Back.LIGHTGREEN_EX + Fore.BLACK + "Enter")
	procesiramo = input()
	if procesiramo == "":
		print(Fore.GREEN + "\nProcesiram...\n")
		racunanje_matrike()
		datoteka.close()
		datoteka2.close()
		print(Fore.GREEN + "Procesiranje končano...\n")
		print(Fore.YELLOW + "Nova datoteka 1: " + Style.BRIGHT + "/izvoz-txt/" + Fore.WHITE + Style.BRIGHT + datoteka_ime + ".txt")
		print(Fore.YELLOW + "Nova datoteka 2: " + Style.BRIGHT + "/izvoz-txt/" + Fore.WHITE + Style.BRIGHT + datoteka_ime2 + ".txt\n")
		print(Fore.RED + Style.BRIGHT + "Zaključim program? (Enter = Izhod / 'n' = Nova datoteka)")
		ponovimo = input()
		if ponovimo == "n" or ponovimo == "N":
			print(Fore.CYAN + "Gremo od začetka... trenutek...")
			time.sleep(0.5)
			delovni_proces()
		else:
			print(Fore.GREEN + Style.BRIGHT + "\nKonec programa...\n")
			time.sleep(0.5)
			quit()
	else:
		print(Back.RED + Fore.WHITE + "Gremo od začetka... trenutek...")
		time.sleep(1)
		delovni_proces()


def delovni_proces():
	vnos_koo()
	izbira_prof()
	vnos_odstopanja()
	datoteka_out()
	zacni_procesiranje()


# Začetek programa
print("\n")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + "-***************************************************************-")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + "|                                                               |")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + "|          Program za generiranje merjenega profila             |")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + "|                                                               |")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + "-***************************************************************-")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + " Podatki programa:                                               ")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + " Mapa - /docs > Dokumentacija in navodila za uporabo programa    ")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + " Mapa - /profili > Matrike projektiranih profilov za računanje   ")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + " Mapa - /izvoz-txt > Mapa za datoteke generiranih profilov       ")
print(" " + Style.DIM + Back.BLUE + Style.BRIGHT + Fore.YELLOW + "                                                                 ")
delovni_proces()
