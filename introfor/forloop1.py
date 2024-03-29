#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list vendors
for x in vendors:
    print("\nThe vendor is:" + x, end="")  # each time through the loop print value of x
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")  # when the loop ends print this
