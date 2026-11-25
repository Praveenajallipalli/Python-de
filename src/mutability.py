nums = [1, 'two', 3]
def number():
    nums.append(4)
    a=nums
    return a

def alfa():
    nums.append('five')
    b=nums
    return b

print("numeric fuction: ", number())
print("alfa function: ", alfa())
print( nums )