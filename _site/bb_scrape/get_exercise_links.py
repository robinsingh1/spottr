from BeautifulSoup import BeautifulSoup 
from string import ascii_lowercase
import urllib2
import csv


#iterate through alphabet
alphabet = list(ascii_lowercase)
base_url = 'http://www.bodybuilding.com/exercises/list/index/selected/'
#alphabet = ['a']

final=[]

for i in alphabet:
  url = base_url+i
  page = urllib2.urlopen(url)
  soup = BeautifulSoup(page)
  lmao = soup.findAll("div", { "class" : "altExerciseLight" })
  for ii in lmao:
    lol = ii.find('div',{'class':'exerciseName'}).find('a')
    href = str(lol).split('href="')[1].split('"')[0]
    name = str(lol).split('>')[1].split('<')[0].strip()
    final.append([href,name])
    print name

  lmao = soup.findAll("div", { "class" : "altExercise" })
  for ii in lmao:
    lol = ii.find('div',{'class':'exerciseName'}).find('a')
    href = str(lol).split('href="')[1].split('"')[0]
    name = str(lol).split('>')[1].split('<')[0].strip()
    final.append([href,name])
    print name

  #print len(final)
  #print final
  
  myfile = open('exercise_links.csv','wb')
  wr = csv.writer(myfile)
  wr.writerows(final)
  

  #find div id listResults
  #class exerciseName -> h3 -> a href
  #write name+link to txt file
