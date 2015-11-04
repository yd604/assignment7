# Author: Yihong Du

from create_array import *
from divide_array import *
from generate_randArray import *
from mandelbrot import *

def main():
    # Question 1
    sol1 = create_array()
    print 'The 2-D array is \n', sol1.array
    print '\n'
    print 'The new array for question 1a is \n', sol1.picking_row()
    print '\n'
    print 'The new array for question 1b is \n', sol1.picking_column()
    print '\n'
    print 'The new array for question 1c is \n', sol1.picking_section()
    print '\n'
    print 'The new array for question 1d is \n', sol1.picking_range()
    print '\n'

    # Question 2
    print 'The array for question 2 is \n', divide_array()
    print '\n'

    # Question 3
    generate_randArray()
    print '\n'

    # Question 4
    candidate_set = mandelbrot(500)
    candidate_set.mandelbrot_iter()
    candidate_set.form_mask()
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
    except EOFError:
        print "EOFError"
    except OverflowError:
        print "OverflowError"
    except ZeroDivisionError:
        print "ZeroDivisionError"
    except TypeError:
        print "TypeError"