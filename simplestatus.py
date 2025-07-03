

class SimpleStatus:
    def __init__(self, max_, posx_, posy_):
        self.pos_x = str(posx_)
        self.pos_y = str(posy_)
        self.max = max_
        self.current = 0
    def write(self):
        print(
          '\x1b['+
          str(self.pos_x)+
          ';'+
          str(self.pos_y)+
          'H'+
          '['+
          ('='*int((self.current/self.max)*10)).ljust(10)+
          ']  '+
          str(self.current)+
          '/'+
          str(self.max)
        )
    def update(self, current_):
        self.current = current_
        self.write()
