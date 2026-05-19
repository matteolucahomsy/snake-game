import settings
class Snake:
    def __init__(self):
        self.body =[[settings.WIDTH//2,settings.HEIGHT//2]]
        self.direction=[0,0]
        self.length=1
    def move(self):
        head=self.body[-1].copy()
        head[0]+=self.direction[0]
        head[1]+= self.direction[1]
        self.body.append(head)

        if len(self.body) > self.length:
            del self.body[0]
    def change_direction(self,x,y):
        if (x,y) == (-self.direction[0], -self.direction[1]):
            return
        self.direction=[x,y]
    def check_self_collision(self):
        head =self.body[-1]
        for part in self.body[:-1]:
            if part == head:
                return True
        return False
    def get_head(self):
        return self.body[-1]
    def reset(self):
        self.body=[[settings.WIDTH//2,settings.HEIGHT//2]]
        self.direction=[0,0]
        self.length=1