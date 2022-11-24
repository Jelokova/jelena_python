import os
print(os.environ.get('HOMEPATCH'))
print(os.environ.get('DATABESE_USERNAME'))

file_patch =os.path.join('new1','test.txt')
print(file_patch)

print(os.path.basename('/somedir/di2/sample.txt'))
print(os.path.dirname('/somedir/di2/sample.txt'))
print(os.path.split('/somedir/di2/sample.txt'))
print(os.path.splitext('/somedir/di2/sample.txt')) ### for homework take type of file

