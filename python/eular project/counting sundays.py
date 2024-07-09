import datetime


class CountingSundays:
    def __init__(self):
        self.date_start = datetime.date.fromisoformat('1901-01-01')
        self.date_end = datetime.date.fromisoformat('2000-12-31')

    def dates(self):
        dates = set()
        current_date = self.date_start
        while current_date <= self.date_end:
            dates.add(current_date)
            current_date += datetime.timedelta(days=1)
        return list(dates)

    def the_main(self):
        number_of_sundays = 0

        instance = CountingSundays()
        leap_years = 0
        for date in instance.dates():
            if date.isoweekday() == 6:
                if date.month == 1:
                    if 1901 <= date.year <= 2000:
                        number_of_sundays += 1
        for date in instance.dates():
            if date.year % 400 == 0:
                if date.month == 1:
                    if date.isoweekday() == 6:

                        leap_years += 1
        print(leap_years)

        print(number_of_sundays)



def main():
    pass



if __name__ == '__main__':
    main()
