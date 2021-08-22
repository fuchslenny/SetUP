import os


#just writes the info to the file
def write_info(content):
    filename = "_info_"

    try:
        counter = 1

        while os.path.exists(filename + ".txt"):
            filename = filename + str(counter)
            counter += 1

        out_file = open(filename + ".txt", "w")

        for i in content:
            now = str(i).replace("[", "").replace("]", "").replace("'", "").strip()
            out_file.write(now)

        #after writing just check if it worked
        out_file_check = open(filename + ".txt", "r")
        if out_file_check.readlines() is not None:
            out_file_check.close()

        else:
            print("Could not write Data to File")
            out_file.close()

    except Exception as e:
        print(e)


def configure():
    configure_arr = [True, True, True, True, True]

    input_str = input()
    strng = input_str.replace(" ", "").split(",")

    if len(strng) == 5:
        for i in strng:
            for j in configure_arr:
                if i == "t" or "T":
                    configure_arr[j] = True
                elif i == "f" or "F":
                    configure_arr[j] = False
                else:
                    print("Wrong input please try again")
                    configure()
    else:
        print("Your input is to long or to short please try again")
        configure()

    return configure_arr
