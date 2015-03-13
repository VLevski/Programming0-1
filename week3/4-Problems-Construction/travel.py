def travel_cost(travels):
    cost = 0

    for travel in travels:
        if travel > 23:
            cost += 23
        else:
            cost += travel

    if cost > 50:
        cost = 50

    return cost
