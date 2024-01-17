'''
def mas():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3
    
g = mas()
#res = next(g)

for res in g:
    print(res)
'''    
def squares(count: int):
    for n in range(count):
        yield n**2
        
for res in squares(5):
    print(res)
