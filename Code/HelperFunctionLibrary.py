import math

def GetCoordinatesForTime(hour, minute):
    es = [(0, 0), (0, 1)]
    ist = [(0, 3), (0, 4), (0, 5)]
    fuenf = [(0, 7), (0, 8), (0, 9), (0, 10)]
    zehn = [(1, 0), (1, 1), (1, 2), (1, 3)]
    vor = [(1, 8), (1, 9), (1, 10)]
    # drei = [(2, 0), (2, 1), (2,2)]
    viertel = [(2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10)]
    dreiviertel = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                   (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10)]
    nach = [(3, 1), (3, 2), (3, 3), (3, 4)]
    halb = [(3, 7), (3, 8), (3, 9), (3, 10)]

    hours = {
        1: [(9, 4), (9, 5), (9, 6), (9, 7)],
        2: [(5, 0), (5, 1), (5, 2), (5, 3)],
        3: [(4, 4), (4, 5), (4, 6), (4, 7)],
        4: [(7, 0), (7, 1), (7, 2), (7, 3)],
        5: [(5, 7), (5, 8), (5, 9), (5, 10)],
        6: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4)],
        7: [(8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10)],
        8: [(4, 0), (4, 1), (4, 2), (4, 3)],
        9: [(9, 0), (9, 1), (9, 2), (9, 3)],
        10: [(6, 6), (6, 7), (6, 8), (6, 9)],
        11: [(4, 8), (4, 9), (4, 10)],
        12: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)]
    }

    full_hours = {
        1: [(7, 8), (7, 9), (7, 10)],
        2: [(5, 0), (5, 1), (5, 2), (5, 3)],
        3: [(4, 4), (4, 5), (4, 6), (4, 7)],
        4: [(7, 0), (7, 1), (7, 2), (7, 3)],
        5: [(5, 7), (5, 8), (5, 9), (5, 10)],
        6: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4)],
        7: [(8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10)],
        8: [(4, 0), (4, 1), (4, 2), (4, 3)],
        9: [(9, 0), (9, 1), (9, 2), (9, 3)],
        10: [(6, 6), (6, 7), (6, 8), (6, 9)],
        11: [(4, 8), (4, 9), (4, 10)],
        12: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)]
    }

    uhr = [(9, 8), (9, 9), (9, 10)]

    m1 = [(10, 0)]
    m2 = [(10, 0), (10, 1)]
    m3 = [(10, 0), (10, 1), (10, 2)]
    m4 = [(10, 0), (10, 1), (10, 2), (10, 3)]

    coordinates = []

    coordinates += es
    coordinates += ist

    minutes_offset = minute % 5
    if minutes_offset == 1:
        coordinates += m1
    elif minutes_offset == 2:
        coordinates += m2
    elif minutes_offset == 3:
        coordinates += m3
    elif minutes_offset == 4:
        coordinates += m4

    minutes_five = minute - minutes_offset
    displayHour = hour
    if minutes_five == 5:
        coordinates += fuenf + nach
    elif minutes_five == 10:
        coordinates += zehn + nach
    elif minutes_five == 15:
        coordinates += viertel + nach
    elif minutes_five == 20:
        coordinates += zehn + vor + halb
        displayHour += 1
    elif minutes_five == 25:
        coordinates += fuenf + vor + halb
        displayHour += 1
    elif minutes_five == 30:
        coordinates += halb
        displayHour += 1
    elif minutes_five == 35:
        coordinates += fuenf + nach + halb
        displayHour += 1
    elif minutes_five == 40:
        coordinates += zehn + nach + halb
        displayHour += 1
    elif minutes_five == 45:
        coordinates += dreiviertel
        displayHour += 1
    elif minutes_five == 50:
        coordinates += zehn + vor
        displayHour += 1
    elif minutes_five == 55:
        coordinates += fuenf + vor
        displayHour += 1

    displayHour %= 12
    if displayHour == 0:
        displayHour = 12

    if minutes_five == 0:
        coordinates += full_hours[displayHour] + uhr
    else:
        coordinates += hours[displayHour]

    return coordinates
    # return es+ist+fuenf_part+zehn_part+vor+drei_part+dreiviertel+nach+halb


