class Date:
    """represents a year, month, and day"""
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0

# TODO: Write make_date(year, month, day)
def make_date(year, month, day):
    d = Date()
    d.year = year
    d.month = month
    d.day = day
    return d

# TODO: Write print_date(date)
def print_date(date):
    print(f"{date.year}-{date.month}-{date.day}")

# TODO: Write print_date_tuple(date) -- return (year, month, day)
def print_date_tuple(date):
    return (date.year, date.month, date.day)

# TODO: Write is_after(d1, d2)
def is_after(d1, d2):
    return print_date_tuple(d1) > print_date_tuple(d2)

# ---- TEST CODE ----

d1 = make_date(1933, 6, 22)
d2 = make_date(1933, 9, 17)
print_date(d1)
print_date(d2)
print(is_after(d2, d1)) # should print True