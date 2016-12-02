from colors import color

module_list = []
ordered_list = []

with open("d.txt") as f:
    for line in f:
        nline = line.strip('\n').split(',')
        caller = nline[0]
        callee = nline[1].strip()
        module_list.append([caller, callee])


# print module_list


def dive(i):
    root_caller = module_list[i][0].replace("'", "")
    root_callee = module_list[i][1].replace("'", "")

    counter = 0

    for item in module_list:
        ref_caller = item[0].replace("'", "")
        ref_callee = item[1].replace("'", "")

        if root_callee == ref_caller:
            if "viper" in ref_callee:
                ordered_list.append([ref_caller, ref_callee, 1])
                dive(counter)

            elif "modules" in ref_callee:
                ordered_list.append([ref_caller, ref_callee, 31])
                dive(counter)

        elif root_callee in ref_caller:
            if "viper" in ref_callee:
                ordered_list.append([ref_caller, ref_callee, 32])
            dive(counter)

        counter = counter + 1

dive(0)


# print ordered_call_list

# find dependencies

ordered_list_len = len(ordered_list)

for n in range(0, ordered_list_len):
    next_item_index = n + 1
    if next_item_index < ordered_list_len:
        root_callee = ordered_list[n][1]
        next_caller = ordered_list[n+1][0]
        if root_callee == next_caller:
            # make next_caller's color code 33
            ordered_list[n+1][2] = 33


# print ordered_list

for n in range(0, ordered_list_len):
    color_code = ordered_list[n][2]
    connection_found = 33
    packages_found = 32
    lower_bound = 0
    callee_to_inspect = n - 2

    caller = ordered_list[n][0]
    callee = ordered_list[n][1]
    previous_2_callee = ordered_list[n-2][1]

    connection = "\t\t\t-> " + callee
    packages = "\t\t" + caller + "\n\t\t\t-> " + callee
    another_dep_found = "\t\t\t[d] " + caller + "\n\t\t\t-> " + callee
    normal = caller + "\n\t-> " + callee

    if color_code == connection_found:
        print color(connection, color_code)
    elif color_code == packages_found:
        print " o " + color(packages, color_code)
    else:
        # look for other dependencies in the same module
        # in viper, same module appears at previous 2 callee
        if callee_to_inspect > lower_bound:
            if caller == previous_2_callee:
                print color(another_dep_found, color_code)
            else:
                print color(normal, color_code)
        else:
            print color(normal, color_code)
