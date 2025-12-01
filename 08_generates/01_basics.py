def serve_chai():
    yield "Cup 1: Masal Chai"
    yield "Cup 2:Ginger Chai"
    yield  "cup 3 Elaichi Chai"
stall= serve_chai()
for cup in stall :
    print(cup)