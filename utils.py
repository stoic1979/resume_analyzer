#
# script for utility/helper functions
#


def flog(msg):
    """
    utility func to write/append a msg to logs.txt file
    """
    f = open("logs.txt", "a")
    f.write(msg)
    f.write("\n")
    f.close()

if __name__ == "__main__":
    flog("log some msg")
