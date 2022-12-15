PLACEHOLDER = "[name]"  # variable to modify the file content

"""converting the names from the files into a python list"""
with open("./Input/Names/invited_names.txt") as target:  # accessing the files with relative paths
    names = target.readlines()  # assigning the variable from the file contents (list of their names)

"""Creating new files with modified contents"""
with open("./Input/Letters/starting_letter.txt") as letter:  # accessing the mail templates
    contents = letter.read()  # converting the text files into a string
    for x in names:
        clean = x.strip()  # removing unusable character from the name lists
        sent_letter = contents.replace(PLACEHOLDER, clean)  # replacing the templates with the correct name
        with open(f"./Output/ReadyToSend/{clean}.txt", mode="w") as fix_mail:  # define the filenames &  directory
            fix_mail.write(sent_letter)  # writing the files for respective names
