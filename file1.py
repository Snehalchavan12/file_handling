
file1 =open ('sample.txt','r')
reading_file = file1.readlines ()
print (reading_file)
file1.close ()


'''
try:
    with open('non_existent_file.txt', 'r') as file1:
        content = file1.read()
except FileNotFoundError:
    print("The sample file does not exist.")
    '''