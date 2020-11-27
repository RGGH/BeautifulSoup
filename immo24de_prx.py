# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
import os.path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
from time import sleep
from datetime import datetime
import csv
import mysql.connector
from mysql.connector import errorcode
from sys import platform

# Use same posted time for entire run 
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

# Set csv to false to write to database
export_csv = False

from scraper_api import ScraperAPIClient
client = ScraperAPIClient("8da8727186d0c7xxxxxxxxxxxxxxxxxxx") # use your own api key (register for trial)

if platform == "linux" or platform == "linux2":
    print("OS is Linux - this is the correct OS for this code\n")

if export_csv == False:
	print("Export to Database mode - no CSV\n")

#'Haus'
# url = "https://www.immobilienscout24.de/Suche/radius/haus-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&enteredFrom=one_step_search"

# 'Wohnung'
url = "https://www.immobilienscout24.de/Suche/radius/wohnung-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&enteredFrom=one_step_search"

# Get parent page
def fetch_parent(iurl):
    
	response = client.get(iurl)
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
		response = client.get(url2)
		soup = BeautifulSoup(response.content, features="lxml")
		parse_details(soup, url2)
		if i % 5 == 4:
			sleep(randint(1,10))

# parse child page #
def parse_details(soup, url2):

	print("----------")
	title=''
	price='' 
	postcode=''
	addressblock=''
	livingspace='' 
	rooms='' 
	parking=''
	provision=''
	wohnungstyp=''
	etage=''
	kaufpreis_stellplatz=''
	baujahr=''
	objektzustand=''
	mieteinnahmen=''
	hausgeld=''
	expose=url2
 
	# TITLE
	try:
		title = soup.find('h1', class_='font-semibold font-xl margin-bottom margin-top-m palm-font-l font-line-s').text
		print(title)
	except:
		pass

	# PRICE
	try:
		price = soup.find('div', class_ ='is24qa-kaufpreis-main is24-value font-semibold is24-preis-value')
		price = price.text
		print(price)
	except:
		pass
	
	# for apartment
	try:
		price = soup.find('div', class_ ='is24qa-kaufpreis-main is24-value font-semibold')
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

	# Address block 
	try:
		addressblock = soup.find('div', class_ = 'address-block').text
		print(addressblock)
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

	# Apartment type - wohnungstyp
	try:
		wohnungstyp = soup.find('dd', class_ = 'is24qa-typ grid-item three-fifths').text
		print("wohnungstyp")
		print(wohnungstyp)
	except:
		pass

	# Floors - etage
	try:
		etage = soup.find('dd', class_ = 'is24qa-etage grid-item three-fifths').text
		print("etage")
		print(etage)
	except:
		pass

	# Parking Space Purchase Price - kaufpreis_stellplatz
	try:
		kaufpreis_stellplatz = soup.find('dd', class_ = 'is24qa-garage-stellplatz-kaufpreis grid-item three-fifths').text
		print("kaufpreis_stellplatz")
		print(kaufpreis_stellplatz)
	except:
		pass

	# Build year - baujahr
	try:
		baujahr = soup.find('dd', class_ = 'is24qa-baujahr grid-item three-fifths').text
		print("baujahr")
		print(baujahr)
	except:
		pass

	# Property condition - Objektzustand
	try:
		objektzustand = soup.find('dd', class_ = 'is24qa-objektzustand grid-item three-fifths').text
		print("objektzustand")
		print(objektzustand)
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
		hausgeld = soup.find('dd', class_ = 'is24qa-hausgeld grid-item three-fifths').text
		hausgeld = hausgeld.split()
		hausgeld = hausgeld[0]
		print("hausgeld=")
		print(hausgeld)
	except:
		pass

	# expose link
	try:
		print('expose=')
		print(expose)
	except:
		pass
	
 
	headers=[
		'title',
		'price', 
		'postcode',
		'addressblock', 
		'livingspace', 
		'rooms', 
		'parking',
		'provision',
		'wohnungstyp',
		'etage',
		'kaufpreis_stellplatz',
		'baujahr',
		'objektzustand',
		'mieteinnahmen',
		'hausgeld',
		'expose']

	# CSV writer
	if export_csv == True:
		try:
			file_exists = os.path.isfile('immo_results.csv')
		
			with open('immo_results.csv', 'a+',newline='') as csvfile:
				writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
				if not file_exists:
					writer.writeheader()
				writer.writerow({'title':title,'price':price, 'postcode':postcode,'addressblock':addressblock,'livingspace':livingspace,'rooms':rooms,'parking':parking,'provision':provision, 'wohnungstyp':wohnungstyp,'etage':etage,'kaufpreis_stellplatz':kaufpreis_stellplatz, 'baujahr':baujahr,'objektzustand':objektzustand,'mieteinnahmen':mieteinnahmen,'hausgeld':hausgeld, 'expose':expose})
		except:
			print('error with csv')
	sleep(1)

	# MySQL writer
	if export_csv == False:

    # Connect to DB
		try:
			conn = mysql.connector.connect(
				user = 'user1',
				passwd = 'password1',
				host = 'localhost',
				port=3306,
				database ='immodb'
			)
			curr = conn.cursor()
			curr.execute("""CREATE TABLE IF NOT EXISTS kaufen (
				id INT AUTO_INCREMENT PRIMARY KEY,
				title VARCHAR(255),
				price VARCHAR(25),
				postcode VARCHAR(255),
				addressblock VARCHAR(255),
				rooms VARCHAR(25),
				parking VARCHAR(255),
				provision VARCHAR(255),
				wohnungstyp VARCHAR(255),
				etage VARCHAR(25),
				kaufpreis_stellplatz VARCHAR(255),
				baujahr VARCHAR(25),
				objektzustand VARCHAR(255),
				mieteinnahmen VARCHAR(255),
				hausgeld VARCHAR(255),
				expose VARCHAR(255),
				posted TIMESTAMP
				)
				""")
		except:
			print("error connecting to DB")

# Main Driver #
if __name__ == '__main__':

	fetch_parent(url)
	
	for i in range (2,67):
		url_nextpage = "https://www.immobilienscout24.de/Suche/radius/wohnung-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&pagenumber={}".format(i)
		fetch_parent(url_nextpage)
