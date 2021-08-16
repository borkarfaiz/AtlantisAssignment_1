import re

def floor_and_direction(position):
    """
    splits the position into floor and direction
    """
    if position.endswith(("U", "D")):
        return int(position[:-1]), position[-1]
    return int(position), None

def find_difference(lift_position, request_floor, request_direction, number_of_floors):
    """
    finds how much lift needs to travel to reach the destination
    """
    lift_floor, lift_direction = floor_and_direction(lift_position)
    if lift_direction is None:
        difference = abs(lift_floor - request_floor)
    elif request_direction == "U":
        if lift_direction == "U":
            difference = request_floor - lift_floor if lift_floor <= request_floor else (number_of_floors - lift_floor) + (number_of_floors - request_floor)
        else:
            difference = abs(request_floor) + abs(lift_floor)
    elif lift_direction == "D":
        difference = lift_floor - request_floor if lift_floor >= request_floor else lift_floor + request_floor
    else:
        difference = abs(number_of_floors - lift_floor) + abs(number_of_floors - request_floor)
    return difference


def find_optimal_lift(lift_positions, request, number_of_floors):
    """
    finds the 
    """
    request_floor, request_direction = floor_and_direction(request)
    optimal = find_difference(lift_positions[0], request_floor, request_direction, number_of_floors)
    optimal_index = 0
    for index in range(1, len(lift_positions)):
        difference = find_difference(lift_positions[index], request_floor, request_direction, number_of_floors)
        if difference < optimal:
            optimal = difference
            optimal_index = index
    return f"Lift #{optimal_index+1} will be coming up to receive you"


if __name__ == '__main__':
    lift_positions = ["0", "1D", "12", "4U", "19D"]
    number_of_floors = 20
    request = input("Enter a Request ").strip()
    request_expression = re.compile("\d+(U|D)")
    if not request_expression.fullmatch(request):
        request = input("Enter a Request").strip()
    print(find_optimal_lift(lift_positions, request, number_of_floors))