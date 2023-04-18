# load packages
import tkinter as tk

class Calculator:
    """
    Create a calculator GUI for simple operations
    """

    def __init__(self):
        self.expression = "" # temporary variable that updates the equation
        self.gui = tk.Tk()
        self.equation = tk.StringVar(self.gui) # the output shown in GUI
        self.clear_button = self.create_button('AC', self.clear) # to make dynamic


    def press(self, num):
        # concatenation of string
        self.expression += str(num)
    
        # update the expression by using set method
        self.equation.set(self.expression)

        # update clear button
        self.clear_button['text'] = 'C'

    def invert(self):
        self.equation.set(-float(self.equation.get()))            

    def percent(self):
        self.equation.set(str(float(self.equation.get()) / 100))
    
    def eval(self):
        try:
            print(self.expression)
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = self.equation.get()

        except:
            self.equation.set("error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")
        self.clear_button['text'] = 'AC'

    def create_button(self, text, command):
        return tk.Button(self.gui, text=text, bd=1, fg='grey', bg="red", command=command, height=5, width=5)

    def create_widgets(self):
        # Expression
        expression_field = tk.Entry(self.gui, textvariable=self.equation, width=12, font=('Times', 50), justify='right')
        expression_field.grid(columnspan=5, row=0)

        # clear, invert, percent
        self.clear_button.grid(row=1, column=0)

        invert = self.create_button(' +/- ', self.invert)
        invert.grid(row=1, column=1)

        percent = self.create_button(' % ', self.percent)
        percent.grid(row=1, column=2)

        # 1 - 9
        # numberpad = [['7', '8', '9'],
        #              ['4', '5', '6'],
        #              ['1', '2', '3']]

        for i in range(3, 0, -1):
            for j in range(1, 4):
                def updateLocalScope(i, j):
                    value = 3 * (i-1) + j
                    button = self.create_button(str(value), lambda: self.press(value))
                    button.grid(row=(-i+5), column=j-1)
                updateLocalScope(i, j)
    
        # 0, .
        button0 = tk.Button(self.gui, text='0', bd=1, fg='grey', bg="red", command=lambda: self.press(0), height=5, width=13)
        button0.grid(row=5, column=0, columnspan=2, ipadx=3)
    
        Decimal= self.create_button(' . ', lambda: self.press('.'))
        Decimal.grid(row=5, column=2)

        # Operator Column
        operators = ["/", "*", "-", "+"]

        for operator in operators:
            def updateLocalScope(operator):
                button = self.create_button(operator, lambda: self.press(operator))
                button.grid(row=operators.index(operator)+1, column=3)
            updateLocalScope(operator)
    
        equal = self.create_button(' = ', self.eval)
        equal.grid(row=5, column=3)

    def run(self):
        # Create a GUI window
        self.gui.configure(background="dark gray")
        self.gui.title("Simple Calculator")

        w = 315 # width for the Tk root
        h = 520 # height for the Tk root

        # get screen width and height
        ws = self.gui.winfo_screenwidth() # width of the screen
        hs = self.gui.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws*3/5 - 13) 
        y = (-hs)

        # set the dimensions of the screen 
        # and where it is placed
        self.gui.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.create_widgets()

        self.gui.mainloop()


calculator = Calculator()
calculator.run()