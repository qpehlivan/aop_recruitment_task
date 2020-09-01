# Titanic - data science project 

## INTRODUCTION
These are my solutions to the tasks given to me as a recruitment step. Even though I am not that experienced, I tried to do my best, because I want to work in this field.


### TASK1 - organizational instructions
Here is the GitHub page.

### TASK2 - sense of humour
I wrote the best joke ever written. You can find it in docs folder.

### TASK3 - good practices
Code has been fixed.

### TASK4 - feature engineering
I think the following attributes are not needed:
1- Name: In the Titanic scenario, name is irrelivant to passangers' survival(assuming that you are not Rose Dewitt Bukater).
2- Ticket: Instead of whether the person has a ticket or not, which everyone do have a ticket, the class of their ticket matters (because of location in an emergency scenario).
3- Fare: How much they pay for the ticket is irrelivant to passangers' survival.
4- Embarked: The ports that passangers embarked on the ship has no effect on their survival.

Other than these, I think cabin is an important factor. Because, the location of the passanger's cabin can play a vital role in terms of arriving to lifeboats in time, or simply avoiding the spot that the ship got damaged at, but it should still be avoided. The reason for that is that the data for cabin is missing for more than half of the passangers.

These are my logical assumptions, but I don't have the required experience to analyze every single attribute on their own. If I could, I would analyze each one of them by visualizing the data. And if I had any more questions, I would ask for a senior data scientist's help.

### TASK5 - models
Logistic Regression Algorithm.

### TASK6 - measures
I didn't analyze it myself, but I have researched and found out that the Random Forest Classifier is in fact one of the best methods to solve this problem. I would also try the Logistic Regression and compare their accuracy. The reason I chose the Logistic Regression is that it is a good fit for binary output problems. Since we have just two possible outcomes, it would be a good idea to try and see the performance of this method as well.

