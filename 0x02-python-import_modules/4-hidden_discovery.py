#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    str = dir(hidden_4)
    for i in range(0, len(str)):
        if str[i].startswith("__") is False:
            print("{}".format(str[i]))
