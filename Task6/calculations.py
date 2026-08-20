# calculations module

def get_squares(num_list):
    """returns a list of squares for the given numbers."""
    try:
        return [x**2 for x in num_list]
    except TypeError as e:
        print(f"Error calculating squares: Please ensure all items in the list are numbers. Details: {e}")
        return []

def get_cubes(num_list):
    """returns a list of cubes for the given numbers."""
    try:
        return [x**3 for x in num_list]
    except TypeError as e:
        print(f"Error calculating cubes: Please ensure all items in the list are numbers. Details: {e}")
        return []