def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Access the element; may raise IndexError if i >= len(my_list)
            element = my_list[i]
            # Try to format and print as integer
            print("{:d}".format(element), end="")
            count += 1
        except IndexError:
            # Stop the loop when we run out of list elements
            break
        except (ValueError, TypeError):
            # Skip non-integer types silently
            continue
    # Print a newline after all integers
    print()
    return count
