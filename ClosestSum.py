def closest_sum(arry1, arry2, target):
    i = 0
    j = len(arry2) - 1
    arry1_sorted = sorted(arry1)
    arry2_sorted = sorted(arry2)
    smallest_difference = abs(arry1_sorted[0] + arry2_sorted[0] - target)
    closest_pair = (arry1_sorted[0], arry2_sorted[0])
    while i < len(arry1_sorted) and j >= 0:
        current_difference = arry1_sorted[i] + arry2_sorted[j] - target
        if abs(current_difference) < smallest_difference:
            smallest_difference = abs(current_difference)
            closest_pair = (arry1_sorted[i], arry2_sorted[j])
        
        if current_difference == 0:
            return closest_pair
        elif current_difference < 0:
            i += 1
        else:
            j -= 1
    return closest_pair