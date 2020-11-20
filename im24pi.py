# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# https://www.immobilienscout24.de/sitemap.html
# https://www.immobilienscout24.de/geoautocomplete/v3/locations.json?i=mannheim

import os.path
import random
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
from time import sleep
import csv


headers = [
		# Firefox 77 Mac
		{
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Referer": "https://www.google.com/",
			"DNT": "1",
			"Connection": "keep-alive",
			"Upgrade-Insecure-Requests": "1"
		},
		]

headers = random.choice(headers)

url = "https://www.immobilienscout24.de/Suche/radius/haus-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&enteredFrom=one_step_search"

# Get parent page
def fetch_parent():
    
	response = requests.get(url, headers=headers)
	print(response.status_code)
	#print(response.text)
	soup = BeautifulSoup(response.content, features="lxml")
	ls_expose = []
	for a in soup.select('a'):
				if 'expose' in a['href']:
					ls_expose.append(a['href'])            
	ls_expose = (set(ls_expose))
	ls_expose = list(ls_expose)
	# Get link to first details page

	# Get expose link for each of 20 detail pages, visit it, and parse details

	for i, exp in enumerate(ls_expose):
		relative_link = exp
		url2 = urljoin('https://www.immobilienscout24.de/', relative_link)
		response = requests.get(url2, headers=headers)
		soup = BeautifulSoup(response.content, features="lxml")
		parse_details(soup)
		if i % 5 == 4:
			print("switch vpn") ### TBC
			sleep(80) # TBC

# get next 20 listings
def nav_next_parent():
	pass

# parse child page #
def parse_details(soup):

	print("----------")
	address=''
	price='' 
	postcode=''
	livingspace='' 
	rooms='' 
	parking=''
	provision=''
	provision_note=''
	mieteinnahmen=''
	hausgeld=''
	# ADDRESS
	try:
		address = soup.find('div', class_='font-ellipsis').text
		address = address.replace(',', '')
		print(address)
	except:
		pass

	# PRICE
	try:
		price = soup.find('div', class_ ='is24qa-kaufpreis-main is24-value font-semibold is24-preis-value')
		price = price.text
		print(price)
	except:
		pass

	# POSTCODE # 
	try:
		postcode = soup.find('span', class_ = 'zip-region-and-country').text
		print(postcode)
	except:
		pass

	# LIVING SPACE #
	try:
		livingspace = soup.find('dd', class_ =  'is24qa-wohnflaeche-ca grid-item three-fifths').text
		livingspace = livingspace.strip()
		print(livingspace)
	except:
		pass

	# ROOMS
	try:
		rooms = soup.find('dd', class_ = 'is24qa-zimmer').text
		rooms = rooms.strip()
		print(rooms)
	except:
		pass
	# PARKING
	try:
		parking = soup.find('dd', class_ = 'is24qa-garage-stellplatz grid-item three-fifths').text
		parking = parking.strip()
		print(parking)
	except:
		pass

	# PROVISION
	try:
		provision = soup.find('dd', class_ = 'is24qa-provision').text
		provision = provision.strip()
		print(f"provision={provision}")
	except:
		pass

	# PROVISION_NOTE
	try:
		provision_note = soup.find('dd', class_ = 'is24qa-provision-note').text
		provision_note = provision_note.strip()
		print("provision note")
		print(provision_note)
	except:
		pass

	# Mieteinnahmen
	try:
		mieteinnahmen = soup.find('dd', class_ = 'is24qa-mieteinnahmen-pro-monat').text
		mieteinnahmen= mieteinnahmen.strip()
		print("mieteinnahmen=")
		print(mieteinnahmen)
	except:
		pass
	
	# Hausegeld
	try:
		hausgeld = soup.find('span', class_ = 'is24qa-hausgeld').text
		hausgeld = hausgeld.strip()
		print("hausgeld=")
		print(hausgeld)
	except:
		pass
	
 
	headers=['address', 
		'price', 
		'postcode', 
		'livingspace', 
		'rooms', 
		'parking',
		'provision',
		'provision_note',
		'mieteinnahmen',
		'hausgeld' ]

	file_exists = os.path.isfile('immo_results.csv')
 
	with open('immo_results.csv', 'a+',newline='') as csvfile:
		writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
		if not file_exists:
			writer.writeheader()
		writer.writerow({'address':address,'price':price, 'postcode':postcode,'livingspace':livingspace,'rooms':rooms,'parking':parking,'provision':provision, 'provision_note':provision_note,'mieteinnahmen':mieteinnahmen,'hausgeld':hausgeld})

	sleep(1)

# Main Driver #
if __name__ == '__main__':

	fetch_parent()
	
