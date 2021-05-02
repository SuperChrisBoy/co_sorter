def cleaner(logfile):
    cleaned_list = []
    for x in range(0, len(logfile)):
        split_word = logfile[x].split(" ")
        for y in range(0, len(split_word)):
            if "§" in split_word[y]:
                char_list = list(split_word[y])
                for i in range(0, len(char_list)):
                    if char_list[i] == "§":
                        del char_list[i]
                        del char_list[i]
                        break
                fill_str = ""
                split_word[y] = fill_str.join(char_list)

            if y == 8:
                if "x" in split_word[y]:
                    split_word[y] = split_word[y].replace("x", "", 1)

        space = " "
        cleaned_list.append(space.join(split_word))

    return cleaned_list

def chest_sorter(logfile, logname):
    co_commands = []

    for i in range(0, len(logfile)):
        split_list = logfile[i].split(" ")
        if "ago" in split_list:
            co_commands.append(logfile[i])

    ordered_list = []
    for j in range(len(co_commands), 0, -1):
        ordered_list.append(co_commands[j - 1])
    
    name_split = logname.split(".")
    write_to_file = open(name_split[0] + "_sorted." + name_split[1], "w", encoding='utf-8')
    str1 = "\n"
    write_to_file.write(str1.join(ordered_list))
    write_to_file.close()

    return ordered_list

def item_counter(ordered_list, logname):
    item_names = []
    result_num = 0
    action = ""
    index = 0
    for x in range(0, len(ordered_list)):
        split_word = ordered_list[x].split(" ")
        for y in range(0, len(split_word)):
            split_word[-1] = split_word[-1].replace(".", "", 1)
            action_num = int(split_word[8])
            action = split_word[7]
            if split_word[-1] not in item_names:
                item_names.append(split_word[-1])
                item_names.append("0")
            index = item_names.index(split_word[-1])
        cur_num = int(item_names[index+1])
        if action == "added":
            result_num = cur_num + action_num
        elif action == "removed":
            result_num = cur_num - action_num
        item_names[index+1] = str(result_num)

    item_cur_in_chest = []
    item_past_in_chest = []
    item_negative_in_chest = []
    item_content = ""
    for i in range(0, len(item_names), 2):
        item_content = str(item_names[i]) + ":" + " " + str(item_names[i + 1])
        if int(item_names[i + 1]) > 0:
            item_cur_in_chest.append(item_content)
        elif int(item_names[i + 1]) == 0:
            item_past_in_chest.append(item_content)
        elif int(item_names[i + 1]) < 0:
            item_negative_in_chest.append(item_content)

    name_split = logname.split(".")
    write_to_file2 = open(name_split[0] + "_estimated_contents." + name_split[1], "w", encoding='utf-8')
    str1 = "\n"

    write_to_file2.write("\n------- Items currently in the chest -------\n\n")
    write_to_file2.write(str1.join(item_cur_in_chest))
    write_to_file2.write("\n\n------- Items used to be in the chest -------\n\n")
    write_to_file2.write(str1.join(item_past_in_chest))
    write_to_file2.write("\n\n------- Items might be duplicated from the chest -------\n\n")
    write_to_file2.write(str1.join(item_negative_in_chest))

    write_to_file2.close()

def main():
    print("v1.1")
    print("Epic chest sorter program by XxSlayerMCxX.\n")
    print("Put this program in a folder where you want to sort coreprotect logs. \nBe sure that your log files should be in the same folder.\n")
    print("Note: This program only sorts coreprotect chest logs and is EXPERIMENTAL. \nUse this when verifying refunds but don't fully trust the estimated number of chest items.\n")

    while (True):
        logname = input("Enter coreprotect log file name (include filename extension) or exit (enter \"exit\"): ")

        if logname == "exit":
            break
 
        try:
            fp = open(logname, 'r', encoding='utf-8')
            logfile = fp.read().split('\n')
            fp.close()
        except IOError:
            print("File not found!\n")
            continue

        ordered_list = chest_sorter(cleaner(logfile), logname)
        item_list = item_counter(ordered_list, logname)
        print("Completed!\n")

if __name__ == "__main__":
    main()