from re import search
from urllib import response
import requests
search_key=input("Enter search key\n")
search_key=search_key.replace(" ","_")
URL="https://en.wikipedia.org/wiki/Special:Search?search="+search_key
response=requests.request("GET",URL)
file=open("log.txt","a")
response_url=(response.url)
print(response_url)
file.write(response_url+"\n")
file.close()