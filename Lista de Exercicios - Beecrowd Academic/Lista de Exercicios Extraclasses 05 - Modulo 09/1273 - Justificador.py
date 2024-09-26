n = int(input())

while n != 0:
    list_strings = list()
    largest_string = None
    largest_string_size = float('-inf')

    for i in range(n):
        list_strings.append(input())
        if len(list_strings[i]) > largest_string_size:
            largest_string = list_strings[i]
            largest_string_size = len(list_strings[i])

    for i in range(n):
        justifier = 0
        if len(list_strings[i]) != largest_string_size:
            justifier = largest_string_size - len(list_strings[i])
            list_strings[i] = (' ' * justifier) + list_strings[i]

    for i in range(n):
        print(list_strings[i])

    n = int(input())

    if n != 0:
        print()
