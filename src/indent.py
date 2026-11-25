source = "orders_api"
record_count = 100
is_active = True

print("Source:", source)
print("Records:", record_count)
print("Pipeline active:", is_active)

if is_active:
    print("pipeline running")

o = [2,3,1,4,5]
o.append([2,1])
o.extend({9,10})
print("o: ",o)