The project " Estimating Pi with Random Points" was  carried out by five students, as indicated in the project description. 
We agreed to divide tasks ax as follows: 
- Jacques Kodjitebaye was responsible for the function that estimates the value of pi: estimate_pi(n).
- Khardiata Ba also implemented a function called estimate_area to verify the functionality of these functions. 
- Gnagna Camara first implemented a column based display of the different estimation results and their corresponding errors. Secondly, she handled the case of estimate_area with its different specified values. 
- Fagbedji Gbenakpon Camille was mainly responsible for the extra task, which consisted of determining how many points were needed to obtain an error smaller than the specified value.
- Edward Ndungu wrote the README.md file to explain the project's objective and provide comments on certain aspects, such as the errors .     

About the bug, we have try firstly a while loop with this function: 
""" 

""" 
The problem of this code is that we assume that if we have a value of (n) where the error is less than 0.005, we should check the condition for the  next ten values of (n). However, when we update (n) by multiplying it by a hundred , the value becomes too large, making the program behave as if it were stuck in an infinite loop. We refined the approach and write a program to find the value of (n) for which the error is less than 0.005 in 20 consecutive trials. 