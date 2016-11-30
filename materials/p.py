module_list = []

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
        ref_value = item[1]


        if ref_key == init_value:
            if "viper" in ref_value:
                print str(i) + "\t" + ref_key + " -> " + ref_value
                dive(counter)
        counter = counter + 1

dive(0)
