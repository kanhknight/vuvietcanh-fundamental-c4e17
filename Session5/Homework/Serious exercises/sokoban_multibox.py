p = {
    "x":1,
    "y":1
}

# b ={
#     "x":2,
#     "y":2
# }

boxes = [
    {
        "x":4,
        "y":2
    },
    {
        "x":5,
        "y":3
    },
    {
        "x":3,
        "y":6
    }
]
while True:
    # Bien luu tru gia tri tuong lai cua px va py
    next_px = p["x"]
    next_py = p["y"]
    dx = 0
    dy = 0
    # Ve bang Sokoban
    for i in range(10):
        for j in range(10):
            if j == p["x"] and i == p["y"]:
                print("P ", end = " ")
            elif j == 1 and i ==3:
                print("G ", end = " ")
            else:
                for box in boxes:
                    if j == box["x"] and i == box["y"]:
                            print("B ", end = " ")
                            break
                else:
                            print("_ ", end = " ")
        print()
    next_bx = box["x"]
    next_by = box["y"]
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
    if next_px == box["x"] and next_py == box["y"]:
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
    if 0 <= next_px <10:
        p["x"] = next_px
    if 0 <= next_py <10:
        p["y"] = next_py

    # Kiem tra gioi han cua bang va box
    if 0 <= next_bx < 10:
        box["x"] = next_bx
    if 0<= next_by < 10:
        box["y"] = next_by