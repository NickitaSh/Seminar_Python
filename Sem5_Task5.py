def display_codes(start, end):
    if start == end:
        print(str(start) + " - " + chr(start))
    else:
        print(str(start) + " - " + chr(start), end=" ")
        display_codes(start + 1, end)

display_codes(32, 127)