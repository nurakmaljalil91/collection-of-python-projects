import json
import time
import os
import string
import random
# main function


def main():
    # application variables
    is_running = True  # is the app running
    is_saving = False  # is the app is saving
    is_timing = True
    init()  # initialize the app
    while is_running:
        print('>>Enter your command here')
        action = input('>>:')
        if action == 'init':
            init()
        if action == 'quit!' or action == 'q!':
            is_running = False
            is_timing = False
        if action == 'q':
            if is_saving == False:
                print('The application is not saving...save file?')
        if action == 'help':
            help()
        if action == 'show':
            show()
        if action == 'addTask':
            addTask()
        if action == 'showDateTime':
            show_time()
        if action == 'done':
            done()
        else:
            print('Command not found! (type help to show all commands)')
        print('')

    print('TODO is exiting.......')


def init():
    # application information and attributes
    author = 'Nur Akmal arcmole007'  # author name : str
    company_name = 'OHWOW Game Studio est. 2019'  # game company name : str
    build = 1  # version number build : int
    major_change_no = 10  # version major changes no : int
    minor_change_no = 74  # version minor changes no : int
    version = '{}.{}.{}'.format(
        build, major_change_no, minor_change_no)  # version : str
    # this is welcoming page and developer description
    print('welcome to TODO_cli')
    print('Author :', author)  # show author name
    print('Software version :', version)  # show application version
    print('Company :', company_name)  # show company name
    print('')


def help():
    print('1. help    -- show all the commands ')
    print('2. show    -- show all the tasks ')
    print('3. addTask -- add new task to tasks ')
    print('4. quit!   -- quit without saving ')
    print('')


def show():
    with open('../data.json') as f:
        data = json.load(f)
    print('+-------------------------------------------------------------------------------+')
    print('|\t Task \t\t\t| End Date \t| Status \t| Due Time      |')
    print('+-------------------------------------------------------------------------------+')
    num_task = 1
    for d in data:
        print('{}.{:30}|{:15}|{:15}|{:15}|         '.format(
            num_task, d['task'], d['end date'], d['status'], 2))
        num_task += 1
    print('+-------------------------------------------------------------------------------+')


def addTask():
    pass


def show_time():
    localtime = time.asctime(time.localtime(time.time()))
    print("Current time :", localtime)


def generate_unique_id():
    # Generate a random string
    # with 32 characters.
    unique_id = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(5)])
    print(unique_id)


def done():
    with open('../data.json', 'r') as r:
        data = json.load(r)
    print('+-----------------------------------------------+')
    print('|\t Task \t\t\t| Unique Id     |')
    print('+-----------------------------------------------+')
    num_task = 1
    for d in data:
        print('{}.{:30}|{:15}|'.format(num_task, d['task'], d['unique id']))
        num_task += 1
    print('+-----------------------------------------------+')
    print('')
    print('>>Choose task to change status to done (write unique id)')
    un_id = input('>>:')

    for do in data:
        do.pop('{un_id}', None)
    
    with open('../data.json', 'w') as w:
        data = json.dump(data, w)


main()
