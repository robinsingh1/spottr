from BeautifulSoup import BeautifulSoup 
from string import ascii_lowercase
import urllib2
import csv

#read from csv
fileName = 'exercise_links.csv'
thefile = open(fileName, 'r')
links = [line.split(',') for line in thefile.readlines()]

instructions=[]
for i in links:
  current = []
  current.append(i[1].rstrip())
  page = urllib2.urlopen(i[0])
  soup = BeautifulSoup(page)
  lol = soup.find('div',{'class':'guideContent'}).find('ol').findAll('li')
  for l in lol:
    inst = str(l).split('>')[1].split('<')[0].strip()
    current.append(inst)
  instructions.append(current)
  print i[1].rstrip()
  #print current

myfile = open('exercise_instructions.csv','wb')
wr = csv.writer(myfile)
wr.writerows(instructions)
