from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_center = self.mouth.getCenter()
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        mouth_center.move(0, abs(p1.getX() - mouth_center.getX()))
        left_side = Line(p1, mouth_center)
        right_side = Line(p2, mouth_center)
        left_side.draw(self.window)
        right_side.draw(self.window)

    def shock(self):
        mouth_size = 0.25 * (self.head.getRadius())
        mouth = Circle(self.mouth.getCenter(), mouth_size)
        self.mouth.undraw()
        mouth.draw(self.window)

    def wink(self):
        eye_center = self.left_eye.getCenter()
        p1 = self.left_eye.getP1()
        p2 = self.left_eye.getP2()
        rotater = (abs(p1.getY() - p2.getY()))/2
        self.left_eye.undraw()
        closed_eye = Line(Point(p1.getX(), (p1.getY() + rotater)), Point(p2.getX(), (p2.getY() - rotater)))
        closed_eye.draw(self.window)
        self.smile()
