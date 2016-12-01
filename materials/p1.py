import sys
from colors import color

# sys.setrecursionlimit(30000)

module_list = []
ordered_call_list = []
sushi = ""
# sushi = []

with open("d.txt") as f:
    for line in f:
        # print line
        nline = line.strip('\n').split(',')

        key = nline[0]
        value = nline[1].strip()

        module_list.append([key, value])


# print module_list


def dive(i):

    root_key = module_list[i][0].replace("'", "")
    root_value = module_list[i][1].replace("'", "")

    # print "root_value " + root_value
    # print init_key + " -> " + init_value

    counter = 0
    for item in module_list:
        ref_key = item[0].replace("'", "")
        ref_value = item[1].replace("'", "")

        if root_value == ref_key:
            if "viper" in ref_value:
                ordered_call_list.append([ref_key, ref_value, 1])
                dive(counter)
            elif "modules" in ref_value:
                ordered_call_list.append([ref_key, ref_value, 31])
                # print "modules found " + ref_key
                dive(counter)
        elif root_value in ref_key:
            if "viper" in ref_value:
                ordered_call_list.append([ref_key, ref_value, 32])
            dive(counter)

        counter = counter + 1

dive(0)


# print ordered_call_list

# find sushi connections
for n in range(0, len(ordered_call_list)):
    # print ordered_call_list[n]

    if n+1 < len(ordered_call_list):
        if ordered_call_list[n][1] == ordered_call_list[n+1][0]:
            # print color(ordered_call_list[n+1], 32)
            # ordered_call_list[n][2] = 33
            ordered_call_list[n+1][2] = 33


# print ordered_call_list

for n in range(0, len(ordered_call_list)):
    if ordered_call_list[n][2] == 33:
        # if connection found
        # print "\t-> " + color(ordered_call_list[n][1],
        # ordered_call_list[n][2])
        print "\t\t\t-> " + color(ordered_call_list[n][1], ordered_call_list[n][2])
    elif ordered_call_list[n][2] == 32:
        msg = "\t\t" + ordered_call_list[n][0] + "\n\t\t\t-> " + ordered_call_list[n][1]
        print " o " + color(msg, ordered_call_list[n][2])
    else:
        # print all
        if n-2 > 0:
            if ordered_call_list[n][0] == ordered_call_list[n-2][1]:
                msg = "\t\t\t[e] " + ordered_call_list[n][0] + "\n\t\t\t-> " + ordered_call_list[n][1]
                print color(msg, ordered_call_list[n][2])
            else:
                msg = ordered_call_list[n][0] + "\n\t-> " + ordered_call_list[n][1]
                print color(msg, ordered_call_list[n][2])
