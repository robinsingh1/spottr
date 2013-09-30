from BeautifulSoup import BeautifulSoup 
from string import ascii_lowercase
import urllib2
import csv

#read from csv
fileName = 'exercise_links.csv'
thefile = open(fileName, 'r')
links = [line.split(',') for line in thefile.readlines()]

#get data
#links=[["http://www.bodybuilding.com/exercises/detail/view/name/alternate-leg-diagonal-bound",""]]
data=[]
for url in links:
  current=[]
  page = urllib2.urlopen(url[0])
  soup = BeautifulSoup(page)
  try:
    lol=soup.find('div',{"id":"exerciseDetails"}).findAll('p')[1]
  except:
    lol=soup.find('div',{"id":"exerciseDetails"}).findAll('p')[0]
  
    
  lol = str(lol).replace("\n","").split('<br />')
  try:
    lol.pop(-2)
    lol.pop()
  except:
    nopop=True
  lol = [x.replace(' ','') for x in lol]
  lol = [x.split(':<') for x in lol]
  for i in lol:
    #print i[0]
    if i[0] == 'OtherMuscles':
      test = ""
      for ii in i[1].split(','):
        test = test+" "+ii.split('>')[1].split('<')[0].strip()
      #print "OtherMuscles" + " " + test
      try:
        current[2] = test
      except:
        print "ERROR " + url[1].rstrip()
    else:
      lol = i[1].split('>')[1].split('<')[0].strip()
      current.append(lol)
      if i[0] == 'MainMuscleWorked':
        current.append(0)
  #print url[0] + " " +''.join(current)
  #print url[0]
  #print current
  print url[1].rstrip()
  data.append(current)
  #print current

  
  #print lmao
  #for l in lol:
  #  name = str(l).split('>')[1].split('<')[0].strip()
  #  current.append(name)
  #print i[1]
  #data.append(current)

myfile = open('exercise_data.csv','wb')
wr = csv.writer(myfile)
wr.writerows(data)
