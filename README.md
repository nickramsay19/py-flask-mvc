# py-flask-mvc - An MVC showcase in flask
> Created by Nicholas Ramsay

## Model
'''python

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
'''

## View
The views will be stored in the `templates/` folder like normal in flask.

## Controller
Like the view, flask will handle the controller like normal.