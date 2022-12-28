def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0
    actions = []

    location_input = input("Enter Location of Vacuum: ")
    status_input = input("Enter status of " + location_input + ": ")
    status_input_complement = input("Enter status of other room: ")
    print("Initial Location Condition" + str(goal_state))
    if location_input == 'A':
        location_complement = 'B'
    else:
        location_complement = 'A'
    if status_input == '1':
        actions.append("Suck at Location "+location_input)
        goal_state[location_input] = '0'
        cost += 1 
        actions.append("Move to Location "+location_complement)

        if status_input_complement == '1':
            cost += 1
            actions.append("Suck at Location "+location_complement)
            goal_state[location_complement] = '0'
            cost += 1

    if status_input == '0':
        actions.append("Move to Location "+location_complement)
        if status_input_complement == '1':
            actions.append("Suck at Location "+location_complement)
            cost += 1
            goal_state[location_complement] = '0'
            cost += 1

    print("GOAL STATE: ")
    print(goal_state)
    print("Actions Taken are: ")
    for var in actions:
        print(var)
    print("Performance Measurement: " + str(cost))


vacuum_world()