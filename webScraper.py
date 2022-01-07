import requests
from requests_html import HTMLSession
 
def getQuote():
    url = "http://wisdomofchopra.com/iframe.php#"
    try:
        session = HTMLSession()
        response = session.get(url)
    except requests.exceptions.RequestException as e:
        print(e)

    quoteHTML = response.html.find('#quote')[0].text
    quote = quoteHTML.split("\"")
    return quote[1]
