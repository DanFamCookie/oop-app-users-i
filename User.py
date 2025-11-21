# your User class goes here
class User: 
    all_users= []
    def __init__(self, name , email_address, driver_licence_number):
        self.email = email_address
        self.driver_licence_number = driver_licence_number
        self.name = name
        self.posts = []


    @classmethod
    def register_user(cls):
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")
        user_license = input("Enter your license num: ")

        # Check if user already exists (by name)
        if any(user.name == user_name for user in cls.all_users):
            print("Username not available.")
            return None # Return nothing if registration fails

        # Create a new User instance
        new_user = cls(user_name, user_email, user_license)
        # Add the new instance to the class list
        cls.all_users.append(new_user)
        print(f"User '{user_name}' added.")
        return new_user # Return the newly created User object
    
    # 1. Add a method to create a new user post
    def create_post(self, post_content):
        self.posts.append(post_content)
        print(f"Post created by {self.name}: '{post_content[:30]}...'")
        
        # 4. Make sure information stays in sync (it is, since 'all_users' holds 
        # a reference to 'self', so modifying self.posts updates the object in the list)





# --- TESTING THE CLASS ---

# Register the first user
user1 = User.register_user()

# Register a second user
user2 = User.register_user() 

# Test posting (Step 1)
if user1:
    user1.create_post("Hello world! This is my first app post.")
    user1.create_post("A second post about my pet.")

# Verify data synchronization (Step 4)
# Print the posts list for the user object stored in the class's all_users list
print("\n--- Verification ---")
if User.all_users:
    # Check the data stored in the first user in the global list
    first_registered_user = User.all_users[0]
    print(f"Name in all_users list: {first_registered_user.name}")
    print(f"Posts in all_users list: {first_registered_user.posts}")












# peach = User("peach@nintendo.com", "DTF987654")
# # Mario = User("mariorules@nintendo.com", "DTF963852")
# # Peach.new_user()
# peach.show_licence_number()
# # Mario.new_user()
# Mario.show_licence_number("DTF963852")






    # def new_user(self):
    #     print(f"Hello {self.name}")

    # def show_licence_number(self):
    #     print(f"Here is your Dirver Licence Number: {self.driver_licence_number}")

    # def NewUserPost():