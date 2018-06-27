# Agron Velovic
# hastings.py
import numpy as np
import math
import time
import random

def tickerName(size):
# In this function I am simply taking the name of every stock and putting it into
# a list
    file = open("100tickers.txt","r")
    n = 0
    t = []
    for line in file:
        # we will only run this loop for the given number of days
        if(n<size):
            # we have to strip \n from every entry
            t.append(line.strip("\n"))
            n += 1
        else:
            break
    file.close()
    return t


def getReturns(ticker, days):
    # In this function we will find the corresponding stock name given by our
    # tickername function and we will take only take a certain number of days of data
    # given by the user
    size = len(ticker)
    # we will essentially return a matrix
    returns = np.zeros((size,days))
    for i in range(size):
        n = 0
        file = open("quotes"+ticker[i]+".txt")
        next(file)
        for j in file:
            if(n<days+1):
                # we wll convert every line of our files into a list
                day = j.split(",")
                if n == 0:
                    # we will only need the 2nd entry in our new lsit which corresponds
                    # to the open price
                    future_return = float(day[1])
                    n += 1
                    del day[:]
                else:
                    todays_return = float(day[1])
                        # we will divide every stock opening by its previous opening and
                        # take the log of the quotient, and we will put this answer into out matrix
                    daily_return = math.log(future_return/todays_return)
                    future_return = todays_return
                    returns[i][n-1] = daily_return
                    n += 1
                    del day[:]
            else:
                break
    return returns

def Variance(Weights, Cov, total):
    # this function will find the variance of our simple portfolio
    Vmin = np.zeros(total)
    for i in range(total):
        sum = 0
        for j in range(total):
            sum += Cov[i][j]*Weights[j]
        Vmin[i] = sum

    var = 0
    for i in range(total):
        var += Vmin[i]*Weights[i]
    return var



#################################################################################
print("How many stocks would you like to use (100 stocks maximum): ")
size = int(input())
days = 50


ticker = tickerName(size)
returns = getReturns(ticker, days)
stocks = len(ticker)
s = stocks

# W will be my indicator vector
W = np.ones(stocks)
# Weights will be the weights of my original portfolio in this case it does not matter
# much because we will quickly move away from our original portfolio
Weights = np.full(stocks, 1/stocks)

covariance = np.cov(returns)
covariance = covariance*10000

# we will find the variance of our original portfolio
E_min = Variance(Weights, covariance, stocks)
OldVar = E_min

print("Please enter a temperature: ")
T = float(input())

print("How long will you like to run this code (seconds): ")
TIME0 = int(input())
t_end = time.time()+TIME0
time0 = time.time()
elapsed_time = .1

while time0 < t_end:
    # we will generate a random number from 1 to the number of stocks
    x = int(size*random.uniform(0,1))
    # we will flip the sign in the indicator vector indexed by our randomky
    # generated  number
    if(W[x] == 1):
        W[x] = 0
        s -= 1
    elif(W[x] == 0):
        W[x] = 1
        s += 1
    # now we will change the weights of our stocks
    for i in range(stocks):
        Weights[i] = W[i]/s
    # we calculate the variance of our new portfolio
    NewVar = Variance(Weights, covariance, stocks)

    deltaE = abs(NewVar - OldVar)

    # if our new portfolio has a smaller variance we automatically move to it
    if NewVar < OldVar:
        E_min = NewVar
        OldVar = E_min
    # else we would move to our new portfolio with some positive probability p
    else:
        p = math.exp(-deltaE/T)
        U = random.uniform(0,1)
        # p must be greater than our randomly generated number
        if p >= U:
            E_min = NewVar
            OldVar = E_min
        # if it is not than we return to the previous portfolio
        else:
            if(W[x] == 1):
                W[x] = 0
                s -= 1
            elif(W[x] == 0):
                W[x] = 1
                s += 1

    print( "%.3f: %.5f"% (TIME0+time0 - t_end, E_min))
    time0 = time.time()

print(" ")
sum = 0
print("Best found simple portfolio is: ")
for k in range(stocks):
    if(W[k]):
        print(ticker[k],": ", 1/s)
        sum += 1
print("\n VARIANCE: ",E_min)
print("Total number of stocks in portfolio: ", sum)
