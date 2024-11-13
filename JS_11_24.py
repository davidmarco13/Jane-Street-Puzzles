import numpy as np

def closest_side(point, L=1):
    x, y = point
    distances = [x, L - x, y, L - y]
    closest = np.argmin(distances)
    return closest

def perpendicular_bisector_intersection(red, blue, closest_side, L=1):
    x_red, y_red = red
    x_blue, y_blue = blue

    midpoint = ((x_red + x_blue) / 2, (y_red + y_blue) / 2)

    if x_blue != x_red:
        gradient = (y_red - y_blue) / (x_red - x_blue)
        perp_gradient = -1 / gradient
    else:
        perp_gradient = None

    # Calculate intersection point based on closest side
    if closest_side == 0:  # left side
        x = 0
        y = perp_gradient * (x - midpoint[0]) + midpoint[1] if perp_gradient is not None else midpoint[1]

    elif closest_side == 1:  # right side
        x = 1
        y = midpoint[1] + perp_gradient * (x - midpoint[0]) if perp_gradient is not None else midpoint[1]

    elif closest_side == 2:  # bottom side
        y = 0
        x = (y - midpoint[1]) / perp_gradient + midpoint[0] if perp_gradient is not None else midpoint[0]

    elif closest_side == 3:  # top side
        y = 1
        x = (y - midpoint[1]) / perp_gradient + midpoint[0] if perp_gradient is not None else midpoint[0]

    # Return the intersection point and whether it lies within the bounds of the side
    if closest_side in [0, 1]:  # left or right side
        return (x, y), (0 <= y <= L)
    else:  # top or bottom
        return (x, y), (0 <= x <= L)

def montecarlo_simulation(num_trials, L=1):
    success_count = 0

    for _ in range(num_trials):
        # Generate random points within the square
        blue_point = L * np.random.rand(2)
        red_point = L * np.random.rand(2)

        # Find closest side to blue point
        closest = closest_side(blue_point, L)

        # Find intersection of perpendicular bisector with the closest side
        intersection_point, is_on_side = perpendicular_bisector_intersection(red_point, blue_point, closest, L)

        if is_on_side:
            success_count += 1

    probability = success_count / num_trials
    return probability

# Run the simulation with 1 million trials
estimated_probability = montecarlo_simulation(99999999)
print(f"Estimated Probability: {estimated_probability:.10f}")











    
    

