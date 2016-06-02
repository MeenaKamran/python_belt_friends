"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        
        self.load_model('Friend')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """

        friends = self.models['Friend'].get_friends(session['id'])
        non_friends = self.models['Friend'].get_non_friends(session['id'])
        return self.load_view('friends.html', friends=friends, non_friends=non_friends)

    def add(self, friend_id):

        data_info = {
                    'user_id': session['id'],
                    'friend_id': friend_id
                    }
        self.models['Friend'].add_friend(data_info)
        return redirect('/friends')

    def remove(self, friend_id):

        print "in remove"
        data_info = {
                    'user_id': session['id'],
                    'friend_id': friend_id
                    }
        self.models['Friend'].remove_friend(data_info)
        return redirect('/friends')

