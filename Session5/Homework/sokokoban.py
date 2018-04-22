p = {
    "x":1,
    "y":1
}

b ={
    "x":2,
    "y":2
}

while True:
    # Bien luu tru gia tri tuong lai cua px va py
    next_px = p["x"]
    next_py = p["y"]
    next_bx = b["x"]
    next_by = b["y"]
    dx = 0
    dy = 0
    # Ve bang Sokoban
    for i in range(4):
        for j in range(4):
            if j == p["x"] and i == p["y"]:
                print("P ", end = " ")
            elif j == b["x"] and i == b["y"]:
                print("B ", end = " ")
            elif j == 1 and i ==3:
                print("G ", end = " ")
            else:
                print("_ ", end = " ")
        print()
    
    #Player Di Chuyen
    m = input("Enter your move? (W/A/S/D) ").upper()
    if m == "W":
        # next_py -=1
        dy = -1
    elif m == "A":
        # next_px  -=1
        dx = -1
    elif m == "S":
        # next_py +=1
        dy = 1
    elif m == "D":
        # next_px  +=1
        dx  = 1

    next_px +=dx
    next_py +=dy

    # Đẩy hộp
    if next_px == b["x"] and next_py == b["y"]:
        # if m == "W":
        #     next_by -=1
        # elif m == "A":
        #     next_bx -=1
        # elif m =="S":
        #     next_by +=1
        # elif m =="D":
        #     next_bx +=1
        next_bx +=dx
        next_by +=dy

    # Kiem tra gioi han cua bang va gan  gia tri cua bien tuong lai vao px va py 
    if 0 <= next_px <4:
        p["x"] = next_px
    if 0 <= next_py <4:
        p["y"] = next_py

    # Kiem tra gioi han cua bang va box
    if 0 <= next_bx < 4:
        b["x"] = next_bx
    if 0<= next_by < 4:
        b["y"] = next_by
    
    