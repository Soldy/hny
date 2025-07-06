"""
simple status bar.

Because others are complex.
just check this : https://github.com/wolph/python-progressbar/blob/develop/progressbar/bar.py
"""

class SimpleStatus:
    def __init__(self, title_, max_, posx_, posy_):
        self.title = str(title_)
        self.pos_x = str(posx_)
        self.pos_y = str(posy_)
        self.max = max_
        self.current = 0
    def generate(self):
        return (
          self.title+
          ' ['+
          ('='*int((self.current/self.max)*10)).ljust(10)+
          ']  '+
          str(self.current)+
          '/'+
          str(self.max)+
          ' '+
          str(int((self.current/self.max)*100))+
          '%'
        )
    def write(self):
        print(
          '\x1b['+
          str(self.pos_x)+
          ';'+
          str(self.pos_y)+
          'H'+
          self.generate()
        )

    def update(self, current_):
        self.current = current_

    def increase(self):
        self.current = self.current + 1
        self.write()
