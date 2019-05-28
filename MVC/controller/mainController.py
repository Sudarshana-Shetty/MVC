from flask import Flask, request
from model import dbConn

app = Flask(__name__)

class MainController(object):
# >>>>>> --- Insert user details to DB --- <<<<<<
    def insertUser(self, uDetails):
        if dbConn.db.UserCollections.count({"Name": uDetails['Name']}) == 0:            
            result = dbConn.db.UserCollections.insert_one(uDetails)
            if (result.acknowledged):
                # status = 'Insert Successfull'
                # user = self.displayAllUser()
                user = self.displaySingleUser(uDetails)
                print(user)
                return user
        else:
            return 'Duplicate user'
        
# >>>>>> --- Update the user Address --- <<<<<<
    def updateUser(self, uInput):
        userExist = self.findUser(uInput)
        if userExist:
            dbConn.db.UserCollections.update(
                {
                    'Name': uInput['Name']
                },
                {
                    '$set':{
                        'Address': uInput['Address']
                    }

                }, multi = False
                )
            print('Record updated successfully!!\n', uInput)
            return self.displaySingleUser(uInput)
        else:
            print('User doesnot exist')
            return 'User doesnot exist'        

    # >>>>>> --- Delete User Details --- <<<<<<

    def deleteUser(self, uInput):
        userExist = self.findUser(uInput)
        if userExist:
            dbConn.db.UserCollections.delete_one({
                'Name': uInput['Name']
            })
            print('!!!-----Record Deleted----!!!')
            return self.displayAllUser()
        else: 
            return 'Please enter valid user details to delete'

# >>>>>> --- Display one user details --- <<<<<<
    def displaySingleUser(self, findUser): 
        details = []      
        uCollections = dbConn.db.UserCollections.find({'Name': findUser['Name']}, {'_id':0, 'Name':1, 'Address':1})
        for userColumn in uCollections:
            details.append(userColumn)
        # print(details)
        return details
    
# >>>>>> --- Display all user details --- <<<<<<
    def displayAllUser(self):      
        users = []  
        uCollections = dbConn.db.UserCollections.find({}, {'_id':0, 'Name':1, 'Address':1})
        for allrecord in uCollections:
            users.append(allrecord)            
        # print(users)
        return users
    
# >>>>>> --- Checking for user if exists --- <<<<<<    
    def findUser(self, search):
        if dbConn.db.UserCollections.count({"Name": search['Name']}) == 0:
            return False
        else:
            return True
