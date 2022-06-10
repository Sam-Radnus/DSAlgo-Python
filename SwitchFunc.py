class Month(object):
    def month_1(self):
        print('hi 1')

    def month_2(self):
        print('hi 2')

    def month_3(self):
        print('hi 3')

    def month_4(self):
        print('hi 4')

    def month_5(self):
        print('hi 5')

    def month_6(self):
        print('hi 6')

    def getMonth(self, no):
        name_of_method = "month_" + str(no)
        try:
            method = getattr(self, name_of_method)
            method()
        except:
            print('not available')


mon = Month()

mon.getMonth(0.1)
