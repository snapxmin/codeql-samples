def positive(L, x):
    c1 = -1
    c2 = -1
  
    for c in L:
        if c1 >= 0 and c2 >= 0:
            break
    
        if c == x and c1 < 0:
            continue
    
        if c == x and c2 < 0:
            # If we got here we already know that
            # c1 < 0 and c != x so the following
            # statement should be unreachable
            print('unreachable')
            break
            
    return c1, c2


def false_positive(L, x):
    c1 = -1
    c2 = -1
  
    for c in L:
        if c1 >= 0 and c2 >= 0:
            break
    
        if c == x and c1 < 0:
            c1 = c
            continue
    
        if c == x and c2 < 0:
            # In this case we are updating the variables c1 and c2 in
            # the loop.  So we could have c1 >= 0 and c2 < 0 and thus
            # this code is reachable
            c2 = c
            break
            
    return c1, c2
