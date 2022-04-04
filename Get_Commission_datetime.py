import datetime

def get_commission(date_str = ''):
    '''Function for evaluating commission based on month in year
    
    Parameters
    ---------
    date_str : str
        String containing date in the format YYYY-MM-DD. Default is "".
        
    Returns
    -------
    Float, 0.1 is for 10% and 0.15 is for 15%. -1 is for invalid date.'''
    
    try:
        date_str = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        check = 1
    except ValueError:
        check = -1

    if check == 1:
        if date_str.month > 5 and date_str.month < 10:
            return 0.15
        elif date_str.month == 12 or date_str.month == 1:
            return 0.12
        else:
            return 0.1
    else:
        return check

if __name__ == '__main__':

    date_str = input("Please enter a date in the format 'YYYY-MM-DD': ")

    get_commission(date_str)