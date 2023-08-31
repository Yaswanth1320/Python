
# Water jug problem
# problem- Given the capacity of two jugs l1 and l2 measure g amount of water by using the rules

l1 = int(input("enter the capacity of jug 1 :"))
l2 = int(input("enter the capacity of jug 2 :"))
g = int(input("Amout of water you need :"))


def display():
    print("\nSelect the rule to be applied")
    print("Rule 1: Fill Jug 1")
    print("Rule 2: Fill Jug 2")
    print("Rule 3: Empty Jug 1")
    print("Rule 4: Empty Jug 2")
    print("Rule 5: Transfer all the water from jug 1 to jug 2")
    print("Rule 6: Transfer all the water from jug 2 to jug 1")
    print("Rule 7: Transfer some water from jug 1 to jug 2 until jug 2 is full")
    print("Rule 8: Transfer some water from jug 2 to jug 1 until jug 1 is full")


def apply_rule(rule, x, y):
    # rule 1: Fill the jug 1
    if (rule == 1):
        if x < l1:
            return l1, y
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 2: Fill the jug 2
    elif (rule == 2):
        if y < l2:
            return x, l2
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 3: Empty jug 1
    elif (rule == 3):
        if x > 0:
            return 0, y
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 4: Empty jug 2
    elif (rule == 4):
        if y > 0:
            return x, 0
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 5: Transfer all the water from jug 1 to jug 2
    elif (rule == 5):
        if x > 0 and x+y <= l2:
            return 0, x+y
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 6: Transfer all the water from jug 2 to jug 1
    elif (rule == 6):
        if y > 0 and x+y <= l1:
            return x+y, 0
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 7: Transfer some water from jug 1 to jug 2 until jug 2 is full
    elif (rule == 7):
        if x > 0 and x+y >= l2:
            return x-(l2-y), l2
        else:
            print("Rule cannot be applied")
            return x, y

    # rule 8: Transfer some water from jug 2 to jug 1 until jug 1 is full
    elif (rule == 8):
        if y > 0 and x+y >= l1:
            return l1, y-(l1-x)
        else:
            print("Rule cannot be applied")
            return x, y

    else:
        print("INVALID CHOICE")


# intilizing both l1 and l2 as empty intially

x = y = 0
while (True):
    if (x == g) or (y == g):
        print("Goal Acheived")
    else:
        display()
        rule = int(input("Enter the rule number : "))
        x, y = apply_rule(rule, x, y)
        print("\nStatus")
        print("CURRENT STATE :", end=" ")
        print(x, y)
