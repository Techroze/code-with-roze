# a function which takes effect at starting point of my program
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_sign = d.replace("$", "")
    return float(d_sign)

def percent_to_float(p):
    p_sign = p.replace("%", "")
    p_converted = float(p_sign) / 100
    return p_converted



main()