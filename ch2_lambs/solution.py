"""Google foo.bar challenge 2 LAMBS payout solution"""


def solution(total_lambs):
    """total_lambs is the integer number of LAMBs you are trying to divide.
    It should return an integer which represents the difference between
    the minimum and maximum number of henchmen who can share the LAMBs"""

    if(total_lambs < 1):
        return 0

    if total_lambs > 10**9:
        return 0

    # if there was only 1 total lamb to distribute, just return 0
    if total_lambs == 1:
        return 0

    # calculate the stingy payout list using fibonacci
    generous_list = []
    hench_ctr1 = 0
    generous_sum = 0
    out_of_lambs = False
    while not out_of_lambs:
        payout = 2**hench_ctr1
        generous_sum = generous_sum + payout
        if generous_sum > total_lambs:
            out_of_lambs = True  # break out of the loop
            break
        generous_list.append(payout)  # add payout to the list
        hench_ctr1 = hench_ctr1 + 1

    # calculate the stingy payout
    stingy_list = [1, 1]
    stingy_sum = 2
    hench_ctr2 = 2
    out_of_lambs = False
    while not out_of_lambs:
        # calculate the next number in the fibonacci
        payout = stingy_list[hench_ctr2-1] + stingy_list[hench_ctr2-2]
        stingy_sum = stingy_sum + int(payout)
        if stingy_sum > total_lambs:
            out_of_lambs = True  # break out of the loop
            break
        stingy_list.append(payout)  # add payout to the list
        hench_ctr2 = hench_ctr2 + 1

    # return the difference between the length of lists
    return len(stingy_list) - len(generous_list)
