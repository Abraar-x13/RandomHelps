# QUESTION 6 : Suppose, you are working in a company ‘X’ where your job is to
# calculate the profit based on their investment. If the company invests
# 100,000 USD or less, their profit will be based on 75,000 USD as first
# 25,000 USD goes to set up the business in the first place. For the first
# 100,000 USD, the profit margin is low: 4.5%. Therefore, for every 100
# dollar they spend, they get a profit of 4.5 dollar. For an investment
# greater than 100,000 USD, for the first 100,000 USD (actually on 75,000
# USD as 25,000 is the setup cost), the profit margin is 4.5% where for
# therest,itgoesupto 8%.Forexample,iftheyinvest250,000USD,theywillget an 8%
# profit for the 150,000 USD. In addition, from the rest 100,000 USD, 25,000
# is the setup cost and there will be a 4.5% profit on the rest 75,000.
# Investment will always be greater or equal to 25,000 and multiple of 100.
# Complete the RECURSIVE methods below that take an array of integers
# (investments) and an iterator (always sets to ZERO(‘0’) when the method
# is initially called) and prints the profit for the corresponding
# investment. You must avoid loop and multiplication (‘*’) operator.

class FinalQ:
    def print(self, array, idx):
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            print("Investment: " + str(array[idx]) + "; Profit: " + str(profit))
            return self.print(array, idx + 1)

    def calcProfit(self, investment):
        if investment < 25000:
            return "Investment can't be smaller than 25,000"
        elif investment % 100 != 0:
            return "Investment will always be a multiple of 100"
        elif investment <= 100000:
            return self.case1(investment - 25000)
        else:
            return self.case2(investment - 100000) + self.case1(75000)

    def case1(self, div, count=1):
        if count == 5:
            # v = (div/2)/100
            return div/200
        else:
            v1 = self.case1(div, count + 1)
            return (div/100) + v1

    def case2(self, div, count=1):
        if count == 8:
            return div/100
        else:
            v2 = self.case2(div, count + 1)
            return (div/100) + v2


if __name__ == '__main__':
    array = [25000, 100000, 250000, 350000]
    f = FinalQ()
    f.print(array, 0)
