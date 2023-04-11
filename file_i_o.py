#!/usr/bin/python3

def main():
    #open files
    p1 = open("p1.txt", 'r')
    p2 = open("p2.txt", 'r')
    finished = open("finished.txt", "w")

    part1, part2 = list(), list()

    #read each line of the file
    for line in p1:
        part1.append(line)

    for line in p2:
        part2.append(line)
    for x, y in zip(part1, part2):
        print(x, file = finished, end = '')
        print(y, file = finished, end = '')
        
if __name__ == "__main__": main()