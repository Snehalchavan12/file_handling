# file_handling
1] Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

    file1 =open ('sample.txt','r')
    reading_file = file1.readlines ()
    print (reading_file)
    file1.close ()

    try:
    with open('non_existent_file.txt', 'r') as file1:
        content = file1.read()
    except FileNotFoundError:
    print("The sample file does not exist.")

2] Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

    file3 = open ('output.txt','w')
    writing_file = file3.write ('hello,python!')
    print (writing_file)
    file3.close()

    file3 = open ('output.txt','a')
    appending_file = file3.write('Learning file handling to the python.')
    print (appending_file)
    file3.close()

    file3 = open ('output.txt','r')
    reading_file = file3.read()
    print (reading_file)
    file3.close()
    
