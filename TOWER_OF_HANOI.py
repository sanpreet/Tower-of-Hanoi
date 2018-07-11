#This is the code of Tower of Hanoi################
#this is a function which will be called when we have to move just disk from source to destination
def move_disk(a, b):
    print('Disk is moved from %s %s' % (a, b))
#This is the recursive function because this game allows to put one disk at a time so we can play with recursion
def tower_of_hanoi(n, source, destination, help):
    if n >= 1:  #This condition states that at least there should be one disk present to move
        tower_of_hanoi(n - 1, source, help, destination) #recursion
        move_disk(source, destination)                   #refer to function move_disk(a,b)
        tower_of_hanoi(n - 1, help, destination, source)  #again recursion
# actual program starts here
def main(): # this is the main function
    while True:   #runs infinite unless the condition remains true
        try:       #putting the case in the try statement, This reflects good coding skills
            n = int(input("Enter the value from the use")) #please enter the value in the integer form
        except ValueError:   #if value is not integer it would raise value error
            break             #Break from the code is executed here
        if n == 0:            #if value so entered is zero, again break because there is no disk to move from source to destination
            break
        A = tower_of_hanoi(n, "A", "B", "C")  #it will go to the function callled which is tower_of_hanoi

main()         #runs the main function
