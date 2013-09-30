from BeautifulSoup import BeautifulSoup 
from string import ascii_lowercase
import urllib2
import csv

#read from csv
fileName = 'exercise_links.csv'
thefile = open(fileName, 'r')
links = [line.split(',') for line in thefile.readlines()]

imgs=[]
count = 0
for i in links:
  current = []
  current.append(i[1].rstrip())
  page = urllib2.urlopen(i[0])
  soup = BeautifulSoup(page)
  lol = soup.find('div',{'class':'exercisePhotos'}).findAll('img')
  for l in lol:
    try:
      src = str(l).split('src="')[1].split('"')[0]
    except:
      print l
      break
      break
    if 'jpg' in src:
      current.append(src)
  lol = soup.find('div',{'class':'guideImage'}).find('img')
  guideImage= str(lol).split('src="')[1].split('"')[0]
  current.append(guideImage)
  imgs.append(current)
  print i[1].rstrip()
  #print imgs

myfile = open('exercise_images.csv','wb')
wr = csv.writer(myfile)
wr.writerows(imgs)
