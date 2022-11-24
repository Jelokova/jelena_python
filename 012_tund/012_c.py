import os
import time
print(dir(os))
print(len(dir(os)))
print(os.getcwd()) #currect working dir as str
#os.chdir('../') #change dir =her is one level up
#print(os.getcwd())

#os.mkdir('new1/new2')#create one dir or new dir in existing no sequesneses of dir
os.makedirs('new1/new2/new3') #use tryexept to check if not created. or will get error
time.sleep(5)
os.rmdir('new1/new2/new3')#remove last dir
#os.removedirs('new1/new2/new3) #remove all dir


