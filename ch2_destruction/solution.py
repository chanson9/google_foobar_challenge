"""Google foo.bar challenge 2 Gears of Destruction solution"""


def solution(pegs):
    """pegs represents the location of each peg along the support beam
    Your goal is to build a system where the last gear 
    rotates at twice the rate (in revolutions per minute, or rpm) of the first gear"""

#For example, if the pegs are placed at [4, 30, 50], 
# then the first gear could have a radius of 12, 
# the second gear could have a radius of 14, 
# and the last one a radius of 6. 
# Thus, the last gear would rotate twice as fast as the first one. 
# In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

# first calculate the possible sums of 2 numbers
# when added with the first gear placement which add up to the 2nd gear placement
# 4 + (12+14) = 30...we know 4 and 30.  find 12 + 14

    iPeg = 0
    radius_list = []
    # loop through all the pegs
    while iPeg < len(pegs) - 1:
        #create a list of numbers from 1 to half of the gear position.
        list_half = pegs[iPeg+1]/2
        x = 0
        radius_options = []
        seen = []
        while x < list_half:
            radius_options.append(x)
            x = x + 1

        # if we're on the first peg, get radius of pegs 1 & 2
        if iPeg == 0:
            for i in radius_options:
                if (pegs[iPeg+1] - pegs[iPeg] - i) in seen:
                    radius_list.append(pegs[iPeg+1] - pegs[iPeg] - i)  # radius 1
                    radius_list.append(i)  # radius 2
                    break
                else:
                    seen.append(i)
            iPeg = iPeg + 1
        # since we already know the 2nd radius, calculate up to n radius
        else:
            prev_radius = radius_list[iPeg]
            radius_list.append( pegs[iPeg+1] - (pegs[iPeg] +  prev_radius) )
            iPeg = iPeg + 1

    # ensure the last gear turns at twice the rpm of the first gear
    # calculate the difference between the first and last radius to check that it is double.
    radius_dif = radius_list[0] - radius_list[len(radius_list)-1]
    if radius_dif * 2 == radius_list[0]:
        # returns list of two positive integers representing the num and denom of the first gear's radius
        # stub out 1 for second value...figure that out later
        return [radius_list[0], 1]
    else:
        # returns list of -1, -1
        return [-1, -1]

def calc_rpm(input_radius):
    rpm = input_radius
    return rpm