# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

table_rows = soup.findAll("tr")

state_high_test = ""
state_low_test = ""
high_test_ratio = 0.0
low_test_ratio = 100.0

state_high_death = ''
state_low_death = ''
death_high_ratio = 0.0
death_low_ratio = 100.0

for row in table_rows[2:52]:
    td = row.findAll("td")
    state = td[1].text

    total_cases = int(td[2].text.replace(',',''))
    total_death = int(td[4].text.replace(',',''))
    total_tests = int(td[10].text.replace(',',''))
    popul = int(td[12].text.replace(',',''))

    death_rate = round(((total_death / total_cases) * 100),2)
    test_rate = round(((total_tests / popul) * 100),2)

    if death_rate < death_low_ratio:
        state_low_death = state
        death_low_ratio = death_rate

    if death_rate > death_high_ratio:
        state_high_death = state
        death_high_ratio = death_rate

    if test_rate < low_test_ratio:
        state_low_test = state
        low_test_ratio = test_rate

    if test_rate > low_test_ratio:
        state_high_test = state
        high_test_ratio = test_rate

print(f'{state_high_death}has the highest death rate.' )
print(f'High death rate: {round(death_high_ratio, 2)}%')
print()
print(f'{state_low_death}has the lowest death rate.')
print(f'Low death rate: {round(death_low_ratio, 2)}%')
print()
print(f'{state_high_test}has the highest test rate.')    
print(f'High test rate: {round(high_test_ratio, 2)}%')   
print() 
print(f'{state_low_test}has the lowest test rate.')
print(f'Low test rate: {round(low_test_ratio, 2)}%')
print()



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

