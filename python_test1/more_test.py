my_list = [6,2,8,1,0,2,8,1,6,3,0,12,90,89,4,21]
print (sorted(my_list)) # [0, 0, 1, 1, 2, 2, 3, 6, 6, 8, 8, 12, 21, 34, 89, 90]


my_list_2 = ['h','t','m','a','er']
print(sorted(my_list_2)) # ['a', 'er', 'h', 'm', 't']

my_dict = {'a1':1, '4':4, '2':2}
print(sorted(my_dict))

i, v = ['dddd', 'ggggg']
print(i.join('hhhhh'))
image = 'ff'
if image:
    print ('true')
else:
    print ('false')


test = [(9, 'abbc'), (2, 'ffff'), (4, 'hhhh')]

for t, b in test:
    print (t)


# Python program to search all 
# anagrams of a pattern in a text 
  
MAX=256 
  
# This function returns true 
# if contents of arr1[] and arr2[] 
# are same, otherwise false. 
def compare(arr1, arr2): 
    for i in range(MAX): 
        if arr1[i] != arr2[i]: 
            return False
    return True
      
# This function search for all 
# permutations of pat[] in txt[]   
def search(pat, txt): 
  
    M = len(pat) 
    N = len(txt) 
  
    # countP[]:  Store count of 
    # all characters of pattern 
    # countTW[]: Store count of 
    # current window of text 
    countP = [0]*MAX
  
    countTW = [0]*MAX
  
    for i in range(M): 
        (countP[ord(pat[i]) ]) += 1
        (countTW[ord(txt[i]) ]) += 1
  
    # Traverse through remaining 
    # characters of pattern 
    for i in range(M,N): 
  
        # Compare counts of current 
        # window of text with 
        # counts of pattern[] 
        if compare(countP, countTW): 
            print("Found at Index", (i-M)) 
  
        # Add current character to current window 
        (countTW[ ord(txt[i]) ]) += 1
  
        # Remove the first character of previous window 
        (countTW[ ord(txt[i-M]) ]) -= 1
      
    # Check for the last window in text     
    if compare(countP, countTW): 
        print("Found at Index", N-M) 
          
# Driver program to test above function        
txt = "cbabadcbbabbcbabaabccbabc"
pat = "abbc"       
search(pat, txt)    