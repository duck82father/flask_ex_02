def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)

def format_date(value, fmt='%Y년 %m월 %d일'):
    return value.strftime(fmt)

def format_time(value, fmt='%p %I:%M'):
    return value.strftime(fmt)