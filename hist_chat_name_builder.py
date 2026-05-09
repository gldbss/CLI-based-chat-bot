import random as r

nums = "1234567890"

def make_name():
    name="".join(r.choices(nums,k=12))
    return name