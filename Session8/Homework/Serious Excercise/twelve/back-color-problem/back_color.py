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
    textcolor = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    colortext = ['#3F51B5','#C62828', '#FFD600', '#4CAF50' ]
    quiz_type = randint(0, 1)
    return [
                choice(textcolor) ,
                choice(colortext),
                quiz_type # 0 : meaning, 1: color
            ]
def mouse_press(x, y, text, color, quiz_type): 
    result = False
    for shape in shapes:
        rect = shape['rect']
        x1, y1, width, height = rect
        if x1 <= x <= x1 + width:
            if y1 <= y <= y1 + height:
                if quiz_type == 0:
                    if text.lower() == shape['text'].lower():
                        result = True
                    else:
                        result = False
                else:
                    if color.lower() == shape['color'].lower():
                        result = True
                    else:
                        result = False
                break
    return result