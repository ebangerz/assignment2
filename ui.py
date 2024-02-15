# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ethan Ngo
# ngoet4@uci.edu
# 34741355

from pathlib import Path
from Profile import Profile
from Profile import Post

RECURSIVE = []
class cd:
    def __init__(self) -> None:
        pass
    
    def admin():

        direc = " "
        words = " "
        
        while True:
            user_input = input()
            user_input_list = user_input.split()
            myPath = Path(cd.get_directory(user_input_list))

            if user_input[0] == 'L':
                if '-r' in user_input:
                    if '-f' in user_input:
                        for x in cd.option_rextra(myPath):
                            if x.is_file():
                                print(x)
                    elif '-s' in user_input:
                        for x in cd.option_rextra(myPath):
                            if user_input_list[-1] in x.name:
                                print(x)
                    elif '-e' in user_input:
                        for x in cd.option_rextra(myPath):
                            if x.is_file() and f'.{user_input_list[-1].lower()}' == x.suffix.lower():
                                print(x)
                    else:
                        cd.option_r(myPath)
                elif '-f' in user_input:
                    cd.option_f(myPath)
                elif '-s' in user_input:
                    cd.option_s(myPath, user_input_list[-1])
                elif '-e' in user_input:
                    cd.option_e(myPath, user_input_list[-1])
                else:
                    cd.L(myPath)

            elif user_input[0].upper() == 'D':
                if myPath.suffix.lower() != ".dsu":
                    print('ERROR')
                else:
                    cd.delete(myPath)
            elif user_input[0].upper() == 'R':
                if myPath.suffix.lower() != ".dsu":
                    print('ERROR')
                else:
                    cd.read(myPath)

            elif user_input[0].upper() == 'C':
                fyepath = cd.create(myPath, user_input_list[-1])
                print(fyepath)
                user_profile = cd.create_p(fyepath)
                print(user_profile)
                direc = f'{myPath}/{user_input_list[-1]}.dsu'
            elif user_input[0].upper() == 'O':
                if myPath.exists() and myPath.suffix.lower() == ".dsu":
                    print("File loaded")
                    words, direc = cd.command_open(myPath)
                else:
                    file = cd.create(myPath, user_input_list[-1])
                    print(file)
            elif user_input[0].upper() == 'P':
                for inputs in range(len(user_input_list)):
                    if user_input_list[inputs] == '-all':
                        print(words)
                    elif user_input_list[inputs] == '-posts':
                        cd.command_p(direc, user_input_list[inputs])
                    elif user_input_list[inputs] == '-usr':
                        cd.command_p(direc, user_input_list[inputs])
                    elif user_input_list[inputs] == '-pwd':
                        cd.command_p(direc, user_input_list[inputs])
                    elif user_input_list[inputs] == '-bio':
                        cd.command_p(direc, user_input_list[inputs])
                    elif user_input_list[inputs] == '-post':
                        material = int(user_input_list[inputs + 1])
                        cd.command_p(direc, user_input_list[inputs], material)
                    
                    


            elif user_input[0].upper() == 'E':
                for inputs in range(len(user_input_list)):
                    if user_input_list[inputs] == '-usr':
                        material = cd.retrieve(user_input_list, user_input_list[inputs])
                        material = " ".join(material)
                        cd.command_e(direc, user_input_list[inputs], material)
                    elif user_input_list[inputs] == '-pwd':
                        material = cd.retrieve(user_input_list, user_input_list[inputs])
                        material = " ".join(material)
                        cd.command_e(direc, user_input_list[inputs], material)
                    elif user_input_list[inputs] == '-bio':
                        material = cd.retrieve(user_input_list, user_input_list[inputs])
                        material = " ".join(material)
                        cd.command_e(direc, user_input_list[inputs], material)
                    elif user_input_list[inputs] == '-addpost':
                        material = cd.retrieve(user_input_list, user_input_list[inputs])
                        material = " ".join(material)
                        cd.command_e(direc, user_input_list[inputs], material)
                    elif user_input_list[inputs] == '-delpost':
                        material = int(user_input_list[inputs + 1])
                        cd.command_e(direc, user_input_list[inputs], material)
                    





            elif user_input[0] == 'Q':
                break

    def command_open(directory):
        '''Opens file given directory'''
        p = Path(directory)
        with open(p, 'r') as file:
            file_words = file.read()
        return file_words, p

    def command_e(directory, input = str, content = str):
        '''Edits a profile given directory, specified input, and what they would like to change it to'''
        path = Path(directory)
        x = Profile()
        y = Post()
        x.load_profile(str(path))
        
        if input == '-usr':
            x.username = content
        elif input == '-pwd':
            x.password = content
        elif input == '-bio':
            x.bio = content
        elif input == '-addpost':
            y.set_entry(content)
            y.timestamp = Post.get_time(y)
            x.add_post(y)
        elif input == '-delpost':
            x.del_post(int(content))
        x.save_profile(path)
        
    def command_p(directory, input = str, id = 0):
        '''Posts specified part of profile given directory and input'''
        path = Path(directory)
        x = Profile()
        x.load_profile(str(path))
        posts = x.get_posts()

        if input == '-usr':
            print(x.username)
        elif input == '-pwd':
            print(x.password)
        elif input == '-bio':
            print(x.bio)
        elif input == '-posts':
            for post in posts:
                print(post.get_entry())
        elif input == '-post':
            for post in posts:
                if post == posts[int(id)]:
                    print(posts[int(id)].get_entry())
        elif input == '-all':
            print(x.username)
            print(x.pwd)
            print(x.bio)
            for post in posts:
                print(post.get_entry())
        x.save_profile(path)

        
    def read(directory):
        '''If file contains something, will print out contents'''
        p = Path(directory)
        if p.exists() and p.stat().st_size == 0:
            print('EMPTY')
        else:
            try:
                with open(p, 'r') as file:
                    content = file.read()
                    print(content)
            except FileExistsError:
                print("File not found.")
            except:
                print('ERROR')

    def L(directory):
        '''Lists files and directories given directory'''
        for current in directory.iterdir():
            if current.is_file():
                print(current)
            elif current.is_dir():
                print(current)

    def option_rextra(directory):
        for current in directory.iterdir():
            RECURSIVE.append(current)
            if current.is_dir():
                cd.option_rextra(current)
        return RECURSIVE


    def option_r(directory):
        for current in directory.iterdir():
            print(current)
            if current.is_dir():
                cd.option_r(current)

    def option_f(directory):
        for current in directory.iterdir():
            if current.is_file():
                print(current)


    def option_s(directory, name):
        for current in directory.iterdir():
            if current.is_file() and name == current.name:
                print(current)

    def option_e(directory, extension):
        for current in directory.iterdir():
            if current.is_file() and (current.suffix.lower() == f'.{extension.lower()}'):
                print(current)
            if current.is_dir():
                cd.option_e(current, extension)

    def delete(directory):
        p = Path(directory)
        if p.exists():
            p.unlink()
            print(f'{p} DELETED')
        else:
            print('ERROR')


    def create(directory, name):
        p = Path(directory)
        file_path = p / f'{name}.dsu'
        file_path.touch()
        return file_path

    
    def get_directory(input):
        '''Retrieves directory and accounts for whitespace'''
        directory = []

        for x in range(len(input)):
            if input[x][0] == '-':
                break
            else:
                try:
                    directory.append(input[x+1])
                except IndexError:
                    break
        if directory[-1][0] == '-':
            directory.pop()
        path = " ".join(directory)
        return path
    
    def create_p(directory):
        '''creates profile to a specified directory. gives it username, password, and bio if user chooses so'''
        file_path = Path(directory)
        usr = input("Enter your username: ")
        passw = input("Enter your password: ")
        bio = input("Enter a bio (optional): ")
        profile = Profile(dsuserver = None, username = usr, password = passw)
        profile.bio = bio
        profile.save_profile(file_path)


    def retrieve(user_list: list, command: str):
        '''accounts for whitespace in user input'''
        contents = []
        c_index = user_list.index(command)

        for words in range(c_index + 1, len(user_list)):
            if user_list[words][-1] == '"':
                contents.append(user_list[words])
                break
            elif user_list[words].find('"') > -1:
                contents.append(user_list[words])
            else:
                contents.append(user_list[words])
        return contents


        

