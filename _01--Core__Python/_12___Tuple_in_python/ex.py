def medium_range_tuple(t):
    if not t:
        return None 
    min_val = min(t)
    max_val = max(t)
    
    return (min_val + max_val) / 2
t = (10, 20, 30, 40, 50)
result = medium_range_tuple(t)
print("Medium Range:", result)