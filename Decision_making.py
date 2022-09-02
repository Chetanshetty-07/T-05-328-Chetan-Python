
'''
Decision Making

In programming, we often have this similar situation where we need to decide which block of code should be executed based on a condition.

Decision-making statements are also known as conditional statements because they specify conditions with boolean expressions evaluated to
a true or false boolean value.

If the condition is true, the block will execute; if the condition is false, the block will not execute.
 Python has the following decision-making statements:
1.if statement
2.if else statements
3.nested if statements
4.if-elif ladder

1.if statement
The if statement is the most straightforward decision-making statement.
It is used to determine whether or not a specific statement or block of statements will be executed.
If a particular condition is true, then a block of statements is executed, otherwise not.
Syntax:
  if ( condition ):
  Statements to execute if
  condition is true
  Statement 1
  Statement 2
   :                :
  Statement n

2.if else statements
The if statement tells us that if a condition is true, a block of statements will be executed
if the condition is false, the block of statements will not be executed.
When the condition is false, we can use the else statement in conjunction with the if statement to run a code block.
Syntax:
if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false

3.nested if statements
In simple terms, nested if statements are if statements that are inside another if statement.
Python allows us to stack any number of if statements inside the block of another if statements.
They are useful when we need to make a series of decisions.
Syntax:
if (condition1):
   # Executes when condition1 is true
   if (condition2):
      # Executes when condition2 is true
   else:
#Executes when condition2 is false
else:
	# Execute when condition1 is false

4.if-elif ladder
The if statements are executed from the top down. When one of the elif conditions is satisfied,
the statement associated with that elif is executed, and the rest of the ladder is skipped.
If none of the conditions is satisfied, the last else statement is executed.
Syntax:
if (condition1):
    #Body of if
elif (condition2):
    Body of elif
elif (condition3):
    Body of elif
else:
    Body of else

'''

