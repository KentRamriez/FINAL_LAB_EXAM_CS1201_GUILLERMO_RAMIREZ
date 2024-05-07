# load score  txt file
# save score
# play_game
# show_top_score
# load_user create txt file
# save_user write and save text file

class User_Manager():
    def __init__(self):
        self.user_file = 'users.txt'
        self.users = self.load_user()

    def load_user():
        users = {}

        with open('users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(" , ")
                users[username] = password
        return users

    def save_users(self, username, password):
        with open(self.user_file, "a") as file:
            file.write(f"{username}, {password}\n")
        self.users[username] = password

    def validate_username(self, username):
        return len(username) >= 4

    def validate_password(self, password):
        return len(password) >= 8

    def register(self, username, password):
        while True:
                while True:
                    username = str(input("Enter a username (Minimum of 4 characters.) (Leave blank to go back): ")).strip()
                    if not username:
                        return
                    elif self.validate_username(username):
                         break
                    else:
                        print("Username must have atleast 4 characters.")
                while True:
                    password = str(input("Enter a password (Minimum of 8 characters.) (Leave blank to go back): ")).strip()
                    if not password:
                        return
                    elif self.validate_password(password):
                         break
                    else:
                        print("Password must have atleast 8 characters.")

                if username not in self.user:
                    self.save_users(username, password)
                    print("Registration successful!")
                elif self.validate_username(username) and self.validate_password(password):
                    if not username:
                        pass
                    elif username not in self.users:
                        self.save_users(username, password)
                        print("Register Successful.")
                    else:
                        print("Username already exists.")
                else:
                    print("Invalid username or password. Try again!")

    def login():
        pass

    register()