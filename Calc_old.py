from tkinter import *

def calcstr(strnum):
    listnum = list(strnum.split())
    result = listnum[0]
    oper = ''
    for i in range(1, len(listnum)):
        if not listnum[i].isdigit():
            if listnum[i] == '+':
                pass
        print(listnum[i])

class CalcWindow:
    def __init__(self, width, height, title='Calc'):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f'{width}x{height}+200+200')
        self.btnw = 4
        self.btnh = 1
        self.cbgnum = '#D1D0D5'
        self.cbgfunr = '#F09225'
        self.cbgfunt = '#C6C5CA'
        self.fs = ('Calibri light', 20)
        self.fstop = ('Calibri light', 15)
        self.fsbot = ('Calibri light', 35)
        self.lastinput = ''
        self.currentsum = 0.0
        #labels:
        self.toplText = StringVar()
        self.toplText.set('0')
        self.Toplabel = Label(self.root, bg='black', textvariable=self.toplText, fg='white', font=self.fstop, anchor=E, width=self.btnw, height=self.btnh)
        self.botlText = StringVar()
        self.botlText.set('0')
        self.Botlabel = Label(self.root, bg='black', textvariable=self.botlText, fg='white', font=self.fsbot, anchor=E, width=self.btnw, height=self.btnh)
        #buttons functions:
        self.cancelbtn = Button(self.root, bg=self.cbgfunt, text='AC', font=self.fs, width=self.btnw, height=self.btnh, command=self.canceloff)
        self.polarbtn = Button(self.root, bg=self.cbgfunt, text='+/-', font=self.fs, width=self.btnw, height=self.btnh)
        self.percentbtn = Button(self.root, bg=self.cbgfunt, text='%', font=self.fs, width=self.btnw, height=self.btnh)
        self.divisionbtn = Button(self.root, bg=self.cbgfunr, text='÷', font=self.fs, width=self.btnw, height=self.btnh)
        self.multiplicbtn = Button(self.root, bg=self.cbgfunr, text='×', font=self.fs, width=self.btnw, height=self.btnh)
        self.subtractbtn = Button(self.root, bg=self.cbgfunr, text='-', font=self.fs, width=self.btnw, height=self.btnh)
        self.additionbtn = Button(self.root, bg=self.cbgfunr, text='+', font=self.fs, width=self.btnw, height=self.btnh)
        self.enterbtn = Button(self.root, bg=self.cbgfunr, text='=', font=self.fs, width=self.btnw, height=self.btnh)
        #bottons numbers:
        self.num7 = Button(self.root, text='7', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('7'))
        self.num8 = Button(self.root, text='8', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('8'))
        self.num9 = Button(self.root, text='9', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('9'))
        self.num4 = Button(self.root, text='4', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('4'))
        self.num5 = Button(self.root, text='5', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('5'))
        self.num6 = Button(self.root, text='6', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('6'))
        self.num1 = Button(self.root, text='1', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('1'))
        self.num2 = Button(self.root, text='2', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('2'))
        self.num3 = Button(self.root, text='3', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('3'))
        self.num0 = Button(self.root, text='0', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('0'))
        self.numdot = Button(self.root, text='.', font=self.fs, bg=self.cbgnum, width=self.btnw, height=self.btnh, command=lambda: self.num_btn_action('.'))
        #binds nums:
        self.root.bind("<KeyPress>", func=lambda event: self.num_btn_action(event.keysym))


    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        #label draw
        self.Toplabel.grid(row=0, column=0, columnspan=4, sticky=W+E)
        self.Botlabel.grid(row=1, column=0, columnspan=4, sticky=W+E)
        #buttons function draw
        self.cancelbtn.grid(row=2, column=0)
        self.polarbtn.grid(row=2, column=1)
        self.percentbtn.grid(row=2, column=2)
        self.divisionbtn.grid(row=2, column=3)
        self.multiplicbtn.grid(row=3, column=3)
        self.subtractbtn.grid(row=4, column=3)
        self.additionbtn.grid(row=5, column=3)
        self.enterbtn.grid(row=6, column=3)
        #buttins numbers draw
        self.num7.grid(row=3, column=0)
        self.num8.grid(row=3, column=1)
        self.num9.grid(row=3, column=2)
        self.num4.grid(row=4, column=0)
        self.num5.grid(row=4, column=1)
        self.num6.grid(row=4, column=2)
        self.num1.grid(row=5, column=0)
        self.num2.grid(row=5, column=1)
        self.num3.grid(row=5, column=2)
        self.num0.grid(row=6, column=0, columnspan=2, sticky=W+E)
        self.numdot.grid(row=6, column=2)

    def num_btn_action(self, num):
        print(num)
        if '0' <= num <= '9' or num == 'period' or num == 'comma':
            if self.lastinput == 'oper':
                self.botlText.set('0')
            elif self.lastinput == 'Return':
                self.canceloff()
            if num == 'period' or num == 'comma':
                if self.botlText.get().find('.') != -1:
                    return
                num = '.'
            if self.botlText.get() == '0' and num != '.':
                self.botlText.set(num)
            else:
                self.botlText.set(self.botlText.get() + num)
            self.lastinput = 'digit'
        elif num == 'plus' or num == 'minus' or num == 'asterisk' or num == 'slash':
            if self.toplText.get() == '0' and self.botlText.get() != '0':
                self.currentsum = float(self.botlText.get())
                self.toplText.set(self.correctstrtolabel(self.botlText.get()) + self.opertolabel(num))
                self.botlText.set(self.correctstrtolabel(str(self.currentsum)))
            elif self.toplText.get() == '0' and self.botlText.get() == '0':
                self.currentsum = self.operfunc(num, self.currentsum, float(self.botlText.get()))
                self.toplText.set(self.correctstrtolabel(self.botlText.get()) + self.opertolabel(num))
                self.botlText.set(self.correctstrtolabel(str(self.currentsum)))
            elif self.toplText.get() != '0' and self.botlText.get() != '0':
                self.currentsum = self.operfunc(num, self.currentsum, float(self.botlText.get()))
                self.toplText.set(self.toplText.get() + self.correctstrtolabel(self.botlText.get()) + self.opertolabel(num))
                self.botlText.set(self.correctstrtolabel(str(self.currentsum)))
            elif self.toplText.get() != '0' and self.botlText.get() == '0':
                self.currentsum = self.operfunc(num, self.currentsum, float(self.botlText.get()))
                self.toplText.set(self.toplText.get() + self.correctstrtolabel(self.botlText.get()) + self.opertolabel(num))
                self.botlText.set(self.correctstrtolabel(str(self.currentsum)))
            self.lastinput = 'oper'
        elif num == 'Return' or num == 'equal':
            if self.toplText.get() == '0' and self.botlText.get() != '0':
                self.currentsum = self.operfunc(num, self.currentsum, float(self.botlText.get()))
                self.toplText.set(self.correctstrtolabel(self.botlText.get()) + " = ")
                self.botlText.set(self.correctstrtolabel(str(self.currentsum)))
            elif self.toplText.get() == '0' and self.botlText.get() == '0':
                self.currentsum += float(self.botlText.get())
                self.toplText.set(self.botlText.get() + " = ")
                self.botlText.set(str(self.currentsum).rstrip('0').rstrip('.'))
            elif self.toplText.get() != '0' and self.botlText.get() != '0':
                if self.toplText.get()[-2] == '+':
                    self.currentsum += float(self.botlText.get().rstrip('0').rstrip('.'))
                    self.toplText.set(self.toplText.get() + self.botlText.get().rstrip('0').rstrip('.') + " = ")
                    self.botlText.set(str(self.currentsum).rstrip('0').rstrip('.'))
            elif self.toplText.get() != '0' and self.botlText.get() == '0':
                if self.toplText.get()[-2] == '+':
                    self.currentsum += float(self.botlText.get())
                    self.toplText.set(self.toplText.get() + self.botlText.get() + " = ")
                    self.botlText.set(str(self.currentsum).rstrip('0').rstrip('.'))
            self.lastinput = 'Return'

    def operfunc(self, opertype, one=0.0, two=0.0):
        if opertype == 'plus':
            return one + two
        if opertype == 'minus':
            return one - two
        if opertype == 'asterisk':
            return one * two
        if opertype == 'slash':
            return one / two
        return

    def opertolabel(self, opertype):
        if opertype == 'plus':
            return ' + '
        if opertype == 'minus':
            return ' - '
        if opertype == 'asterisk':
            return ' × '
        if opertype == 'slash':
            return ' ÷ '
        return

    def correctstrtolabel(self, strnum):
        correctstr = strnum
        if correctstr != '0':
            if '.' in correctstr or ',' in correctstr:
                return correctstr.rstrip('0').rstrip('.')
            else:
                return correctstr
        else:
            return correctstr

    def canceloff(self):
        self.lastinput = ''
        self.currentsum = 0.0
        self.toplText.set('0')
        self.botlText.set('0')


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



def main():
    calc = CalcWindow(300, 300, 'Calc')
    calc.run()


if __name__ == '__main__':
    main()
