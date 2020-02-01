import datetime
from dateutils import utils as dateutils

def make_EOD(d):
    return d.replace(hour=23, minute=59, second=59, microsecond=0)

def parse_date(unparsed_date):
    '''
    unparsed_date:
        days:
            'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'today', 'tomorrow'
        time:
            HH:MM, ex: 12:30 (deadline is at 12:30)
        day-time:
            <days>-<time>, ex: mon-12:30 (deadline is on mon, 12:30)
    
    NOTE: 
        1. If you only want the hours needed, then follow the same format as <time> but with a hyphenated 'r'
        Ex. 5:00-r (Task can be completed in 5 hours or deadline is in 5 hours)
    '''
    td_1 = datetime.timedelta(days=1)

    if unparsed_date in {'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'}:
        #create a datetime of the immediate day available
    elif unparsed_date == 'today':
        parsed_date = make_EOD(datetime.datetime.now())
    elif unparsed_date == 'tomorrow':
        parsed_date = make_EOD(datetime.datetime.now()) + td_1
    elif 'today' in unparsed_date:
        #create a time from the hyphenated integer
        day, time = unparsed_date.split('-')
        try:
            hour, minute = time.split(':')
        except ValueError:
            hour = time
    elif 'tomorrow' in unparsed_date:


if __name__ == '__main__':
    pass
    #TODO unit-testing





