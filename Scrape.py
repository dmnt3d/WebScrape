from bs4 import BeautifulSoup
#import urllib
import requests

BLOG  =  'http://blogs.vmware.com/vcloud'
#url =  urllib.urlopen('http://blogs.vmware.com/vcloud')
r = requests.get(BLOG)
data = r.text
soup = BeautifulSoup(data)

soup

print ("soup")




#test edit
