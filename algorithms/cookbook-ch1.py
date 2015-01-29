#!/usr/bin/env python3


# 1.1
def unpack():
    values = (1, 2, 3, (4,5,6))
    a, b, c, d = values
    print(a == values[0])
    print(d[0] == values[3][0])

#1.2
def drop_first_last():
    grades = [1,2,3,4]
    first, *middle, last = grades
    head, *tail = grades
    print(head == grades[0])
    print(tail == grades[1:])
    print(middle == grades[1:-1])
    *head, tail = grades
    print(head == grades[0:-1])
    print(tail == grades[-1])
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')


if __name__ == '__main__':
    unpack()
    drop_first_last()
