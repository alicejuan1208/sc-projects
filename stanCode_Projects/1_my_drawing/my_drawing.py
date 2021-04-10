"""
File: my_drawing.py
Name: Alice
----------------------
TODO:
Using the objects of the classes GOval, GRect, GLabel, GPolygon, and GLine to make a creative masterpiece!
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    The program shows the picture of "Pui Pui Molcar"
    "Pui Pui Molcar" is a famous cartoon which I watch recently.
    """
    window = GWindow(width=800, height=500, title='Alice_de_hwa')

    background = GRect(800, 500)
    background.filled = True
    background.fill_color = 'lightskyblue'
    background.color = 'lightskyblue'
    window.add(background)

    cloud1 = GOval(60, 30, x=50, y=50)
    cloud1.filled = True
    cloud1.fill_color = 'snow'
    cloud1.color = 'snow'
    window.add(cloud1)

    cloud2 = GOval(70, 50, x=70, y=40)
    cloud2.filled = True
    cloud2.fill_color = 'snow'
    cloud2.color = 'snow'
    window.add(cloud2)

    cloud3 = GOval(60, 30, x=100, y=50)
    cloud3.filled = True
    cloud3.fill_color = 'snow'
    cloud3.color = 'snow'
    window.add(cloud3)

    cloud4 = GOval(80, 50, x=610, y=50)
    cloud4.filled = True
    cloud4.fill_color = 'snow'
    cloud4.color = 'snow'
    window.add(cloud4)

    cloud5 = GOval(100, 90, x=650, y=30)
    cloud5.filled = True
    cloud5.fill_color = 'snow'
    cloud5.color = 'snow'
    window.add(cloud5)

    cloud6 = GOval(80, 50, x=710, y=50)
    cloud6.filled = True
    cloud6.fill_color = 'snow'
    cloud6.color = 'snow'
    window.add(cloud6)

    wordbg = GOval(250, 110, x=275, y=60)
    wordbg.filled = True
    wordbg.fill_color = 'snow'
    wordbg.color = 'snow'
    window.add(wordbg)

    word = GLabel('PUI PUI', x=290, y=150)
    word.font = 'Helvetica-60-bold'
    word.color = 'coral'
    window.add(word)

    wood1 = GRect(20, 200, x=55, y=200)
    wood1.filled = True
    wood1.fill_color = 'burlywood'
    wood1.color = 'burlywood'
    window.add(wood1)

    wood2 = GRect(20, 200, x=135, y=200)
    wood2.filled = True
    wood2.fill_color = 'burlywood'
    wood2.color = 'burlywood'
    window.add(wood2)

    wood3 = GRect(20, 200, x=215, y=200)
    wood3.filled = True
    wood3.fill_color = 'burlywood'
    wood3.color = 'burlywood'
    window.add(wood3)

    wood4 = GRect(20, 200, x=565, y=200)
    wood4.filled = True
    wood4.fill_color = 'burlywood'
    wood4.color = 'burlywood'
    window.add(wood4)

    wood5 = GRect(20, 200, x=645, y=200)
    wood5.filled = True
    wood5.fill_color = 'burlywood'
    wood5.color = 'burlywood'
    window.add(wood5)

    wood6 = GRect(20, 200, x=725, y=200)
    wood6.filled = True
    wood6.fill_color = 'burlywood'
    wood6.color = 'burlywood'
    window.add(wood6)

    l_tree3 = GOval(120, 120, x=165, y=105)
    l_tree3.filled = True
    l_tree3.fill_color = 'lightgreen'
    l_tree3.color = 'lightgreen'
    window.add(l_tree3)

    r_tree3 = GOval(120, 120, x=515, y=105)
    r_tree3.filled = True
    r_tree3.fill_color = 'lightgreen'
    r_tree3.color = 'lightgreen'
    window.add(r_tree3)

    l_tree2 = GOval(120, 120, x=85, y=135)
    l_tree2.filled = True
    l_tree2.fill_color = 'lightseagreen'
    l_tree2.color = 'lightseagreen'
    window.add(l_tree2)

    r_tree2 = GOval(120, 120, x=595, y=135)
    r_tree2.filled = True
    r_tree2.fill_color = 'lightseagreen'
    r_tree2.color = 'lightseagreen'
    window.add(r_tree2)

    l_tree1 = GOval(120, 120, x=5, y=185)
    l_tree1.filled = True
    l_tree1.fill_color = 'lightgreen'
    l_tree1.color = 'lightgreen'
    window.add(l_tree1)

    r_tree1 = GOval(120, 120, x=675, y=185)
    r_tree1.filled = True
    r_tree1.fill_color = 'lightgreen'
    r_tree1.color = 'lightgreen'
    window.add(r_tree1)

    road1 = GPolygon()
    road1.add_vertex((300, 220))
    road1.add_vertex((500, 220))
    road1.add_vertex((1000, 500))
    road1.add_vertex((-200, 500))
    road1.filled = True
    road1.fill_color = 'white'
    road1.color = 'white'
    window.add(road1)

    road2 = GPolygon()
    road2.add_vertex((325, 220))
    road2.add_vertex((475, 220))
    road2.add_vertex((900, 500))
    road2.add_vertex((-100, 500))
    road2.filled = True
    road2.fill_color = 'whitesmoke'
    road2.color = 'whitesmoke'
    window.add(road2)

    road3 = GPolygon()
    road3.add_vertex((320, 255))
    road3.add_vertex((480, 255))
    road3.add_vertex((750, 500))
    road3.add_vertex((50, 500))
    road3.filled = True
    road3.fill_color = 'forestgreen'
    road3.color = 'forestgreen'
    window.add(road3)

    l_ear = GOval(50, 30, x=255, y=265)
    l_ear.filled = True
    l_ear.fill_color = 'saddlebrown'
    l_ear.color = 'saddlebrown'
    window.add(l_ear)

    r_ear = GOval(50, 30, x=495, y=265)
    r_ear.filled = True
    r_ear.fill_color = 'saddlebrown'
    r_ear.color = 'saddlebrown'
    window.add(r_ear)

    face1 = GRect(200, 200, x=300, y=200)
    face1.filled = True
    face1.fill_color = 'darkorange'
    face1.color = 'darkorange'
    window.add(face1)

    face2 = GRect(200, 75, x=300, y=325)
    face2.filled = True
    face2.fill_color = 'cornsilk'
    face2.color = 'cornsilk'
    window.add(face2)

    face3 = GRect(50, 50, x=375, y=275)
    face3.filled = True
    face3.fill_color = 'cornsilk'
    face3.color = 'cornsilk'
    window.add(face3)

    l_eye = GOval(30, 30, x=345, y=285)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    l_eye.color = 'black'
    window.add(l_eye)

    r_eye = GOval(30, 30, x=425, y=285)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    r_eye.color = 'black'
    window.add(r_eye)

    l_eyelight = GOval(5, 5, x=365, y=290)
    l_eyelight.filled = True
    l_eyelight.fill_color = 'snow'
    l_eyelight.color = 'snow'
    window.add(l_eyelight)

    r_eyelight = GOval(5, 5, x=445, y=290)
    r_eyelight.filled = True
    r_eyelight.fill_color = 'snow'
    r_eyelight.color = 'snow'
    window.add(r_eyelight)

    mouth1 = GLine(380, 380, 400, 390)
    mouth1.color = 'black'
    window.add(mouth1)

    mouth2 = GLine(420, 380, 400, 390)
    mouth2.color = 'black'
    window.add(mouth2)

    mouth3 = GLine(400, 400, 400, 390)
    mouth3.color = 'black'
    window.add(mouth3)

    forehead = GPolygon()
    forehead.add_vertex((325, 220))
    forehead.add_vertex((475, 220))
    forehead.add_vertex((480, 255))
    forehead.add_vertex((320, 255))
    forehead.filled = True
    forehead.fill_color = 'peachpuff'
    forehead.color = 'peachpuff'
    window.add(forehead)

    l_wheel = GRect(40, 60, x=265, y=345)
    l_wheel.filled = True
    l_wheel.fill_color = 'pink'
    l_wheel.color = 'pink'
    window.add(l_wheel)

    r_wheel = GRect(40, 60, x=495, y=345)
    r_wheel.filled = True
    r_wheel.fill_color = 'pink'
    r_wheel.color = 'pink'
    window.add(r_wheel)



if __name__ == '__main__':
    main()
