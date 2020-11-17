# BeautifulSoup
Web Scraping with BS4

#### Noteworthy Code: 
'set' - need to convert it back to a list <br>
'urljoin'

#### Conditonal logic with soup.select

for a in soup.select('a'):<br>
            if 'expose' in a['href']:<br>
            	ls_expose.append(a['href'])<br>
