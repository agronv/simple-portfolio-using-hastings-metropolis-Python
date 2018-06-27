# simple-portfolio-using-hastings-metropolis-python

This project is a spin off of the minimum variance portfolio. this time I have used hastings metropolis in order to find the simple 
portfolio with the lowest volatility. To run the code simply download and unzip quotes.zip and download hastings.py within the same folder and run the code. I have also provided a file named StockDataToFile.cpp and a file named folder_creation.py. You don't have to use them to run the code, but I used them in order to get data from Quandl and in order to make the zip file. I used StockDataToFile.cpp to write a txt (named ticker.txt) file containing 753 tickers and to download 753 txt files from quandl containing data for the stock whose tickers are the ticker.txt. I used folder_creation.py to create a new folder named quotes and to randomly select 100 tickers from tickers.txt and to store them in a file named 100tickers.txt, then I copied the 100 txt files associated with the randomly selected tickers and stored them in my newly created folder. 

In order to get the code to run you have to download quotes.zip and unzip the folder. then simply save the file named hastings into the
folder and run it. The code will ask the user for some input like the number of stocks to sample from, the temperature, and the time. for
100 stocks I recommend picking a temperature of about .001. The lower the number of stocks the higher the temperature. The code will print
the time elapsed and the variance at every loop.

The hastings metropolis algorithym is a markov chain monte carlo simulation. it is used when our sample space is too large and it would
be computationally infeasible to test all possible outcomes. the hastings metropolis algorithm was originally developed for physicist thats
why it uses terms like energy and temperature, but I found it very useful for this application. essentially what we are doing is we are 
sampling from some random distribution and we record some output (energy) from this random sample. Then we find the neighbor of this random
smaple, if this neighbor has a lower energy then we will move to the neighbor and if this neighbor has a higher energy we will move to it
if and only if U < e^(-deltaE/T). Let me break down this equation. U is a random number between 0 and 1, deltaE is the change in energy,
and T is the temperature. the temperature is quite abritrary (my code works best with about .05 temperature). we move to a state with 
higher energy with positive porbability because we do not want to get stuck at a local minimum. We keep moving onto a neighboring state 
until  we are satisfied with the results.

In my scenario I have provided 100 different stocks and i am asked to find the best simple portfolio. A simple portfolio is a portfolio
where the weight of every stocks is equal. There are 2^100 different simple portfolios, which is an absurdly large number. The hardest 
part about the problem was decided what is a neighboring state. I have defined a neighbooring state a such, i have created an indicator
list that contains 1's and 0's, a 1 means that the stock is in the portfolio and a 0 means that it is not. then i will randomly pick an 
index in the list and if it is a 1 i will change it to a 0 and if it is a 0 i will hange it to a 1. I originally start with every stock
in the portfolio, because it doesnt really matter where you start. every state has 100 neighbors and we are always at a current state,
at every time step we move to a neighboring state and we find the variance of the state then we compare it to our current state. If our 
current state has higher energy we automatically move to the nieghboring state if the current state has lower energy then we will move to 
the higher energy state with some positive probability given by the equation above. We do this so that we dont get stuck at a local minimum.
We will keep moving to different states for the amount of time specified by the user but 30 seconds should be suffiecient. 
