
####### OPENING & READING (REMOVE THE COMENT TO RUN THIS BLOCK PROGRAM)
# myfile = open("/home/aandaldi/Documents/TrainInternal/learn-Python3/test/Routers.txt", "r")     #"r" default acces mode
#
# myfile.mode                 #to check access mode of file
# myfile.read()               #to read all pointer and posision on the last
# myfile.seek(0)              #to set pointer posision on the beginning
# myfile.tell()               #to call the poiter posision
# myfile.read(4)              #to read 4 character from pointer posision
#
# myfile.seek(0)
# myfile.readline()           #to read line from pointer posisition (if you see '' the meaning of the end of line/character)
# myfile.readlines()          #to see the all of lines on list
#
#
# myfile.seek(0)
# for line in myfile.readlines():
#     if line.startswith("A"):
#         print(line)




####### WRITING & APPENDING (REMOVE THE COMENT TO RUN THIS BLOCK

# newfile = open ("newfile.txt", "w")             #to create new file using the accsess mode writing
# newfile.write("I like Python!\n Do you?")       #to write on the new file and this will be replace the content existing
# newfile.close()
# newfile = open("newfile.txt", "a")                 #to write with access mode appending to file
# newfile.write("bicara lah")                        # adding text on file
# newfile.close()
#
# newfile = open("newfile.txt", "w+")                 #to write with access mode appending to file
# newfile.write("bicara lah")                        #remove all content then write with the new adding text
# newfile.close()
# newfile.closed                                      # to check if file is closed

# with open("newfile.txt", "w") as f:               #this file will be open and write to the file then otomatic closed the file
#     f.write("Hello Python!!!")


####### DELETE FILE CONTENT (REMOVE THE COMENT TO RUN THIS BLOCK
# f = open("test/test.txt", "r+")                     #slloe to read and write on the file
# f
# f.seek(0)
# len(f.read())
# f.truncate(10)                                        #to remove after 10 character
# len(f.read())


####### REGEX - MATCH & SEARCH (REMOVE THE COMENT TO RUN THIS BLOCK
# mystr = "You can learn any programming language, whether it is Python3, Perl, Java javascript or PHP"
#
# import re
# a = re.match("You", mystr)                          # a is a match object because found the string given as a pattern at the beginning
# a. group()                                          #to group match
#
# b = re.match("you", mystr, re.I)                    #to create mathch objek with flag ("re.I") to ignoring


