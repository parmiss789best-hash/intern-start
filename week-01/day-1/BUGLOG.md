this is a sample bug i experienced during the previous code:
the loop continued indefinitely.
Hypothesis:
The value of n was not being updated correctly inside the while loop.
Experiment:
I checked the indentation of n = n // 2 and tested the function with a positive integer.
Root Cause:
The division statement was outside the while loop, so the value of n did not change during each iteration.
Fix:
I moved n = n // 2 inside the while loop.
Lesson:
The loop variable must be updated correctly