from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

def generate_quiz():
    color_text = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    colortext = ['#3F51B5','#C62828', '#FFD600', '#4CAF50' ]
    a = randint(0,3)
    b = randint(0,3)
    quiz_type = randint(0, 1)
    return [
                color_text[a] ,
                colortext[b],
                quiz_type # 0 : meaning, 1: color
            ]
def mouse_press(x, y, text, color, quiz_type):
    a = generate_quiz()
    print(a)
    for shape in shapes:
        x_area_max = shape["rect"][0]+ shape["rect"][2]
        y_area_max = shape["rect"][1] + shape["rect"][3]
        if x >= shape["rect"][0] and y >= shape["rect"][1] and x<= x_area_max and y <= y_area_max:
            return True
    else:  
            return False

