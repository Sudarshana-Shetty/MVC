from flask import Flask, request
from model import dbConn

app = Flask(__name__)

class MainController(object):

    def insertUser(self, uDetails):
        if dbConn.db.UserCollections.count({"Name": uDetails['Name']}) == 0:            
            result = dbConn.db.UserCollections.insert_one(uDetails)
            if (result.acknowledged):
                # status = 'Insert Successfull'
                user = self.displayAllUser()
                # user = self.displayAllUser()
                # print(user)
                return user
        else:
            return 'Duplicate user'

    def displaySingleUser(self, findUser):        
        uCollections = dbConn.db.UserCollections.find({'Name': findUser['Name']})
        print(uCollections)
        # for userColumn in uCollections:
        #     details = userColumn
        return uCollections

    def displayAllUser(self):      
        users = []  
        uCollections = dbConn.db.UserCollections.find({}, {'_id':0, 'Name':1, 'Address':1})
        for allrecord in uCollections:
            users.append(allrecord)            
        return users
