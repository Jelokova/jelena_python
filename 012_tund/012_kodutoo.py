import os
try:
    os.makedirs(r'C:\Users\gamma\Desktop\for_sorting\text')
    print('done')
except:
    print()


try:
    os.makedirs(r'C:\Users\gamma\Desktop\for_sorting\picture')
    print('done')
except:
    print()
print(os.path.splitext(r'C:\Users\gamma\Desktop\for_sorting'))
