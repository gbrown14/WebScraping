from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client

#Twilio keys
import keys2


#Website 
url = 'https://crypto.com/price'
#fortune favors the brave -matt damon

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers= headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tr = soup.findAll('tr')

counter = 0

#Scrape loop
for row in tr[1:6]:
    td = row.findAll("td")
    names = soup.findAll("p", attrs={"class":"chakra-text css-rkws3"})
    symbols = soup.findAll("span", attrs={"class":"chakra-text css-1jj7b1a"})
    prices = soup.findAll("div", attrs={"class":"css-b1ilzc"})
    curr_name = names[counter].text
    curr_symbol= symbols[counter].text
    curr_price = float(prices[counter].text.replace(",","").replace("$",""))
    curr_change=float(td[4].text.replace("%",""))
    corresponding_price = ((100-(curr_change))/100) * (curr_price)
    
    counter+=1

#Outputs

    print(f'Currency Name: {curr_name}')
    print(f'Symbol: {curr_symbol}')
    print(f"Current Price: ${curr_price:,.2f}")
    print(f"% change last 24 hours: {curr_change}%")
    print(f'Corresponding Price: ${corresponding_price:,.2f}')
    print()
    input()

#Text messages and conditions

    client = Client(keys2.accountSID, keys2.authToken)
    TwilioNumber = '+12232176237'
    CellPhone = '+17602747675'

    BTC = 'The value of Bitcoin (BTC) has fallen below $40,000.'
    ETH = 'The value of Ethereum (ETH) has fallen below $3,000.'

    if curr_symbol == 'BTC' and float(curr_price) < 40000:
        text = client.messages.create(to = CellPhone, from_ = TwilioNumber, body = BTC)

    if curr_symbol == 'ETH' and float(curr_price) < 3000:
        text = client.messages.create(to = CellPhone, from_ = TwilioNumber, body = ETH)

    print(text.status)