# Network Layer Proxy RTM Game / Random Result Creator
# Lubut Ride Too Moon V.0.4
# Created: 2023.05.10
# Creator: LBT CRYPT
#############
import random

def generateX():
    category = random.choice(["small", "medium", "large"])

    if category == "small":
        start, end = 1.01, 10.00
    elif category == "medium":
        start, end = 10.01, 100.00
    else:  # "large"
        start, end = 100.01, 1000.00
    possible_values = [start + i * 0.01 for i in range(int((end - start) * 100) + 1)]
    return random.choice(possible_values)

for _ in range(1): # Create Only 1 result
    print(generateX())
