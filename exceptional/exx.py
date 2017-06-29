#Where are the chocolates from last week?
class Mike(Exception):
    mike="Mike"
    def __init__(self, arg):
        self.mike = arg
def mike(mik):
    raise mik      
try:
    raise Mike("Mike")
except Mike as mike:
    print("Mike")
    print(mike.mike)
finally:
    try:
        assert Mike.mike=="mike","Mike"*10
    except AssertionError as Mike:
        print("Mike")
        print(Mike.args)
    #how many mikes?