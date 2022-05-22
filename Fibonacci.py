# Initialize variables
a = 0
b = 1
i = 1
list0 = []
# Loop to keep code running
while True:
    n = int(input('Enter limit of series : '))
    while i <=n:
        a = b
        b = i
        i = a + b
        list0.append(i)
    
    Prompt  = int(input("Enter desired position: "))
    if Prompt > len(list0):
        print("Position out of range")
    else:
        print("Number at that position is: ", list0[Prompt-1])
    
    
