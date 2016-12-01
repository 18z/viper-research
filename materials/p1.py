from colors import color

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

    init_key = module_list[i][0]
    init_value = module_list[i][1]

    # print init_key + " -> " + init_value

    counter = 0
    for item in module_list:
        ref_key = item[0]
        # ref_key = item[0]
        ref_value = item[1]

        if init_value == ref_key:
            if "viper" in ref_value:
                # print color(str(i) + "\t" + ref_key + "->" + ref_value, i)
                # print str(i) + "\t" + ref_key + "->" + ref_value
                ordered_call_list.append(
                    [ref_key.replace("'", ""), ref_value.replace("'", ""), 1])
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
        print "\t" + color(ordered_call_list[n][1], ordered_call_list[n][2])
    else:
        print color(ordered_call_list[n], ordered_call_list[n][2])
