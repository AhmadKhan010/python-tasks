import argparse
import math

try:
    # set up argparse to handle our command-line inputs
    parser = argparse.ArgumentParser(description="This script calculates the distance between two point (x1,y1) and (x2,y2)")

    # add the arguments rules
    parser.add_argument("x1", type=float, help="X cosrdinate of first point")
    parser.add_argument("y1", type=float, help="Y coordinate of first point")
    parser.add_argument("x2", type=float, help="X coordinate of second point")
    parser.add_argument("y2", type=float, help="Y coordinate of second point")

    # parse the arguments from terminal
    arg = parser.parse_args()

    # calculate distance using distance formula
    distance = math.sqrt(((arg.x2 - arg.x1)**2) + ((arg.y2 - arg.y1)**2))

    # print the points and final distance
    print(f"Point 1: ({arg.x1}, {arg.y1})")
    print(f"Point 1: ({arg.x2}, {arg.y2})")
    print(f"Distance between P1 and P2: {distance:.2f}")

# if any error occured, except will caught it
except Exception as e:
    print(f"An unexpected error occurred: {e}")