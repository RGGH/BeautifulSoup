# BeautifulSoup
Web Scraping with BS4

#### Noteworthy Code: 
'set' - need to convert it back to a list
'urljoin'

#### Conditonal logic with soup.select

for a in soup.select('a'):
            if 'expose' in a['href']:
            	ls_expose.append(a['href'])
