# a2.py
from pathlib import Path
from Profile import Post
from ui import cd
# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ethan Ngo
# ngoet4@uci.edu
# 34741355

def main():
    
    direction = " "
    words = " "
    
    load = False
    create = False
    user_op = input("Welcome! Do you want to create or load a DSU file (type 'c' to create or 'l' to load, or 'admin' to enter admin mode): ")
    if user_op == 'admin':
        cd.admin()
    elif user_op == 'c':
        name = input("What is the name of the file you would like to create? ")
        directory = input("To what directory? ")
        non_admin_mode = True
        create = True
    elif user_op == 'l':
        name = input("What is the name of the file you would like to load? ")
        non_admin_mode = True
        load = True

    while non_admin_mode:
        '''Keeps running until user quits. load and create are used as entry functions and are not used anymore'''
        
        if load == True:
            '''File will be loaded. Boolean becomes false so this is not ran again.'''
            myPath = Path(name)
            if myPath.exists() and myPath.suffix.lower() == ".dsu":
                try:
                    print("File loaded")
                    words, direction = cd.command_open(myPath)
                    print(words)
                    pass
                except:
                    print('Error')
            load = False
            pass
            cd.command_open(name)
        if create == True:
            '''File will be created. Boolean becomes false so this is not ran again.'''
            myPath = Path(directory)
            fyepath = cd.create(myPath, name)
            print(fyepath)
            user_profile = cd.create_p(fyepath)
            print(user_profile)
            direction == f'{myPath}/{name}.dsu'
            create = False
            pass

        x = input('Anything else? Your options are L, D, R, C, O, P, E, Q: ')
        extra_option = " "

        if x.upper() == "L":

            direction = input('Name of directory?: ')
            extra_option == input('Would you like to add an extra option? Your choices are r, f, s, e: ')
            ourPath = Path(direction)

            if extra_option == 'r':
                exxtra_op = input("Any more options? Your choices are f, s, e: ")
                if exxtra_op == 'f':
                    for x in cd.option_rextra(ourPath):
                            if x.is_file():
                                print(x)
                elif exxtra_op == 's':
                    s_name = input("Name of file?: ")
                    for x in cd.option_rextra(ourPath):
                            if s_name in x.name:
                                print(x)
                elif exxtra_op == 'e':
                    e_name = input("Name of extension?: ")
                    for x in cd.option_rextra(myPath):
                         if x.is_file() and f'.{e_name.lower()}' == x.suffix.lower():
                             print(x)
                else:
                    cd.option_r(ourPath)
            elif extra_option == 'f':
                cd.option_f(ourPath)
            elif extra_option == 's':
                s_name = input('Name of file?: ')
                cd.option_s(ourPath, s_name)
            elif extra_option == 'e':
                e_name = input("Name of extension?: ")
                cd.option_e(ourPath, e_name)
            else:
                cd.L(ourPath)
        elif x.upper() == 'D':
            direction = input('Name of directory?: ')
            ourPath = Path(direction)
            if ourPath.suffix.lower() != ".dsu":
                    print('ERROR')
            else:
                cd.delete(ourPath)
        elif x.upper() == 'R':
            direction = input("Name of directory?: ")
            ourPath = Path(direction)
            if ourPath.suffix.lower() != ".dsu":
                print('ERROR')
            else:
                cd.read(ourPath)

        elif x.upper() == 'C':
            direction = input('Create to what directory?: ')
            name = input('Name of file?: ')
            ourPath = Path(direction)
            fyepath = cd.create(ourPath, name)
            print(fyepath)
            user_profile = cd.create_p(fyepath)
            print(user_profile)
            direction == f'{ourPath}/{name}.dsu'

        elif x.upper() == 'O':
            direction = input('Name of directory?: ')
            if ourPath.exists() and ourPath.suffix.lower() == ".dsu":
                print("File loaded")
                words, direction = cd.command_open(ourPath)
            else:
                print('File does not exist.')

        elif x.upper() == 'P':
            long_input = input('What P commands would you like to do? Your options are (-all, -posts, -usr, -pwd, -bio, -post): ')
            long_input_list = long_input.split()
            ourPath = Path(direction)

            for inputs in range(len(long_input_list)):
                if long_input_list[inputs] == '-all':
                    print(words)
                elif long_input_list[inputs] == '-posts':
                    cd.command_p(ourPath, long_input_list[inputs])
                elif long_input_list[inputs] == '-usr':
                    cd.command_p(ourPath, long_input_list[inputs])
                elif long_input_list[inputs] == '-pwd':
                    cd.command_p(ourPath, long_input_list[inputs])
                elif long_input_list[inputs] == '-bio':
                    cd.command_p(ourPath, long_input_list[inputs])
                elif long_input_list[inputs] == '-post':
                    material = int(input('What index?: '))
                    cd.command_p(ourPath, long_input_list[inputs], material)


        elif x.upper() == 'E':
            long_input = input("What E commands would you like to do? Your options are (-usr, -pwd, -bio, -addpost, -delpost): ")
            long_input_list = long_input.split()
            ourPath = Path(direction)

            for inputs in range(len(long_input_list)):
                if long_input_list[inputs] == '-usr':
                    content = input('What name would you like to change it to?: ')
                    cd.command_e(ourPath, long_input_list[inputs], content)
                elif long_input_list[inputs] == '-pwd':
                    content = input('What password would you like to change it to?: ')
                    cd.command_e(ourPath, long_input_list[inputs], content)
                elif long_input_list[inputs] == '-bio':
                    content = input('What bio would you like to change it to?: ')
                    cd.command_e(ourPath, long_input_list[inputs], content)
                elif long_input_list[inputs] == '-addpost':
                    content = input('What post would you like to add?: ')
                    cd.command_e(ourPath, long_input_list[inputs], content)
                elif long_input_list[inputs] == '-delpost':
                    content = int(input('What is the index of the post you would like to delete?: '))
                    cd.command_e(ourPath, long_input_list[inputs], content)
        elif x.upper() == 'Q':
            break






    

if __name__ == '__main__':
    main()