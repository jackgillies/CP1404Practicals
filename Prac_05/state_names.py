
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}
print(STATE_NAMES)

states = input("Enter short state: ").upper()
while states != "":
    if states in STATE_NAMES:
        print(states, "is", STATE_NAMES[states])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
