""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()

    def get_friends(self, user_id):
        query = "SELECT users.alias, users.id FROM users LEFT JOIN friends ON users.id=friends.user_id LEFT JOIN users as friend ON friend.id=friends.friend_id WHERE friends.friend_id=:user_id"
        data = {'user_id': user_id}
        friends = self.db.query_db(query, data)
        return friends

    def get_non_friends(self, user_id):

        query = "SELECT users.alias, users.id FROM users WHERE users.id !=:user_id AND users.id NOT IN (SELECT users.id FROM users JOIN friends ON friends.user_id=users.id JOIN users as friend ON friend.id=friends.friend_id WHERE friends.friend_id=:user_id)"
        # query = "SELECT users.alias, users.id FROM users JOIN friends ON users.id=friends.user_id JOIN users as user2 ON user2.id=friends.friend_id WHERE user.id NOT IN (SELECT users.id FROM users JOIN friends ON users.id=friends.user_id JOIN users as friend ON friend.id=friends.friend_id WHERE users.id=:user_id)"
        data = {'user_id': user_id} 
        non_friends = self.db.query_db(query, data)
        return non_friends

    def add_friend(self, data):

        query = "INSERT into friends (user_id, friend_id) VALUES (:user_id, :friend_id)"
        data = {'user_id': data['user_id'], 'friend_id': data['friend_id']}
        # self.db.query_db(query, data)
        # query = "INSERT into friends (user_id, friend_id) VALUES (:friend_id, :user_id)"
        return self.db.query_db(query, data)

    def remove_friend(self, data):

        query = "DELETE FROM friends WHERE user_id=:friend_id AND friend_id=:user_id"
        data = {'friend_id': data['friend_id'], 'user_id': data['user_id']}
        return self.db.query_db(query, data)


