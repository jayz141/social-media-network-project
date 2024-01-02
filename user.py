class User:
    def __init__(self,name):
        self.__name = name
        self.__friends = []

    def get_name(self):
        return self.__name

    def get_friends(self):
        return self.__friends    
    
    def get_number_of_friends(self):
        return len(self.__friends)  

    def add_friend(self,friend):
        self.__friends.append(friend)
    
    def display_friends(self):
        for i,friend in enumerate(self.__friends):
            print(f"{i+1}. {friend.get_name()}")

    def has_friend(self, friend):
        for member in self.__friends:
            if(member.get_name()==friend):
                return True
        return False












    