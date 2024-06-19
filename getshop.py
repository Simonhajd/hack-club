import requests
from bs4 import BeautifulSoup

def list():
    from keys import API_KEY
    options = requests.get(API_KEY)
    with open('test.html', 'w') as file:
        file.write(options.text)
    soup = BeautifulSoup(options.text, 'html.parser')


    items = soup.find_all(class_='slackey css-ydmcwf')


    tickets = soup.find_all(class_='gaegu css-r6e9ao')


    images = soup.find_all('img', class_='css-hso7i9')


    item_names = [item.get_text() for item in items]
    ticket_values = [ticket.get_text() for ticket in tickets]


    image_urls = [image['src'] for image in images]

    print(item_names)
    print(ticket_values)
    print(image_urls)

    for i in range(len(tickets)):
        print("Name: "+str(item_names[i])+"| Tickets: "+str(tickets[i].get_text())+"| Image URL: "+str(image_urls[i]))

    return item_names, ticket_values, image_urls
list()