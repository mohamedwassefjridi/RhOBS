from pymongo import MongoClient
from pprint import pprint

client = MongoClient('15.236.51.148', username='rhobs', password='xeiPhie3Ip8IefooLeed0Up6',
authSource='rhobs',
authMechanism='SCRAM-SHA-1')

collection=client.rhobs.get_collection("test")

    
### 0

Musics={}
for person in collection.find({},{'_id':0}):
    for music in list(person.values())[0]["music"]:
        if music in Musics:
            Musics[music]+=1
        else:
            Musics[music]=1
            
pprint(Musics)          
            

    
                
### 1
from datetime import datetime
  
def calculateAge(birthDate):
    birthDate=datetime.strptime(birthDate,"%Y-%m-%d")
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
  
    return age


Ages={}
for per in collection.find({},{'_id':0}):
    for person in list(per.values()):

        for music in person["music"]:
            if music not in Ages:
                Ages[music] = calculateAge(person["birthdate"])
            if music in Ages:
                Ages[music] += calculateAge(person["birthdate"])
                
for music in Ages:
    Ages[music]/=Musics[music]
    
pprint(Ages)

### 2

#def agePyramid(city, size):
size=4
city='Blin'
Age=[]
for per in collection.find({},{'_id':0}):
    if list(per.values())[0]["city"]==city:
        Age.append(calculateAge(list(per.values())[0]["birthdate"]))

Slices=list(range(min(Age),max(Age),size))+[max(Age)]
frag=[(Slices[i],Slices[i+1]) for i in range(len(Slices)-1)]
pyramid={}
for i in Age:
    k=1
    while i>Slices[k]:
        k+=1

    if k not in pyramid:
        pyramid[k]=1
    else:
        pyramid[k]+=1
        
Pyramideee={
    frag[i-1]:pyramid[i] for i in pyramid
}
pprint(Pyramideee)