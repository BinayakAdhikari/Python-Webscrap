from bs4 import BeautifulSoup
from urllib.request import urlopen

#Requesting from Web
html=urlopen("https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=Graphic+Card&N=-1&isNodeId=1")


soup=BeautifulSoup(html.read(),"html.parser")         #Using Beautiful Soup and Reading all html elements


container=soup.find_all("div",{"class":"item-container  "})  #scaping class named => item-container

print(len(container))          #total length of items