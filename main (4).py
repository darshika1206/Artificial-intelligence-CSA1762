'''
#Accessing first and last character
s = input("")
print(f"first chara {s[0]},the last character {s[-1]}")
'''
'''
# Extract the substring:
s = input("")
start = int(input(""))
end = int(input(""))
print(f"The substring is : {s[start : end+1]}")
'''
'''
# count occurance of a character
s = input("")
char = input("")
print(f"The char{char} occur {s.count(char)} times.")

'''
'''
# count the word 
s = input("")
word = input("")
print(f"The char {word} occur : {s.count(word)} times.")

'''
'''
# count the space 
word = input("")
print(f"The num of space occur {word.count("")}.")
'''
'''
# convert title case without title():
s = input().split()
t = ""
for i in s:
    s1 = str(i)
    s2 = s1[0].upper()
    t += s2+s1[1::]+" "
t = t.rstrip()
print(t)
'''

'''
s = input("")
t =""
t += s[0].upper()
i = 1 
while (i < len(s)-1):
    if s[i] == " ":
        t+=s[i]
        t += s[i+1].upper()
        i += 2
    else: 
        t+= s[i].lower()
        i += 1 
t += s[len(s) - 1]
print(t)
'''
'''
# Remove the duplicate preserving order 
x = input("")
print(set(x))
s = ""
for i in x:
    if i not in s:
        s += i
else:
    pass
print(f"String with distinct data: {s}")
'''
'''

# print duplicate preserving order 
x = input("")
print(set(x))
s = ""
ans = ""
for i in x:
    if i not in s:
        s += i
    else:
        if i not in ans:
            ans+= i
print(f"String with distinct data: {ans}")
'''
'''
# Check two String are anagram (sort based):
def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    return False
s1 = input("")
s2 = input("")
ans = anagram(s1,s2)
print("The String are anagram" if ans == True else "not anagram")


'''
'''
s = input("").split()
max = 0
char = ""
for i in s:
    t = str(i)
    if len(t)>max:
        max = len(t)
        char=i
print(f"The max character is : '{char}' with The length of : '{max}''.")
'''
'''
# Remove nth index 
s = input("")
ind = int(input(""))
print(f"String after removing {ind} is {s[:ind]+s[ind+1:]}")


  
  
  
  

# 