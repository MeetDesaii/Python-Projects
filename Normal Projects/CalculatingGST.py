# Calculating tax by adding 18% GST and returned as formatted string!

def calculate_gst(price):
    price_with_tax = price * 1.18  # This calculating 18% GST
    """
    The formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot.
    """
    return "Base price: {:.2f}. Price with including tax: {:.2f}".format(price, price_with_tax)


print(calculate_gst(200))
print(calculate_gst(50000))
