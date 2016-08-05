class Hiker:
    nl = [{'num':1000,'d':'M'},
          {'num':900,'d':'CM'},
          {'num':500,'d':'D'},
          {'num':400,'d':'CD'},
          {'num':100,'d':'C'},
          {'num':90,'d':'XC'},
          {'num':50,'d':'L'},
          {'num':40,'d':'XL'},
          {'num':10,'d':'X'},
          {'num':9,'d':'IX'},
          {'num':5,'d':'V'},
          {'num':4,'d':'IV'},
          {'num':1,'d':'I'}]

    def answer(self, number):
        varnum = int(number)
        theAnswer=""
        for x in self.nl:
            while x['num']<=varnum & varnum>0:
                if x['num']<=varnum:
                    theAnswer = theAnswer + x['d']
                    varnum= varnum - x['num']
        return theAnswer
