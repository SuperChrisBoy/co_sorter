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

        space = " "
        cleaned_list.append(space.join(split_word))

    return cleaned_list

def command_sorter(cleaned_list, logname):
    co_commands = []

    for i in range(0, len(cleaned_list)):
        splitlist = cleaned_list[i].split(" ")
        if "ago" in splitlist:
            co_commands.append(cleaned_list[i])

    print(len(co_commands))

    ordered_list = []
    for j in range(len(co_commands), 0, -1):
        ordered_list.append(co_commands[j-1])

    namesplit = logname.split(".")
    write_to_file = open(namesplit[0] + "_sorted." + namesplit[1], "w", encoding='utf-8')
    str1 = "\n"
    write_to_file.write(str1.join(ordered_list))
    write_to_file.close()

    return ordered_list

def main():
    print("v1.1")
    print("Epic command sorter program by XxSlayerMCxX.\n")
    print("Put this program in a folder where you want to sort coreprotect logs. \nBe sure that your log files should be in the same folder.\n")
    print("Note: This program only sorts coreprotect command logs.\n")

    while(True):
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

        cleaned_list = cleaner(logfile)
        ordered_list = command_sorter(cleaned_list, logname)

        print("Completed!\n")

if __name__ == "__main__":
    main()