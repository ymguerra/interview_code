'''
    is string unique?
'''

def has_unique_char(characters):
    if len(characters) > 256:
        return False
    
    chart_set = [0] * 256
    
    for pos in range(len(characters)):
        val = ord(characters[pos])
        if chart_set[val] == True:
            return False
        
        chart_set[val] = True
    
    return True

print (has_unique_char('abcdz'))
print ('********************* Unique String *********************************')


