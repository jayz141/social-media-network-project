class recommendSystem:
    def __init__(self,users):
        self.__social_nw = users
        self.__common_friends = {}
        self.__members = list(self.__social_nw.keys())
        self.__gather_common_friends()
    
    def __gather_common_friends(self):
        for i in self.__members:
            user_1 = self.__social_nw[i]
            commonlist = []
            for j in self.__members:
                user_2 = self.__social_nw[j]
                # If user has no friends in the social network as we discount members being friends with themselves
                if(user_2.get_name()==user_1.get_name() and len(user_1.get_friends())==0):
                    common_count = 1
                else:
                    common_count = self.get_common_friends(user_1,user_2)
                commonlist.append(common_count)
            self.__common_friends[user_1.get_name()] = commonlist
    
    def get_recommended_friend(self,user_name):
        common_friends = self.__common_friends[user_name]
        best_recommended = None
        max_common_count = 0
        for i,common_count in enumerate(common_friends):
            friend = self.__social_nw[self.__members[i]]
            condition1 = (common_count>max_common_count)
            condition2 = (friend.get_name()!=user_name)
            condition3 = (friend.has_friend(user_name)==False)
            if condition1 and condition2 and condition3:
                best_recommended = friend
                max_common_count = common_count
        return best_recommended


    def get_common_friend_dict(self):
        return self.__common_friends

    def get_common_friends(self, user1,user2):
        common_count = 0
        for friend in user1.get_friends():
            if user2.has_friend(friend.get_name()):
                common_count+=1
        return common_count

        