class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.inbox = 0
        self.sent = 0

    def print_details(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Inbox:", self.inbox)
        print("Sent:", self.sent)

    def send_email(self, user):
        user.inbox += 1
        self.sent += 1


user1 = User("John", "john@gmail.com")
user2 = User("Jane", "jane@gmail.com")

user1.send_email(user2)

user1.print_details()
user2.print_details()




