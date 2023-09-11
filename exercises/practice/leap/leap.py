def leap_year(year):
    def leap_year(year):
    """Check if a year is a leap year.

    :param year: int - the year to check.
    :return: bool - True if the year is a leap year, False otherwise.

    This function checks if a year is a leap year based on the following rules:
    1. It is evenly divisible by 4.
    2. It is not evenly divisible by 100, except when it is also evenly divisible by 400.
    """

    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False
