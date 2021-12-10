from flask_app.config.mysqlconnection import connectToMySQL


class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.sender = data['sender']
        self.receiver_id = data['receiver_id']
        self.receiver = data['receiver']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages ( message , sender_id , receiver_id, created_at, updated_at ) VALUES ( %(message)s , %(sender_id)s , %(receiver_id)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('private_wall').query_db(query, data)

    @classmethod
    def get_my_messages(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('private_wall').query_db(query, data)
        # Create an empty list to append our instances of friends
        messages = []
        # Iterate over the db results and create instances of friends with cls.
        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('private_wall').query_db(query, data)
