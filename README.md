# HigherLowerGameSim

There is a game called "higher-lower". Basically the program picks a number 1-100 randomly and you have to guess it. If you guess wrong, the program informs you if the number you tried is "too high" or "too low" compared to the correct number.
In the Easy mode, you have 10 attempts.
In the Hard mode you only have 5 attempts.

#not important The game is easy to make. After making it, I showed it to some friends and they imidiatly started arguing about the "Best strategy" on the Hard mode. They agreed that after the first number they would devide by 2. But what was the best 1st number?
A mathematisian said that it made no difference as long as the number was in a specific range (15-85), and he proved it to me mathematically. But I wanted to be 100% certain and show my friends that the mathematitian was right. #not important

So I made a simulation for the hard mode, with which we can test what is the best number to begin with. The simulation plays the game 100k times and it keeps the wins inside a variable so you can have a % of te wins. 

It turns that if the first number you choose is in the range (16-84) you have the same odds of winning (31%). As you move on to the extremes the odds are progresively getting lower and lower with the lowest being observed with 1 and 100(16%).
