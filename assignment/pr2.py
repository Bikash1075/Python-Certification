# problem 2 string_split and join
def split_and_join(line):
    # l= line.split(" ")
    s="-".join(line.split(" "))
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)