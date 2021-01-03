
#just writes the info to the file
def write_info(content):

    try:
        out_file = open("_info_", "rw")
        out_file.write(content)
        #after writing just check if it worked
        if out_file.readlines() is not None:
            out_file.close()

        else:
            print("Could not write Data to File")

    except Exception as e:
        print(e)