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