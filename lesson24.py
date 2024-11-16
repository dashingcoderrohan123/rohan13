#The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.

mean1=38
total_numbers=40
wrong_number=36
correct_number=56

sum=mean1*total_numbers
print(sum)

sum2=sum-(wrong_number)+(correct_number)
print(sum2)

mean2=sum2/total_numbers
print(mean2)