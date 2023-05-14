from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur

# Getting input for webiste from user
url_input = input("https://www.shiseido.com.vn/vi/axe_suncare/")
print(" This is the website link that you entered", url_input)


# For extracting specific tags from webpage
def getTags(tag):
  s = ur.urlopen(url_input)
  soup = BeautifulSoup(s.read())
  return soup.findAll(tag)

# For extracting all h1-h6 heading tags from webpage
def headingTags(headingtags):
  h = ur.urlopen(url_input)
  soup = BeautifulSoup(h.read())
  print("List of headings from headingtags function h1, h2, h3, h4, h5, h6 :")
  for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    print(heading.name + ' ' + heading.text.strip())

# For extracting specific title & meta description from webpage
def titleandmetaTags():
    s = ur.urlopen('https://www.shiseido.com.vn/vi/axe_suncare/')
    soup = BeautifulSoup(s.read())
    #----- Extracting Title from website ------#
    title = soup.title.string
    print ('Website Title is :', title)
    #-----  Extracting Meta description from website ------#
    meta_description = soup.find_all('meta')
    for tag in meta_description:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            #print ('NAME    :',tag.attrs['name'].lower())
            print ('CONTENT :',tag.attrs['content'])



#------------- Main ---------------#
if __name__ == '__main__':
  titleandmetaTags()
  tags = getTags('p')
  headtags = headingTags('h1')
  for tag in tags:
     print(" Here are the tags from getTags function:", tag.contents)