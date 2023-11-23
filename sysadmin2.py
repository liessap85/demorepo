import subprocess

def add_user_to_group():
    username=input("Enter name of user that you want to add to group: ")
    output=subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Enter a list of groups to which you would like to add the user")
    print("The list should be separated by spaces, for example: \r\n group1 group2 group3")
    print("The available groups are: " + str(output))
    chosenGroups = str(input("Groups : "))

    #Part 2
    output = output.decode().split()
    chosenGroups = chosenGroups.split()
    print("Add to: " + chosenGroups)
    found = True
    groupString = ""

    #Part 3
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print(" Existing Group : " + grp)
                groupString = groupString + grp + ","
            if found == False:
                print(" New Group : " + grp)
                groupString = groupString + grp + ","
            else:
                found = False
            
            #Part 4
            groupString = groupString[:-1]
            confirm=""
            while confirm != "Y" and confirm !="N":
                print("Add user " + username + " to these groups? (Y/N)")
                confirm = input().upper()
                if confirm == "N":
                    print("User " + username + " not added")
                #else confirm == "Y":os.system("sudo usermod -aG " + groupString + username):
                    #print("User " + username = " added")


add_user_to_group()