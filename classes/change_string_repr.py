#!/usr/bin/env python3

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # '0' is the instance 'self'
        # alternative:
        # return 'Pair(%r, %r)' % (self.x, self.y)
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)






if __name__ == '__main__':
    main()

