# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import requests
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

url = "https://www.immobilienscout24.de/Suche/radius/haus-kaufen?centerofsearchaddress=Mannheim;;;1276001025;Baden-W%C3%BCrttemberg;&geocoordinates=49.50057;8.50248;50.0&enteredFrom=one_step_search"

headers = {
    'User-Agent': 'Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
}
params = dict(
	Accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	referer = "https://www.immobilienscout24.de/",
	Control = "max-age=0",
	Connection="keep-alive",
	Cookie = "seastate=\"TGFzdFNlYXJjaA==:ZmFsc2UsMTYwNTUzOTc1MDI2NywvZGUvbmllZGVyc2FjaHNlbi93b2xmc2J1cmcvd29obnVuZy1taWV0ZW4=\"; feature_ab_tests=\"IF311@2=NEW|XTypeSearch@3=Default\"; ABNTEST=1605538429; is24_experiment_visitor_id=04922a4d-3393-4333-95c7-68ec64d492fa; AWSALB=7ZOh1vSgI0DvIBai63sj4d0mSocpCNaihzskjOT+OtPtO3VgElnXzkXDnyopXOJh69sg1CXTzJFTmWE+42Mb4VSVF9hZtY5cQS2vlB6v+NrfU9EVh1jHLQ8aLLGQ; AWSALBCORS=7ZOh1vSgI0DvIBai63sj4d0mSocpCNaihzskjOT+OtPtO3VgElnXzkXDnyopXOJh69sg1CXTzJFTmWE+42Mb4VSVF9hZtY5cQS2vlB6v+NrfU9EVh1jHLQ8aLLGQ; IS24VisitIdSC=sidd9deffd1-89b7-4a0b-936f-4f0f3aee8906; IS24VisitId=vid7bacbb5b-4696-4651-abf8-0c157a9f5258; websessionid=1DDF645E74C35CE7D4422AB7709C6B7D; longUnreliableState=\"dWlkcg==:YS05MmExYTQ0MDFkNWM0NzRlYTU0MDcxMzNlM2ZmNTc1OA==\"; reese84=3:y2ZoLMDtCuZREolU5p+2tg==:BhHE6xotXvvvEfM6r/CbLKUFnt62QbgbeiR92HxCHAmjz5QItN3J7VhIRDGdRANwlgvnvOzn9U4Pu1NhArAd5OTbNuErm4Kecf17lE79VqdiiU1mKn7kzDv8Qg1OQMb3Y2K5gidzU9HLNQtQXgzwWZG4dMmGttitfc+fMvja1J4nf8S55nDpfBL6V7UbEYwEY2fwk4HDgTNgypWByKoe963PYdrf1wagams8V+sjb3kdD3iwotxr+7GcM3RNiIbgtcKhIHqap+aPKTHAww8it/ZvsZEgtTAbUEwQDLk38EutzOI2ynTC7QC4A7ZXR4QdBbYnaDGRXqZO+YXyvc+WyA67rdytJ4er/c21idZSBhvh+iY2HKKzJ4eMtWxywc5zYnvzzADmLvEL690Em8U5agzDukvA8bmj/MSqMBckBv676H6OEnLt9slr2iV/GrpFmGU2U+CvhcRHcmS35dblVEjQM79FPbZemHM34UpMtC7szZVcOrfXWc55x54l4SFT:biqK+15qdYBlN4Urry5FjWtMcfKQTgYCv0rRntzZC+Q=",
	TE="Trailers",
	Host="www.immobilienscout24.de",
	)

response = requests.get(url, headers=headers)
# get 20 expose links from page
soup = BeautifulSoup(response.content, features="lxml")

ls_expose = []

for a in soup.select('a'):
            if 'expose' in a['href']:
            	ls_expose.append(a['href'])
             
ls_expose = (set(ls_expose)) 

relative_link = list(ls_expose)[0]
url = urljoin('https://www.immobilienscout24.de/', relative_link)

print(url)
