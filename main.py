from pathlib import Path #Used for handling files
from social_network import Social_Network # For building the social network

def prompt_member_name(network):
    selectedUserName = input(f"Enter a member name: ")

    if(network.has_user(selectedUserName)):
        return selectedUserName
    else:
        print("Member does not exist")
        return None


def feature1(network):
    display = input("Display the social network (any key or n)? ")
    if display.lower() == "n":
        return
    network.display_social_network()
    print("\nCommon friends")
    network.print_common_friends()

def feature2(network):
    display = input("Do you want to recommend a friend to a member (any key or n)? ")
    if(display.lower()=="n"): 
        return
    while True:
        selectedUserName = prompt_member_name(network)
        if(selectedUserName!=None):
            recommendedFriend = network.get_recommended_friend(selectedUserName)
            if(recommendedFriend==None):
                print(f"The recommended friend for {selectedUserName} is None")
            else:
                print(f"The recommended friend for {selectedUserName} is {recommendedFriend.get_name()}")

        repeat = input("Do you want to recommend friends to another member (any key or n)? ")
        if(repeat.lower()=="n"):
            break

def feature3(network):
    display = input("Display how many friends a member has (any key or n)? ")
    if(display.lower()!="n"):   
        selectedUserName = prompt_member_name(network)
        if(selectedUserName!=None):
            user = network.get_user(selectedUserName)
            print(f"{selectedUserName} has {user.get_number_of_friends()} number of friends")
    
    display = input("Show the number of the least number of friends or no friends at all (any key or n)? ")
    if(display.lower()!="n"): 
        network.display_users_no_or_least_friends()

    
    display = input("Show friends of a member (any key or n)? ")
    if(display.lower()!="n"): 
        selectedUserName = prompt_member_name(network)
        if(selectedUserName!=None):
            user = network.get_user(selectedUserName)
            if(user.get_number_of_friends()>0):
                print(f"{selectedUserName} is friends with:")
                user.display_friends()
            else:
                print(f"{selectedUserName} has no friends")


    display = input("Display the friends of the friends of a given member (any key or n)? ")
    if(display.lower()!="n"): 
        selectedUserName = prompt_member_name(network)
        if(selectedUserName!=None):
            network.print_indirect_friends(selectedUserName)
    


if __name__ == "__main__":
    while(True):
        # Ask the user to enter a file name
        file_name = input("Please Enter a File Name :\n")

        # If the user enters the letter 'n' the code ends
        if(file_name.lower()== 'n'):
            break
        path = Path(file_name)
        # Check if the file exists
        if(file_name.strip()!="" and path.exists()):
            network = Social_Network(file_name)
            feature1(network)
            if(network.is_inconsistent()==False):
                feature2(network)
                feature3(network)
        else:
            # An error message is shown in case of the file does note exist
            print("Error: File does not exist")

        repeat = input("Do you want to try another social network (any key or n)")
        if(repeat=="n"):
            break


