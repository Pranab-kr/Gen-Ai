# You're creating a monthly report for a cafe's sales.
# Instead of putting all logic in one place, break it down.
# Task:
# * Write a function generate_report() that calls:
# « fetch_sales()
# « filter_valid_orders()
# + summarize_data()


def fetch_sales():
    print("Fetching the sales data!")


def filter_valied_sales():
    print("Filtering valid sales data!")


def summerize_data():
    print("Summerizeing the sales data!")


def generate_report():
    fetch_sales()
    filter_valied_sales()
    summerize_data()
    print("Report is Ready!")


generate_report()
