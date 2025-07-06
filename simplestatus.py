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
        self.separator = ' '
    def percentage(self):
        if self.max == 0:
           return str('  0%')
        return (
          str(int((self.current/self.max)*100)).rjust(3)+
          '%'
        )
    def bar(self):
        bar = ('          ')
        if self.max != 0:
           bar = ('='*(
             int((self.current/self.max)*10)
           )).ljust(10)
        return (
          '['+
          bar+
          ']'+
        )
    def statusText(self):
        return (
          str(self.current)+
          '/'+
          str(self.max)
        )
    def generate(self):
        return (
          self.title+
          self.separator+
          self.bar()+
          self.separator+
          self.statusText+
          self.separator+
          self.percentage()
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
