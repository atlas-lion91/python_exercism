# Estimate value after exchange
# budget : The amount of money you are planning to exchange.
# exchange_rate : The amount of domestic currency equal to one unit of foreign currency.
# This function should return the value of the exchanged currency.

def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    estimated_value = budget / exchange_rate
    return estimated_value

# Calculate currency left after an exchange
# budget : Amount of money before exchange.
# exchanging_value : Amount of money that is taken from the budget to be exchanged.
# This function should return the amount of money that is left from the budget.

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    money_left = budget - exchanging_value
    return money_left

# Calculate value of bills
# This exchanging booth only deals in cash of certain increments. The total you receive must be divisible by the value of one "bill" or unit, which can leave behind a fraction or remainder. Function should return only the total value of the bills (excluding fractional amounts) the booth would give back. Unfortunately, the booth gets to keep the remainder/change as an added bonus.

def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    total_value = denomination * number_of_bills
    return int(total_value)



# Calculate number of bills
# This function should return the number of currency bills that you can receive within the given budget.

def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    number_of_bills = budget / denomination
    return int(number_of_bills)



# Calculate leftover after exchanging into bills
# This function should return the leftover amount that cannot be exchanged from your budget given the denomination of bills. It is very important to know exactly how much the booth gets to keep.

def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    bill_leftover = budget % denomination
    return bill_leftover




# Calculate value after exchange
# This function should return the maximum value of the new currency after calculating the exchange rate plus the spread. 

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    true_exchange_rate = exchange_rate + (exchange_rate * spread / 100)
    value_after_exchange = int(budget / true_exchange_rate / denomination) * denomination
    return value_after_exchange
