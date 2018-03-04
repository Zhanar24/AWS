def c_to_f(cel):
    return int((cel * 1.8) +32)
c_to_f(-10)

print("Water freezing at {} C, {} F".format(0, c_to_f(0)))
print("Coldest recorded temperatura is {} C, {} F".format(-79, c_to_f(-79)))
print("Coldest temperatura possible {} C, {} F".format(-273, c_to_f(-273)))