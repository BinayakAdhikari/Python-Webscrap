from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlReq
scrap_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=Graphic+Card&N=-1&isNodeId=1'
urlClient = urlReq(scrap_url)                             #Requesting from Web
html=urlClient.read()
urlClient.close()
page=soup(html,"html.parser")                             #Using Beautiful Soup and Reading all html elements
containers=page.findAll("div",{"class":"item-container"})  #scraping class named => item-container
#Now Container contains all the elememts of the class item-container
#use for loop to get individual element seperately
print(containers)
print(len(containers))                                     #total length of items
