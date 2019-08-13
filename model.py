'''
    --- model.py ---
    * Imports db libraries
    * Sets up db connection
    * db will be queried from this file only
'''

class User:
    def __init__(self, id, name):
        self.id = id 
        self.name = name

class Post:
    def __init__(self, id, body, authorId):
        self.id = id 
        self.body = body
        self.authorId = authorId

class Model:
    def __init__(self):
        # setup db ...

    '''
        --- Model Methods ---
    '''
    def GetUsers():
        pass
    def GetUserById():
        pass
    
    def GetPosts():
        pass
    def GetPostsByAuthorId():
        pass
    def GetPostById():
        pass

    def Login(username, password):
        pass




