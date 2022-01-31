## Imports
from re import search
from urllib import response
import requests

## setting the URL 
search_key=input("Enter search key\n")
search_key=search_key.replace(" ","_")
URL="https://en.wikipedia.org/wiki/Special:Search?search="+search_key


## Gettings response url 
response=requests.request("GET",URL)
response_url=(response.url)

## writing to a log file
file=open("log.txt","a")
print(response_url)
file.write(response_url+"\n")
file.close()