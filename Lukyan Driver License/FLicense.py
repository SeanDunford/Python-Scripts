import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
    print 'Please enter driver license as argument'
else:
    url = 'https://services.flhsmv.gov/DLCheck/HomeView.aspx'
    html = requests.get(url)

    soup = BeautifulSoup(html.text)
    hidden = soup.find_all('input', type='hidden')
    license = sys.argv[1]

    post_data = {
        '__VIEWSTATE' : hidden[0]['value'],
        '__EVENTVALIDATION' : hidden[1]['value'],
        'ctl00$MainContent$txtDLNumber' : license,
        'ctl00$MainContent$btnEnter' : 'Enter'
    }

    result = requests.post(url, post_data)
    print result.text
    finalResults = result.text.decode('utf-8-sig')
    file = open('results.html', 'w')
    file.write(finalResults)
    file.close()
    
