class Logicalc:
    def __init__(self):
        self.xlist = []
        self.inputnum = '0'

    def set_inputnum(self, nums):
        self.inputnum = nums

    def get_inputnum_str(self):
        return self.correctstrtolabel(self.inputnum)

    def add_num_oper(self, num, oper):
        self.xlist.append(num)
        self.xlist.append(oper)
        resul = ''
        if len(self.xlist) == 0:
            resul = '0'
        elif len(self.xlist) == 1 or len(self.xlist) == 2:
            resul = self.xlist[0]
        elif len(self.xlist) > 2:
            res = float(self.xlist[0])
            for i in range(1, len(self.xlist)):
                if i % 2 == 0:
                    if self.xlist[i - 1] == 'plus':
                        res += float(self.xlist[i])
                    elif self.xlist[i - 1] == 'minus':
                        res -= float(self.xlist[i])
                    elif self.xlist[i - 1] == 'asterisk':
                        res *= float(self.xlist[i])
                    elif self.xlist[i - 1] == 'slash':
                        res /= float(self.xlist[i])
            resul = str(res)
            self.set_inputnum(self.correctstrtolabel(resul))

    def clear(self):
        self.xlist = []

    def __str__(self):
        if len(self.xlist) == 0:
            return '0'
        else:
            strlist = ''
            for i in range(len(self.xlist)):
                if self.xlist[i] == 'plus':
                    strlist += '+'
                elif self.xlist[i] == 'minus':
                    strlist += '-'
                elif self.xlist[i] == 'asterisk':
                    strlist += '×'
                elif self.xlist[i] == 'slash':
                    strlist += '÷'
                else:
                    strlist += self.correctstrtolabel(self.xlist[i])
                strlist += ' '
            return strlist

    def getresult(self):
        self.xlist.append(self.get_inputnum_str())
        self.xlist.append('=')
        if len(self.xlist) == 0:
            return 0.0
        elif len(self.xlist) == 1 or len(self.xlist) == 2:
            return float(self.xlist[0])
        elif len(self.xlist) > 2:
            res = float(self.xlist[0])
            for i in range(1, len(self.xlist)):
                if i % 2 == 0:
                    if self.xlist[i - 1] == 'plus':
                        res += float(self.xlist[i])
                    elif self.xlist[i - 1] == 'minus':
                        res -= float(self.xlist[i])
                    elif self.xlist[i - 1] == 'asterisk':
                        res *= float(self.xlist[i])
                    elif self.xlist[i - 1] == 'slash':
                        res /= float(self.xlist[i])
            return res

    def getresult_str(self):
        resul = ''
        self.xlist.append(self.get_inputnum_str())
        self.xlist.append('=')
        if len(self.xlist) == 0:
            resul = '0'
        elif len(self.xlist) == 1 or len(self.xlist) == 2:
            resul = self.xlist[0]
        elif len(self.xlist) > 2:
            res = float(self.xlist[0])
            for i in range(1, len(self.xlist)):
                if i % 2 == 0:
                    if self.xlist[i - 1] == 'plus':
                        res += float(self.xlist[i])
                    elif self.xlist[i - 1] == 'minus':
                        res -= float(self.xlist[i])
                    elif self.xlist[i - 1] == 'asterisk':
                        res *= float(self.xlist[i])
                    elif self.xlist[i - 1] == 'slash':
                        res /= float(self.xlist[i])
            resul = str(res)
            self.set_inputnum(self.correctstrtolabel(resul))
        return self.correctstrtolabel(resul)

    def correctstrtolabel(self, strnum):
        correctstr = strnum
        if correctstr != '0':
            if '.' in correctstr or ',' in correctstr:
                return correctstr.rstrip('0').rstrip('.')
            else:
                return correctstr
        else:
            return correctstr


numl = Logicalc()
# print(numl.getresult(), numl.getresult_str())
numl.add_num_oper('5.0', 'plus')

print(numl.__str__())
print(numl.get_inputnum_str())
numl.add_num_oper('51.0', 'plus')

print(numl.__str__())
print(numl.get_inputnum_str())
numl.set_inputnum('3')
numl.getresult_str()
print(numl.__str__())
print(numl.get_inputnum_str())
# numl.add_num_oper('1.0', 'plus')
# print(numl.getresult(), numl.getresult_str())
# numl.add_num_oper('1', 'plus')
# print(numl.getresult(), numl.getresult_str())
# numl.add_num_oper('10', 'plus')
# print(numl.getresult(), numl.getresult_str())
# numl.set_inputnum('15.1')


