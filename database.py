import json
class mydatabase:

    def add(self,name,email,password):
        with open('db.json','r') as d:
            database=json.load(d)
        with open('db.json','w') as d:
            database[email]={'name':name,'password':password}
            json.dump(database,d)
        with open('db.json', 'r') as d:
            database = json.load(d)

    def check(self,email):
        with open('db.json','r') as cd:
            db=json.load(cd)
            if email in db:
                return 1
            else :
                return 0
    def check2(self,email,password):
        with open('db.json','r') as cd:
            db=json.load(cd)
            if email in db:
                if password==db[email]['password']:
                    return 1
                else:
                    return 0
            else :
                return 0


