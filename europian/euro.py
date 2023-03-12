import math

# function to calculate the amount of paint required for a given wall
def paint_required(wall_type):
    if wall_type == "accent":
        return 1.5
    else:
        return 2.25

# function to calculate the time required to paint a given wall
def time_required(wall_type):
    if wall_type == "accent":
        return 2.5
    else:
        return 3.25

# function to calculate the total number of walls in a house
def total_walls(h, s, r):
    return (6*h) + (4*s) + (3*r)

# function to calculate the total amount of paint and time required to paint a house
def paint_house(h, s, r):
    total = total_walls(h, s, r)
    accent_qty = math.ceil((total/3)*1.0) * paint_required("accent")
    regular_qty = math.ceil((total/3)*2.0) * paint_required("regular")
    total_qty = accent_qty + regular_qty
    total_time = (math.ceil((total/3)*1.0) * time_required("accent")) + (math.ceil((total/3)*2.0) * time_required("regular"))
    return [total_time, round(accent_qty, 2), round(regular_qty, 2)]

# main function to take input and calculate the results for each township
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print("Case #{}:".format(i+1), end=" ")
        for j in range(n):
            h, s, r = map(int, input().split(','))
            result = paint_house(h, s, r)
            if j == n-1:
                print("{}, {}, {}".format(round(result[0], 2), result[1], result[2]))
            else:
                print("{}, {}, {}".format(round(result[0], 2), result[1], result[2]), end=" ")

if __name__ == "__main__":
    main()
