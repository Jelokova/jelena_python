# while True:
#     print('I can\t stop')

x=100
while x>0:
    print(x**2)
    x-=1

#step-counter programm
distansce_to_target=float(input('Enter distance to km '))*1000
current_position=0
step_cnt=0
while current_position<distansce_to_target:
    current_position+=0.7
    step_cnt+=1
print(step_cnt)