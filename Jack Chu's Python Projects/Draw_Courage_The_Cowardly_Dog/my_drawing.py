"""
File: SC101_A1
Name: Jack Chu
----------------------
TODO: Draw Courage the Cowardly Dog!
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    To create each body part of the dog, and get the whole pic
    """
    w = GWindow(width=520, height=520, title='Courage the Cowardly Dog')
    # body
    tail = GPolygon()
    tail.add_vertex((301, 335))
    tail.add_vertex((345, 311))
    tail.add_vertex((352, 296))
    tail.add_vertex((355, 307))
    tail.add_vertex((371, 300))
    tail.add_vertex((361, 317))
    tail.add_vertex((364, 335))
    tail.add_vertex((352, 325))
    tail.add_vertex((301, 350))
    tail.filled = True
    tail.fill_color = 'hotpink'
    tail.color = 'hotpink'
    w.add(tail)
    tail_1 = GPolygon()
    tail_1.add_vertex((301, 335))
    tail_1.add_vertex((342, 313))
    tail_1.add_vertex((349, 327))
    tail_1.add_vertex((301, 350))
    tail_1.filled = True
    w.add(tail_1)
    body = GOval(140, 207)
    body.filled = True
    body.color = 'hotpink'
    body.fill_color = 'hotpink'
    w.add(body, x=203, y=188)
    l_leg = GRect(10, 65)
    l_leg.filled = True
    l_leg.fill_color = 'hotpink'
    l_leg.color = 'hotpink'
    w.add(l_leg, x=221, y=358)
    r_leg = GRect(10, 67)
    r_leg.filled = True
    r_leg.fill_color = 'hotpink'
    r_leg.color = 'hotpink'
    w.add(r_leg, x=316, y=358)
    l_feet = GOval(10, 20)
    l_feet.filled = True
    l_feet.fill_color = 'hotpink'
    l_feet.color = 'hotpink'
    w.add(l_feet, x=221, y=416)
    r_feet = GOval(10, 20)
    r_feet.filled = True
    r_feet.fill_color = 'hotpink'
    r_feet.color = 'hotpink'
    w.add(r_feet, x=316, y=416)
    l_toe = GOval(26, 10)
    l_toe.filled = True
    l_toe.fill_color = 'hotpink'
    l_toe.color = 'hotpink'
    w.add(l_toe, x=213, y=416)
    r_toe = GOval(26, 10)
    r_toe.filled = True
    r_toe.fill_color = 'hotpink'
    r_toe.color = 'hotpink'
    w.add(r_toe, x=308, y=416)
    # bag
    l_bag = GPolygon()
    l_bag.add_vertex((217, 233))
    l_bag.add_vertex((217, 239))
    l_bag.add_vertex((230, 293))
    l_bag.add_vertex((238, 293))
    l_bag.add_vertex((225, 236))
    l_bag.filled = True
    l_bag.fill_color = 'green'
    l_bag.color = 'green'
    w.add(l_bag)
    r_bag = GPolygon()
    r_bag.add_vertex((309, 207))
    r_bag.add_vertex((307, 290))
    r_bag.add_vertex((315, 290))
    r_bag.add_vertex((317, 210))
    r_bag.filled = True
    r_bag.fill_color = 'green'
    r_bag.color = 'green'
    w.add(r_bag)
    down_bag = GPolygon()
    down_bag.add_vertex((227, 289))
    down_bag.add_vertex((215, 353))
    down_bag.add_vertex((330, 353))
    down_bag.add_vertex((316, 289))
    down_bag.filled = True
    down_bag.fill_color = 'green'
    down_bag.color = 'green'
    w.add(down_bag)
    l_but2 = GOval(14, 14)
    l_but2.filled = True
    l_but2.fill_color = 'grey'
    l_but2.color = 'grey'
    w.add(l_but2, x=225, y=283)
    l_but = GOval(12, 12)
    l_but.filled = True
    w.add(l_but, x=226, y=284)
    r_but2 = GOval(14, 14)
    r_but2.filled = True
    r_but2.fill_color = 'grey'
    r_but2.color = 'grey'
    w.add(r_but2, x=304, y=282)
    r_but = GOval(12, 12)
    r_but.filled = True
    w.add(r_but, x=305, y=283)
    # hand
    l_hand = GRect(10, 50)
    l_hand.filled = True
    l_hand.fill_color = 'hotpink'
    w.add(l_hand, x=246, y=271)
    l_thumb = GOval(23, 8)
    l_thumb.filled = True
    l_thumb.fill_color = 'hotpink'
    l_thumb.color = 'hotpink'
    w.add(l_thumb, x=239, y=317)
    l_finger = GOval(10, 20)
    l_finger.filled = True
    l_finger.fill_color = 'hotpink'
    l_finger.color = 'hotpink'
    w.add(l_finger, x=246, y=315)
    r_hand = GRect(10, 52)
    r_hand.filled = True
    r_hand.fill_color = 'hotpink'
    w.add(r_hand, x=286, y=272)
    r_thumb = GOval(23, 8)
    r_thumb.filled = True
    r_thumb.fill_color = 'hotpink'
    r_thumb.color = 'hotpink'
    w.add(r_thumb, x=280, y=318)
    r_finger = GOval(10, 20)
    r_finger.filled = True
    r_finger.fill_color = 'hotpink'
    r_finger.color = 'hotpink'
    w.add(r_finger, x=286, y=316)
    hand_eraser = GRect(60, 10)
    hand_eraser.filled = True
    hand_eraser.fill_color = 'hotpink'
    hand_eraser.color = 'hotpink'
    w.add(hand_eraser, x=240, y=265)
    # head
    chick = GOval(40, 35)
    chick.filled = True
    chick.fill_color = 'hotpink'
    w.add(chick, x=320, y=145)
    l_ear = GPolygon()
    l_ear.add_vertex((220, 68))
    l_ear.add_vertex((220, 74))
    l_ear.add_vertex((240, 118))
    l_ear.add_vertex((246, 118))
    l_ear.add_vertex((226, 71))
    l_ear.filled = True
    w.add(l_ear)
    l_ear3 = GOval(87, 23)
    l_ear3.filled = True
    w.add(l_ear3, x=140, y=62)
    l_ear2 = GOval(70, 7)
    l_ear2.filled = True
    l_ear2.fill_color = 'chocolate'
    l_ear2.color = 'chocolate'
    w.add(l_ear2, x=146, y=66)
    mouth2 = GOval(60, 49)
    mouth2.filled = True
    mouth2.fill_color = 'hotpink'
    w.add(mouth2, x=183, y=195)
    head = GOval(150, 120, x=200, y=100)
    head.filled = True
    head.fill_color = 'hotpink'
    w.add(head)
    r_ear = GPolygon()
    r_ear.add_vertex((315, 76))
    r_ear.add_vertex((295, 108))
    r_ear.add_vertex((301, 108))
    r_ear.add_vertex((321, 73))
    r_ear.filled = True
    w.add(r_ear)
    r_ear3 = GOval(92, 23)
    r_ear3.filled = True
    w.add(r_ear3, x=315, y=63)
    r_ear2 = GOval(75, 7)
    r_ear2.filled = True
    r_ear2.fill_color = 'chocolate'
    r_ear2.color = 'chocolate'
    w.add(r_ear2, x=321, y=67)
    mouth = GArc(420, 280, 90, 90)
    mouth.filled = True
    mouth.fill_color = 'hotpink'
    mouth.color = 'hotpink'
    w.add(mouth, x=158, y=145)
    mouth1 = GOval(55, 49)
    mouth1.filled = True
    mouth1.fill_color = 'hotpink'
    w.add(mouth1, x=128, y=195)
    nose = GPolygon()
    nose.add_vertex((146, 190))
    nose.add_vertex((212, 212))
    nose.add_vertex((178, 247))
    nose.filled = True
    nose.fill_color = 'chocolate'
    nose.color = 'chocolate'
    w.add(nose)
    nose2 = GPolygon()
    nose2.add_vertex((146, 191))
    nose2.add_vertex((178, 247))
    nose2.add_vertex((212, 212))
    nose2.add_vertex((180, 220))
    nose2.filled = True
    w.add(nose2)
    l_eye = GOval(40, 71)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    w.add(l_eye, x=198, y=108)
    r_eye = GOval(45, 77)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    w.add(r_eye, x=248, y=107)
    lip = GArc(480, 420, 280, 65)
    w.add(lip, x=132, y=65)
    lip_2 = GArc(480, 240, 40, 32)
    w.add(lip_2, x=238, y=159)
    eraser = GOval(13, 32)
    eraser.filled = True
    eraser.fill_color = 'hotpink'
    eraser.color = 'hotpink'
    w.add(eraser, x=339, y=146)
    l_eye_ball = GOval(12, 22)
    l_eye_ball.filled = True
    w.add(l_eye_ball, x=216, y=142)
    l_eye_ball2 = GOval(4, 6)
    l_eye_ball2.filled = True
    l_eye_ball2.fill_color = 'white'
    l_eye_ball2.color = 'white'
    w.add(l_eye_ball2, x=222, y=146)
    r_eye_ball = GOval(12, 21)
    r_eye_ball.filled = True
    w.add(r_eye_ball, x=266, y=145)
    l_eye_ball2 = GOval(4, 6)
    l_eye_ball2.filled = True
    l_eye_ball2.fill_color = 'white'
    l_eye_ball2.color = 'white'
    w.add(l_eye_ball2, x=272, y=149)
    hair_1 = GArc(400, 240, 30, 38)
    w.add(hair_1, x=50, y=204)
    hair_2 = GArc(32, 32, 40, 128)
    w.add(hair_2, x=114, y=222)
    hair_1 = GArc(90, 90, 40, 68)
    w.add(hair_1, x=214, y=225)
    pink1 = GOval(2, 2)
    pink1.filled = True
    w.add(pink1, x=149, y=224)
    pink2 = GOval(2, 2)
    pink2.filled = True
    w.add(pink2, x=217, y=221)
    pink3 = GOval(2, 2)
    pink3.filled = True
    w.add(pink3, x=207, y=230)
    pink4 = GOval(2, 2)
    pink4.filled = True
    w.add(pink4, x=224, y=230)
    brow_1 = GArc(160, 150, 270, 70)
    w.add(brow_1, x=153, y=65)
    brow_2 = GArc(65, 50, 180, 120)
    w.add(brow_2, x=260, y=84)
    eye_line = GArc(185, 167, 280, 60)
    w.add(eye_line, x=164, y=131)
    eye_line2 = GArc(122, 108, 190, 85)
    w.add(eye_line2, x=252, y=142)


















if __name__ == '__main__':
    main()
