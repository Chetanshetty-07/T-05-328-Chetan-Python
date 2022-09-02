'''
Contol Statements
control statements change the way we execute a loop from it’s normal behavior.
There are many types of control statements in python that you can use to control the loops.
Different types of control statements available in python are:

1.Break Statement
2.Continue Statement
3.Pass Statement

1.Break Statement
Break statement is used to terminate or abandon the loop. Once the loop breaks then the next statement after the break continues.
The main reason we could use the break statement is to take a quick exit from a nested loop (i.e. a loop within a loop).
The break statement is used with both while and for loop.

Example :
car_name = "\nPlease enter the name of the Car you love: "
while True:
    car = input(car_name)
    if car == 'Jaguar E-pace':
        break
    else:
        print("My favorite car is: " + car.title())

1.Output:buggati chiron
       buggati chiron
2.Output:Jaguar E-pace
         #program come out of the loop

2.Continue Statement

Continue statement in Python is used to continue running the program even after the program encounters a break during execution.
The continue statement enables the code to proceed inside a loop and move on skipping the particular condition.

Example:for x in range(11):
    if x == 5:
        continue
    print ('Number:', x)
Output:
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
Number: 6
Number: 7
Number: 8
Number: 9
Number: 10

3.Pass statement
The pass statement is used when comment cannot be printed to show the program’s status to the programmer.
It is always going to be a null operation. For example if a programmer has written a comment within the code,
then that comment will be ignored but the pass statement won’t be ignored. It will be used as a placeholder.
Example:for x in range(11):
    if x == 5:
        pass
        print("We are still printing numbers")
    print ('number:', x)
Example:

for x in range(11):
    if x == 5:
        pass
        print("We are still printing numbers")
    print ('number:', x)

Output:
number: 0
number: 1
number: 2
number: 3
number: 4
We are still printing numbers
number: 5
number: 6
number: 7
number: 8
number: 9
number: 10


'''
