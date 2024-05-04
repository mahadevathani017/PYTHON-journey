import requests
from bs4 import BeautifulSoup
# Send an HTTP GET request to the webpage
url = 'https://en.wikipedia.org/wiki/Sachin_Tendulkar'
response = requests.get(url)
# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the image tags and extract the 'src' attribute
image_links = [img['src'] for img in soup.find_all('img')]
# Display the image links
for link in image_links:
    print(link)
