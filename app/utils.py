from toolz import first, last
import os


def has_next_day(dates_dict, year, month, day):
    '''Return next day found in nested dates_dict
    or None if can't find one.'''
    # Check current month for next days
    days = sorted(dates_dict[year][month].keys())
    if day != last(days):
        di = days.index(day)
        next_day = days[di+1]
        return({'year': year, 'month': month, 'day': next_day})
    # dates_dict[year][month][next_day])

    # Check current year for next months
    months = sorted(dates_dict[year].keys())
    if month != last(months):
        mi = months.index(month)
        next_month = months[mi+1]
        next_day = first(sorted(dates_dict[year][next_month].keys()))
        return({'year': year, 'month': next_month, 'day': next_day})

    # Check for next years
    years = sorted(dates_dict.keys())
    if year != last(years):
        yi = years.index(year)
        next_year = years[yi+1]
        next_month = first(sorted(dates_dict[next_year].keys()))
        next_day = first(sorted(dates_dict[next_year][next_month].keys()))
        return({'year': next_year, 'month': next_month, 'day': next_day})
    return False


def has_previous_day(dates_dict, year, month, day):
    '''Return previous day found in nested dates_dict
    or None if can't find one.'''
    days = sorted(dates_dict[year][month].keys())
    # Check current month
    if day != first(days):
        di = days.index(day)
        prev_day = days[di-1]
        return({'year': year, 'month': month, 'day': prev_day})

    # Check current year
    months = sorted(dates_dict[year].keys())
    if month != first(months):
        mi = months.index(month)
        prev_month = months[mi-1]
        last_day = last(sorted(dates_dict[year][prev_month].keys()))
        return({'year': year, 'month': prev_month, 'day': last_day})

    # Check other years
    years = sorted(dates_dict.keys())
    if year != first(years):
        yi = years.index(year)
        prev_year = years[yi-1]
        prev_month = last(sorted(dates_dict[prev_year].keys()))
        last_day = last(sorted(dates_dict[prev_year][prev_month].keys()))
        return({'year': prev_year, 'month': prev_month, 'day': last_day})

    return False


def get_env(x):
    res = os.environ.get(x)
    if res is not None:
        print("Found env var " + x + " " + res)
        return res
    else:
        print("Env var " + x + " not found")
        return None
