import json 
import random

# fileName = "hello.db"
# Default argument dena ek acchi coding practice hai.
# Isse agar user koi argument nahi bhi de, toh bhi code sahi chalega
def load(fileName='hello.db',autodumping = False):
    '''```
    Yeh ek fileName leta hai, jiska content yeh load karta hai
    By default yeh hello.json file ko load karta hai
    Content load kar ne ke liye, yeh ek MeraDB class ka object
    create karta hai. Ussi object ko yeh return kar deta hai
    jisse ki hum uss object par set, get, aur dump jaise
    functions call kar sakein.
    ```'''
    meraDB = MeraDB(fileName,autodumping)
    meraDB.load_file()
    return meraDB

class MeraDB():
    '''```
    Yeh main class hai, jaha saara magic hoga!

    Humne yeh class isliye banayi jisse ki hum meradb object bana kar
    uss par koi bhi functions call kar sake

    Jaise list_a = [1,2,4] kar kar aap list_a naam ki list create karte ho
    Phir aap list_a object par functions call kar sakte ho, jaise
    list_a.append(another_list), list_a.pop()

    aise hi jab aap meradb ka object declare karoge, toh class use karne ke
    vajah se, hum meradb object par functions call kar payenge, jaise:

    mdb = MeraDB("dbfile.json")
    mdb.load_file()
    mdb.dump()
    
    class ke ander variable ko property bolte hai aur function ko method.

    ```'''
    fileName = ""
    jObject = {}
    autodumping  = False
    def __init__(self, fileName,autodumping):
        self.fileName = fileName
        self.autodumping = autodumping
    def load_file(self): 
        try:
            files= open(self.fileName, 'r+')
        except:
            files= open(self.fileName, 'w+') 
            content= files.read()
        if True :
            content= json.dumps({})
            self.jObject= json.loads(content)
        print ("loading success")
        return self.jObject
    def dump(self):
        '''```
        Iss function ko use kar kar, aap content ko dump kar satke hai
        ```'''
        print "Dumping database to ", self.fileName, " !"
        
        open(self.fileName, 'w+').write(json.dumps(self.jObject))
        '''```
        You can also write the above line as:
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        ```'''

        print "DB dumped successfully!"
        return "OK"
    def set(self, key, value):
        self.jObject[key]=value    
        return True
    def get(self, key1):
        if True:
            print (self.jObject[key1])
            return self.jObject[key1]
    def get_all(self):
        list=[]
        for keys in self.jObject:
            list.append(keys)
            if list ==[]:
                print ("no key in the Database.") 
                return "ok" 
            print (list) 
            return "ok"
    # def dump(self):
    #     file1=open(self.filename, "w")
    #     data=json.dumps(self.jobject)
    #     file1.write(data)
        return self.jobject
    def rem(self):
        if 'key' in self.jObject:
            del self.jObject['key']
        else:
            print 'ok'
    def exists(self):
        if "key" in self.jObject:
            print True
        else:
            print False
    def total_keys(self):
        counter = 0
        if "key" in self.jObject:
            counter = counter + 1
        else:
            print "none"
        print counter
    def del_db(self):
        if "key" in self.jObject:
            del self.jObject['key']
        if "value" in self.jObject:
            del self.jObject['value']
        else:
            print "none"
    def random_insert(self,number):
        i = 0
        while(i<number):
            key = random.randint(0,100)
            value = random.randint(0,100)
            self.jObject[key] = value
            i = i + 1
        return self.jObject
    def dmerge(self,fileName):
        open_file= open(fileName,"r+")     
        data= open_file.read()
        self.jObject= json.loads(data)
        self.dump()
        return True
        second = MeraDB(fileName,True)
        self.jObject=second.load_file()
    
