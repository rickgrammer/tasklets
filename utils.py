import datetime
from dateutil import parser as date_parser

verbose_days = [ 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun' ]

def make_EOD(d):
    return d.replace(hour=20, minute=00, second=00, microsecond=0)

def int_or_zero(t):
    try:
        return int(t)
    except ValueError:
        return 0

def validate_hour(h):
    h = abs(int(h))
    if h > 24:
        h = 23
    return h

def validate_minute(m):
    m = abs(int(m))
    if m > 60:
       m = 59
    return m

def verbose_day_to_datetime(verbose):
    td_1 = datetime.timedelta(days=1)
    if verbose == 'today':
        parsed_date = datetime.datetime.now()
    elif verbose == 'tomorrow':
        parsed_date = datetime.datetime.now() + td_1
    elif verbose in verbose_days:
        parsed_date = date_parser.parse(verbose)
    else:
        raise Exception(verbose + ' is not a supported format. \nFormats supported: %s' % verbose_days)
    return make_EOD(parsed_date)

def parse_datetime(unparsed_datetime):
    '''
    unparsed_date:
        days:
            'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'today', 'tomorrow'
        time:
            HH:MM, ex: 12:30 (deadline is at 12:30)
        day-time:
            <days>-<time>, ex: mon-12:30 (deadline is on mon, 12:30)
    '''
    if unparsed_datetime.count('-') > 1 or unparsed_datetime.count(':') > 1:
        raise Exception('Unsupported format %s' % unparsed_datetime)

    if '-' in unparsed_datetime:
        try:
            day, time = unparsed_datetime.split('-')
        except ValueError:
            raise Exception('Unsupported format: %s' % unparsed_datetime)

        #parse time
        try:
            hour, minute = map(int_or_zero, time.split(':'))
        except ValueError:
            hour, minute = map(int_or_zero, time.split(':') + [0])
        
        hour, minute = validate_hour(hour), validate_minute(minute)
        
        #parse day
        parsed_day = verbose_day_to_datetime(day)
        parsed_datetime = parsed_day.replace(hour=hour, minute=minute)
    else:
        #parse hour
        if ':' not in unparsed_datetime:
            try:
                hour = int(unparsed_datetime)
                hour = validate_hour(hour)
                parsed_datetime = datetime.timedelta(hours=hour)
            except ValueError:
                parsed_datetime = verbose_day_to_datetime(unparsed_datetime)
        #parse hour with minutes
        else:
            hour, minute = map(int_or_zero, unparsed_datetime.split(':'))
            hour, minute = validate_hour(hour), validate_minute(minute)
            parsed_datetime = datetime.timedelta(hours=hour, minutes=minute)
    return parsed_datetime


if __name__ == '__main__':
    test_cases = ['12:30', '12', ':30', '12:', 'hi', 'bro',
                '2313', '0x232', 'mon-2', 'mon-12:30',
                'sun-12:5423', '12:232323', 'tue--2', '12::30'
                ] + verbose_days
    for test_case in test_cases:
        try:
            print(parse_datetime(test_case))
        except Exception as e:
            print(e)






