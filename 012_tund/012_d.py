import os
# os.mkdir('new1')
# print(os.rename('sample.txt','new1/test.txt')) #rename and move if add dir
#s.remove('new1/test.txt')
#print(os.stat('sample.txt').st_size)
information=os.walk('../')
for dirpatch,dirnames,filenames in information:
    # print('Current patch:'+dirpatch)
    # print('Directories:' + str(dirnames))
    # print('Files:' + str(filenames))
    if '007_b.py' in filenames:
        print(dirpatch)