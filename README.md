# BeautifulSoup
Web Scraping with BS4

#### Noteworthy Code: 
    'set' - need to convert it back to a list
    'urljoin`

#### Conditonal logic with soup.select

    for a in soup.select('a'):
                if 'expose' in a['href']:
                            ls_expose.append(a['href'])
# VPN Rotate
    server=$(cat '/etc/openvpn/privatvpn.conf' | grep remote -m1 | cut -d" " -f2)
    nextserver=$(grep -A1 $server /etc/openvpn/list.txt|grep -v $server)
    
## sed
    sed -i "s!$server!$nextserver2!"
  
 # Proxy Version = immo24de_prx
 update line 22 with trial API key - you will need to sign up with them first
 
     response = client.get(iurl) # this is in place of "requests.get(iurl)
     
 # Get all dropdown values from html     
    from bs4 import BeautifulSoup
    import requests

    my_page = "Wohnung mieten im Umkreis von 50 km von Mannheim - ImmobilienScout24.html"

    soup = BeautifulSoup(open(my_page),"lxml")
    soup = soup.find('div',class_ = "select-input-wrapper")
    items = soup.select('option[value]')
    values = [item.get('value') for item in items]
    textValues = [item.text for item in items]
    print(textValues)
    
<a href="https://github.com/RGGH/BeautifulSoup/edit/MySQL_version/README.md">
  <img src="https://github.com/RGGH/Misc/blob/master/dropdown_127_800w.png" alt="Dropdown Values" style="">
</a> 
 <br>
  ### soup.select('option[value]')
 <br>
<a href="https://github.com/RGGH/BeautifulSoup/edit/MySQL_version/README.md">
<img src="https://github.com/RGGH/Misc/blob/master/get_dropdown_values-result_800w.png" alt="Get the dropdown Values" style="">
</a> 
