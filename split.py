# Program to split lists like user:passwords to
# Two seperated lists with the name of users.txt and passes.txt
# It can be used for bruteforce with burpsuite and somethings like it.

# Get file name from user and open it
get_file_name = input('*************************************\nPlease write your file name or address\n(e.g: creds.txt or /home/user/Desktop/creds.txt )\n: ')
open_file = open(get_file_name,'r')

# Creat users.txt and passes.txt files
users_txt_file_creat= open('users.txt','x')
passes_txt_file__creat= open('passes.txt','x')

# Variable to append users and password to end of files
user= open('users.txt','a')
passes= open('passes.txt','a')

# Variabes to read file and put each seperated line as one item of list 
read_file=open_file.read()
split_file=read_file.split()

# Create new necessary lists
clear_list=[]
final_list=[]

# For loop to delete lines without ":" charecter
for index_loop in split_file:
    if ':' in index_loop:
        clear_list.append(index_loop)
    else:
        continue

# For loop to seperate each username with thats password in one seperated list
for seperated_items in clear_list:
    new_listes=seperated_items.split(':')
    final_list.append(new_listes)

# For loop to put each usernames and passwordes in same line on users.txt and passes.txt file 
for final in final_list:
    user.write(final[0]+'\n')
    passes.write(final[1]+'\n')
    
print('\n new files created :)')
