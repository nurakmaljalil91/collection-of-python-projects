import json

def main():
    is_running = True
    is_saving = False
    init()
    while is_running:
        print('>>Enter your command here')
        action = input('>>:')
        if action == 'quit!' or action == 'q!':
            is_running = False
        if action == 'q':
            if is_saving == False:
                print('The application is not saving...save file?')
        if action == 'show':
            show()

    print('TODO is exiting.......')
def init():
    print('TODO')

def show():
    with open('../data.json') as f:
        data = json.load(f)
    print('+-------------------------------------------------------------------------+')
    print('|\t Task \t\t\t| Start Date \t| End Date \t| Progress|')
    print('+-------------------------------------------------------------------------+')
    for d in data:
        print('>>{}            |{}         '.format(d['task'],d['date']))
    
    

main()