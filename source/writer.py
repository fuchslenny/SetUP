
#just writes the info to the file
def write_info(content):

    try:
        out_file = open("_info_", "w")
        out_file.write(content)
        out_file.close()

    except Exception as e:
        print(e)