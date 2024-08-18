import os
import random
import string

PATH = './junk'

# removing files
def remove_files(path):
    try:
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print('All files removed successfully')
    except OSError:
        print('Error in removing files')


#creating n files with random file name and format on specific given path
file_formats = ['.png', '.pdf', '.txt', '.mp4']

def create_files(formats, n, path):
    remove_files(path)
    for i in range(1, n+1):
        random_format = random.choice(formats)
        random_file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        with open(os.path.join(path, f'{random_file_name}{random_format}'), 'w') as f:
            pass

create_files(file_formats, 20, PATH)

#listing a file 
dir_list = os.listdir(PATH)
print(f"==>> dir_list: {dir_list}")



#replacing all files name for specific given file format on given path

def replace_name(format, path):
    dir_list = os.listdir(path)
 

    i = 1
    for file in dir_list:
        if file.endswith(format):
            print('os.path.join(file)', os.path.join(file))
            os.renames(os.path.join(path, file),os.path.join(path,  f'renamed_file_{i}{format}'))
            i+=1





replace_name('.png', PATH)




