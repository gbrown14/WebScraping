
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'
page = urlopen(webpage)			
soup = BeautifulSoup(page, 'html.parser')
title = soup.title

#print(title.text)
#
movie_rows = soup.findAll('tr')

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    ranking = td[0].text
    movie_name = td[1].text
    theater = int(td[6].text.replace(",",""))
    gross = int(td[7].text.replace(",","").replace("$",""))
    dis = td[8].text

    avg = gross / theater

    print(f'Rank: {ranking}')
    print(f'Name: {movie_name}')
    print(f'Total Gross: ${gross :,.2f}')
    print(f'Distributor: {dis}')
    print(f'Average per Theater: {avg :,.2f}')
    print()
    print()


