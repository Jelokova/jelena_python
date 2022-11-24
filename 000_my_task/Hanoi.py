def hanoi (n, start, finish):
    if n<=0: return
    temp=6-start-finish
    hanoi(n-1,start, temp)
    print("remove disk",n,"from disk", start,"to disk", finish)
    hanoi(n-1, temp, finish)
hanoi(5,1,3)