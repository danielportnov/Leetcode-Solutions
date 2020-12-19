def magical_string(n):
    string = string_gen(n)
    return string.count('1')

def string_gen(n):
    start = '122'
    i = 2
    alt = '1'

    while len(start) < n:
        if start[i] == '2':
            start += alt * 2
        else:
            start += alt
        
        if alt == '1':
            alt = '2'
        else:
            alt = '1'
        
        i += 1
    
    return start[:n]