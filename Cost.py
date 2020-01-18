def calculate_cost(temp, time, energy):
    result = 0
    cost = 0
    if 10 <= temp <= 50:
        if 7 <= time < 11:
            cost = 0.094
        elif 11 <= time < 17:
            cost = 0.134
        elif 17 <= time < 19:
            cost = 0.094
        elif 19 <= time <= 23:
            cost = 0.065
        elif 0 <= time < 7:
            cost = 0.065

    elif -50 <= temp < 10:
        if 7 <= time < 11:
            cost = 0.134
        elif 11 <= time < 17:
            cost = 0.094
        elif 17 <= time < 19:
            cost = 0.134
        elif 19 <= time <= 23:
            cost = 0.065
        elif 0 <= time < 7:
            cost = 0.065

    ts = energy['Solar'] * cost
    result += ts
    ns = energy['Nuclear'] * cost
    result += ns
    hs = energy['Hydro'] * cost
    result += hs
    gs = energy['Gas/oil'] * cost
    result += gs
    bs = energy['Biofuel'] * cost
    result += bs
    neis = energy['Neighboor'] * cost
    result += neis

    return result