from user import User
from recommend import recommendSystem # For creating the reccomendation system
class Social_Network:
    def __init__(self, data_name):
        self.__data_name = data_name
        self.__social_nw = {}
        self.__inconsistent = False
        self.__read_data()
        self. __social_nw = {i: self. __social_nw[i] for i in self. __social_nw.keys()}
        self.__recommend_system = recommendSystem(self.__social_nw)

    def get_user(self,name):
        if name in self.__social_nw:
            return self.__social_nw[name]
        return None
    
    def has_user(self,name):
        if name in self.__social_nw:
            return True
        return False

    def is_inconsistent(self):
        return self.__inconsistent

    def __read_data(self):
        # Open and read the file
        r = open(self.__data_name, "r")
        test = r.readline().strip()
        self.number_of_users = int(test)

        line = r.readline().strip()
        while line:
            users = line.split(" ")
            if(len(users)>1):
                # Get the users (assume they are already in the list of users)
                user1 = self.get_user(users[0].strip())
                user2 = self.get_user(users[1].strip())

                # If either user1 or user2 does not exist, create them and add them to the social network
                if user1==None:
                    user1 = User(users[0].strip())
                    self.__social_nw[user1.get_name()]= user1
                if user2==None:
                    user2 = User(users[1].strip())
                    self.__social_nw[user2.get_name()]= user2

                # Add friends
                user1.add_friend(user2)
                user2.add_friend(user1)
            else:
                # If a user has no friends, then they should only be seen once in the data file
                # so an object for this user should idealy not already exist
                if line not in self.__social_nw:
                    user = User(line)
                    self.__social_nw[user.get_name()]= user
                else:
                    # if the user object exists in the social_nw, then this means that the user was mentioned
                    # earlier during reading the file, however users with no friends should only be mentioned once.
                    # This means this network is inconsistent
                    print("The network is inconsistent, try another file")
                    self.__inconsistent = True

            line = r.readline().strip()

    def get_number_of_users(self):
        return self.number_of_users

    def display_users_no_or_least_friends(self):
        friend_count = {}
        for member in self.__social_nw.keys():
            user = self.__social_nw[member]
            if user.get_number_of_friends() in friend_count.keys():
                friend_count[user.get_number_of_friends()].append(user.get_name())
            else:
                friend_count[user.get_number_of_friends()] = [user.get_name()]

        # Print users with least number of friends
        for i in sorted(friend_count.keys()):
            if i!=0:
                members = ", ".join(friend_count[i])
                print(f"The members with least friends is: {members}")
                break

        # Print users with no friends
        if 0 in friend_count.keys():
            members = ", ".join(friend_count[0])
            print(f"The members with 0 friends is: {members}")





    def display_social_network(self):
        for member in self.__social_nw.keys():
            user = self.__social_nw[member]
            friends = []
            for friend in user.get_friends():
                friends.append(friend.get_name())
            connections = ", ".join(friends)
            print(f"{user.get_name()} \t-> {connections}")

    def print_common_friends(self):
        common_friend_dict = self.__recommend_system.get_common_friend_dict()
        for user_name in common_friend_dict:
            print(f"{user_name} \t-> {common_friend_dict[user_name]}")
    
    def get_recommended_friend(self,name):
        return self.__recommend_system.get_recommended_friend(name)
    
    def print_indirect_friends(self,name):
        user = self.__social_nw[name]
        if(user.get_number_of_friends()>0):
            for friend in user.get_friends():
                to_print = f"> {friend.get_name()}"
                indir_friend_names = []
                for indir_friend in friend.get_friends():
                    if(indir_friend.get_name()!=name):
                        indir_friend_names.append(indir_friend.get_name())
                if(len(indir_friend_names)>0):
                    indir_friend_names = ", ".join(indir_friend_names)
                    print(f"{to_print} -> {indir_friend_names}")
                else:
                    print(f"{to_print} -> none")
        else:
            print(f"{name} has no friends")

    





















