import time
class Snake():
    def __init__(self):
        self.segments_addr = [0x09,0x08,0x07,0x06,0x05,0x04,0x03,0x02]
        self.state = [0] * len(self.segments_addr)
        print(self.state)
        self.state[0] = -2
    def serpentine(self):
        for j in range(len(self.segments_addr)-1,0,-1):
            self.state[j] = self.state[j-1]
        self.update_head()
        self.draw()

    def draw(self, reverse=False):
        actions = reversed(self.state) if reverse else self.state
        print("\n"*5)
        print(actions)
        for i in actions:
            if i == -2:
                print("@| |")
            elif i == 2:
                print(" | |@")
            else:
                print(" |@|")
        print("\n")
        time.sleep(0.25)
    def update_head(self):
        if self.state[0] == -2:
            self.state[0] = 1
        elif self.state[0] == 1:
            self.state[0] = 2
        elif self.state[0] == 2:
            self.state[0] = -1
        elif self.state[0] == -1:
            self.state[0] = -2
    def serpentine_turn(self, direct):
        if direct == "left":
            while self.state[0] != -2:
                self.serpentine()
            self.serpentine()
            self.state[0] = -2
            self.state[1] = -2
        elif direct == "right":
            while self.state[0] != 2:
                self.serpentine()
            self.serpentine()
            self.state[0] = 2
            self.state[1] = 2
        self.draw()
                
snake = Snake()
for i in range(10):
    snake.serpentine()
snake.serpentine_turn("right")
for i in range(10):
    snake.serpentine()