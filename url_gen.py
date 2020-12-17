              _                 _                                            _    
#  _ __ ___  __| | __ _ _ __   __| | __ _ _ __ ___  ___ _ __    ___ ___  _   _| | __
# | '__/ _ \/ _` |/ _` | '_ \ / _` |/ _` | '__/ _ \/ _ \ '_ \  / __/ _ \| | | | |/ /
# | | |  __/ (_| | (_| | | | | (_| | (_| | | |  __/  __/ | | || (_| (_) | |_| |   < 
# |_|  \___|\__,_|\__,_|_| |_|\__,_|\__, |_|  \___|\___|_| |_(_)___\___(_)__,_|_|\_\
#                                   |___/                                           



# code to generate urls with page numbers for scraper

'''url = https://www.immobilienscout24.de/Suche/radius/haus-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&pagenumber=82'''

base_url = "https://www.immobilienscout24.de/Suche/radius/haus-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&pagenumber="

page_range = 83


url_list = []
for i in range(page_range+1):
	
	url_list.append(base_url + str(i) +"\n")

print (url_list)	

with open ("txf.txt","a") as f:
	f.write("".join(url_list))