def GetCoordinatesForSeconds(seconds):
    tens = {
        0: [(1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 1), (4, 4), (5, 1), (5, 4), (6, 1), (6, 4), (7, 2), (7, 3)],
        1: [(1, 3), (2, 2), (2, 3), (3, 1), (3, 3), (4, 3), (5, 3), (6, 3), (7, 2), (7, 3), (7, 4)],
        2: [(1, 2), (1, 3), (2, 1), (2, 4), (3, 4), (4, 3), (5, 2), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4)],
        3: [(1, 2), (1, 3), (2, 1), (2, 4), (3, 4), (4, 2), (4, 3), (5, 4), (6, 1), (6, 4), (7, 2), (7, 3)],
        4: [(1, 1), (2, 1), (3, 1), (3, 3), (4, 1), (4, 3), (5, 1), (5, 2), (5, 3), (5, 4), (6, 3), (7, 3)],
        5: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 4), (6, 4), (7, 1), (7, 2), (7, 3)]
    }
    ones = {
        0: [(1, 7), (1, 8), (2, 6), (2, 9), (3, 6), (3, 9), (4, 6), (4, 9), (5, 6), (5, 9), (6, 6), (6, 9), (7, 7), (7, 8)],
        1: [(1, 8), (2, 7), (2, 8), (3, 6), (3, 8), (4, 8), (5, 8), (6, 8), (7, 7), (7, 8), (7, 9)],
        2: [(1, 7), (1, 8), (2, 6), (2, 9), (3, 9), (4, 8), (5, 7), (6, 6), (7, 6), (7, 7), (7, 8), (7, 9)],
        3: [(1, 7), (1, 8), (2, 6), (2, 9), (3, 9), (4, 7), (4, 8), (5, 9), (6, 6), (6, 9), (7, 7), (7, 8)],
        4: [(1, 6), (2, 6), (3, 6), (3, 8), (4, 6), (4, 8), (5, 6), (5, 7), (5, 8), (5, 9), (6, 8), (7, 8)],
        5: [(1, 6), (1, 7), (1, 8), (1, 9), (2, 6), (3, 6), (4, 6), (4, 7), (4, 8), (5, 9), (6, 9), (7, 6), (7, 7), (7, 8)],
        6: [(1, 7), (1, 8), (2, 6), (2, 9), (3, 6), (4, 6), (4, 7), (4, 8), (5, 6), (5, 9), (6, 6), (6, 9), (7, 7), (7, 8)],
        7: [(1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 8), (4, 8), (5, 7), (6, 7), (7, 7)],
        8: [(1, 7), (1, 8), (2, 6), (2, 9), (3, 6), (3, 9), (4, 7), (4, 8), (5, 6), (5, 9), (6, 6), (6, 9), (7, 7), (7, 8)],
        9: [(1, 7), (1, 8), (2, 6), (2, 9), (3, 6), (3, 9), (4, 7), (4, 8), (4, 9), (5, 9), (6, 6), (6, 9), (7, 7), (7, 8)]
    }

    return tens[math.floor(seconds / 10)] + ones[seconds % 10]

def GetSpiralCoordinates():
    spiral = []

    for i in range(0, 11):
        spiral.append((0, i))
    for i in range(1, 10):
        spiral.append((i, 10))
    for i in range(9, -1, -1):
        spiral.append((9, i))
    for i in range(8, 0, -1):
        spiral.append((i, 0))

    for i in range(1, 10):
        spiral.append((1, i))
    for i in range(2, 9):
        spiral.append((i, 9))
    for i in range(8, 0, -1):
        spiral.append((8, i))
    for i in range(7, 1, -1):
        spiral.append((i, 1))    

    for i in range(2, 9):
        spiral.append((2, i))
    for i in range(3, 8):
        spiral.append((i, 8))
    for i in range(7, 1, -1):
        spiral.append((7, i))
    for i in range(6, 2, -1):
        spiral.append((i, 2))   

    for i in range(3, 8):
        spiral.append((3, i))
    for i in range(4, 7):
        spiral.append((i, 7))
    for i in range(6, 2, -1):
        spiral.append((6, i))
    for i in range(5, 3, -1):
        spiral.append((i, 3))    

    spiral.append((4, 4))
    spiral.append((4, 5))
    spiral.append((4, 6))
    spiral.append((5, 6))
    spiral.append((5, 5))
    spiral.append((5, 4))

    return spiral

def GetDotCoordinates(numDots=4):
    dots = []
    if numDots >= 1:
        dots.append((10, 0))
    if numDots >= 2:
        dots.append((10, 1))
    if numDots >= 3:
        dots.append((10, 2))
    if numDots >= 4:
        dots.append((10, 3))
    
    return dots

def GetWatermarkCoordinates():
    made = [(1, 4), (1, 5), (1, 6), (1, 7)]
    by = [(3, 5), (3, 6)]
    flo = [(5, 4), (5, 5), (5, 6)]
    rett = [(7, 4), (7, 5), (7, 6), (7, 7)]

    return made + by + flo + rett

def GetRainbowColor(posIn):
    # Input a value 0 to 767 to get a color value.
    # The colours are a transition r - g - b - back to r.
    pos = int(posIn % 768)

    # 0 - 255: r> g< b0
    # 256 - 511: r0 g> b<
    # 512 - 767: r< g0 b>

    # r = pos + 768 - 512

    if pos < 256:
        r = 255 - pos
        g = pos
        b = 0
    elif pos < 512:
        r = 0
        g = 511 - pos
        b = pos - 256
    else:
        r = pos - 512
        g = 0
        b = 767 - pos

    return (r, g, b)