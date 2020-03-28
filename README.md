# Tower-of-Hanoi  
![f6bed3cf-c3da-41de-bde0-c9f939208fb1](https://user-images.githubusercontent.com/3431730/77816736-3199a600-70eb-11ea-9fc9-cf6260c392c3.jpeg)  

Puzzle Game
---

Tower of Hanoi is very intersting game and let us discuss the rules before going to code which you can find in the file TOWER_OF_HANOI.py
Rules for playing the game  

---

 * Disk are placed in the **descending** order from bottom to top which means the largest disk in diameter is placed at the bottom and is decreasing in size from bottom to top  
 * When you are moving the disk from source to destination, you can move **only one disk** at a time and orientation of the disks at the destination peg must be same as of source  
 * While transferring the disk from source peg to destination peg you can take the help of other peg/stick which you can call as **auxillary peg**.  
 
 ---
  
In the code file please go to the **comment section** so that you can understand the meaning of each line implemented in the code. In the  main function in the code, I have used the **while loop** and **try and catch**, please donot miss that. May be you may learn some additional concepts there. Recursion apppraoch is used by me. Just see these lines to know use of while, try and catch more.
```
while True:   #runs infinite unless the condition remains true
        try:       #putting the case in the try statement, This reflects good coding skills
            n = int(input("Enter the value from the use")) #please enter the value in the integer form
        except ValueError:   #if value is not integer it would raise value error
            break             #Break from the code is executed here
        if n == 0:            #if value so entered is zero, again break because there is no disk to move from source to destination
            break
```           

 Hope you like the code and understand the code in effective way.
