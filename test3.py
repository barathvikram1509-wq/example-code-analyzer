def process_data(vals=[]):
    vals.append(sum(vals))
    for i in range(len(vals)):
        print("Val " + str(i) + ": " + str(vals[i]))
        try:
            res = 100 / vals[i]
            if isinstance(res, int):
                return "High"
        except ZeroDivisionError:
            print("Cannot divide by zero")
