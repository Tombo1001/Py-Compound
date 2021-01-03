# Py-Compound : A compound interest calculator writen in Python 3
import math

def func_invest(input1, input2):
    output = input1 + input2
    return output


def func_interest(input1, input2):
    rate = input2 / 100
    interest = input1 * rate
    output = input1 + interest
    return output


def func_pl_calc(input1, input2, input3):
    output = (input1 - input2) - input3
    return output


def func_round(input, decimals=2):
    multiplier = 10 ** decimals
    return math.floor(input*multiplier + 0.5) / multiplier


def func_main():
    currency = "£" #change to suit
    monthly_invest = 10 #change to suit
    total_invested = 0
    starting_portfolio = 10000 #change to suit
    total_portfolio = starting_portfolio
    cur_month = 1
    investment_period = 120 #(months) change to suit
    interest_period = 12 #(months) change to suit
    interest_percent = 5 #(%) change to suit

    print("-------------\nInterest rate during investment period: {}%".format(interest_percent))
    print("Month investment amount: {}{}".format(currency, monthly_invest))
    print("Starting balance: {:.2f}\n-------------".format(starting_portfolio))

    while cur_month <= investment_period:
        #investment math
        total_invested = func_invest(total_invested, monthly_invest)
        total_portfolio = total_portfolio + monthly_invest

        #check if interest payment due on balance
        if cur_month % interest_period == 0:
            total_portfolio = func_interest(total_portfolio, interest_percent)
            total_portfolio = func_round(total_portfolio)

        #increment investment period
        cur_month = cur_month + 1

    print("Total amount invested at end of period: {}{:.2f}".format(currency, total_invested))
    print("Interest value during investment period ({:.0f} year[s]): {}{:.2f}".format(investment_period / 12, currency, func_pl_calc(total_portfolio, total_invested, starting_portfolio)))
    print("\nPortfolio Value at end of period: {}{:.2f}\n-------------".format(currency, total_portfolio))

if __name__ == '__main__':
    func_main()
