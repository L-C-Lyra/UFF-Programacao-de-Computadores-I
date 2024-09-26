with open('archive_1789.txt', 'r', encoding='utf-8', newline='\n') as fin:
    switch = True

    while switch:
        read_line = fin.readline()
        if read_line == 'EOF':
            switch = False
        else:
            l = read_line
            read_line = fin.readline()
            v_i = read_line