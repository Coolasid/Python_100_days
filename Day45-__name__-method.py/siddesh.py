def welcome():
    print('Hey you are welcome my frnd!')

def do_not_run_from_outside():
    print('do not run')

print(__name__)

if __name__ == "__main__":
    welcome()
    do_not_run_from_outside()

