"""Google foo.bar challenge 2 Gearing Up For Destruction solution"""

# The list pegs will be given sorted in ascending order and 
# will contain at least 2 and no more than 20 distinct positive integers, 
# all between 1 and 10000 inclusive.

from fractions import Fraction  

"""pegs represents the location of each peg along the support beam
    Your goal is to build a system where the last gear 
    rotates at twice the rate (in revolutions per minute, or rpm) of the first gear"""
def solution(pegs):
    # if no list is found or there is only 1 peg, return [-1, -1]
    if ((not pegs) or len(pegs) == 1):
        return [-1,-1]

    # the solution is different if there are an even or odd # of pegs
    even = False
    if (len(pegs)%2==0):
        even = True

    # grab the # of pegs
    num_pegs = len(pegs)
    first_radius = Fraction(0)

    # since the last gear spins at twice the rpm: that's the 2*r1
    # the equation to find the radius based on 2 pegs is P1 - (P0 / R1) = 2R1
    # by reducing this further, we get P1 - P0 = 3R1
    # therefore the radius of the last peg (R1) is R1 = P1-P0 / 3
    # the radius of the first peg is twice R1, which is 2*R1
    # we have different solutions depending on whether there are an even or odd # pegs
    if even:
        distance = calcDistance(num_pegs, pegs, even)
        first_radius = Fraction(2 * (float(distance)/3)).limit_denominator()
    else:
        distance = calcDistance(num_pegs, pegs, even)
        first_radius = Fraction(2 * distance).limit_denominator()

    # all radii have to be greater than 1, so make sure the first radius is >=2
    if first_radius < 2:
        return [-1,-1]

    current_radius = first_radius
    for iPeg in range(0, num_pegs-2):
        center_dist = pegs[iPeg+1] - pegs[iPeg]
        next_radius = center_dist - current_radius
        if (current_radius < 1 or next_radius < 1):
            return [-1,-1]
        else:
            current_radius = next_radius

    # return numerator and denominator of the first radius
    return [first_radius.numerator, first_radius.denominator]

""" calculate the distance between pegs for input to radius calculation """
def calcDistance(num_pegs, pegs, even):
    # if it's even, just take the total distance between last and first pegs
    if even:
        dist = pegs[num_pegs - 1] - pegs[0]
    # if it's odd, take the negative total of distance between first and last pegs
    else:
        dist = (- pegs[0] - pegs[num_pegs - 1]) 

    # if we have more than 2 pegs, iterate over the remaining pegs computing the distance
    if (num_pegs > 2):
        for iPeg in range(1, num_pegs-1):
            dist += 2 * (-1)**(iPeg+1) * pegs[iPeg]
    
    return dist
