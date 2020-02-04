import datetime
from dateutil import parser as date_parser

verbose_days = {'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun' }

def make_EOD(d):
    return d.replace(hour=20, minute=00, second=00, microsecond=0)

def verbose_day_to_datetime(verbose):
    td_1 = datetime.timedelta(days=1)
    if verbose == 'today':
        parsed_date = date_parser.parse(verbose)
    elif verbose == 'tomorrow':
        parsed_date = datetime.datetime.now() + td_1
    elif verbose in verbose_days:
        parsed_date = parser.parse(verbose)
    else:
        raise Exception(verbose + ' is not a supported format. \nFormats supported: %s' % verbose_days)
    return make_EOD(parsed_date)

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

    if '-' in unparsed_date:
        if 'today' in unparsed_date or 'tomorrow' in unparsed_date:
            #create a time from the hyphenated integer
            day, time = unparsed_date.split('-')
            try:
                hour, minute = time.split(':')
            except ValueError:
                hour = time
        elif 'tomorrow' in unparsed_date:
    else:
        parsed_date = verbose_day_to_datetime(unparsed_date)


if __name__ == '__main__':
    pass
    #TODO unit-testing





