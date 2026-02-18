import os
import sys
import time

# Determine operating_system and define applications directory
if sys.platform == 'win32':
    steamapps_directory = 'F:/Steam/steamapps/common' # Windows
    #print ('windows')
elif sys.platform == 'darwin':
    steamapps_directory = '/Library/Application Support/Steam/steamapps/common' # Mac 
else:
    print('Operating System not determined. Applications directory not set.')
    quit()
## print('Steam apps directory:',steamapps_directory)

# Validate the path
if not os.path.exists(steamapps_directory):
    print ('{} does not exist'.format(steamapps_directory))
    quit()

# Get the contents of the steam apps directory and sort them into two catagories
directory_contents = os.listdir(steamapps_directory)
files = list()
directories = list()
for item in directory_contents:
    item_path = os.path.join(steamapps_directory,item)
    if os.path.isdir(item_path):
        directories.append(item)
    else:
        files.append(item)

print('\nFiles: ',files)
print('\nFolders', directories)

# Construct a dictionary that maps each steam apps directory to the date modified 
# EX. {'Mewgenics' : 'Tue Feb 10 10:14:21 2026'}
manifest_dict = dict()
for item in directories:
    item_path = os.path.join(steamapps_directory,item)
    modified_time = os.path.getmtime(item_path)
    manifest_dict[item] = time.ctime(modified_time)
    
print(' ')
for key, value in manifest_dict.items():
    print(key, ":", value)