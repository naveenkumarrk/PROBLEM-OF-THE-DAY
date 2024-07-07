n = 3
time = 2

# using mathematical formula
def cycles_pillow(n, time):
    cycle = 2 * (n-1)
    position = time % cycle

    if position < n:
        return (position + 1)
    else:
        return (2 * n - position - 1 )


def pillow_problem(n, time):
    is_left_to_right = True
    pos = 1
    for i in range(1, n+1):
        if is_left_to_right:
            pos += 1
        else:
            pos -= 1
        if i % (n-1) == 0:
            is_left_to_right = not is_left_to_right
    return pos


def isForward_pillow(n, time):
    position = 1
    isForward = True

    while time > 0:
        if isForward:
            position += 1
            if position == n:
                isForward = False
        else:
            position -=1 
            if position == 1:
                isForward = True
        time -= 1

    return position