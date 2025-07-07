
class StatusPageClass:
    def __init__(self, title_, bars_):
        self.__inited = {}
        self.__bar_details = {}
        self.__freeY = 4
        self.__bars = {}
        for i in bars_:
            self.__inited[i] = False
            self.__bar_details[i] = {
               'title' : bars_[i],
               'max'   : 0
            }

    def title(self, text_):
        print(
          '\x1b['+
          '2'+
          ';'+
          '1'+
          'H'+
          (text_).ljust(100)
        )

    def initCheck(self, bar_):
        if self.__inited[bar_] == True:
            return
        self.__bars[bar_] = SimpleStatus(
            self.__bar_details[bar_]['title'],
            self.__bar_details[bar_]['max'],
            2,
            self.__freeY
        )
        self.__inited[bar_] = True
        self.__freeY = self.__freeY + 1

    def setMax(self, bar_, max_):
        self.__bar_details[bar_]['max'] = max_
        if self.__inited[bar_] == False:
            return
        self.__bars[bar_].setMax(max_)

    def update(self, bar_, current_):
        self.initCheck(bar_)
        self.__bars[bar_].update(current_)

    def increase(self, bar_):
        self.initCheck(bar_)
        self.__bars[bar_].increase()
