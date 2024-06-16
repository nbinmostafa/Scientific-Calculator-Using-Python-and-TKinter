'''
Name: Nafi Bin Mostafa 
Date: 24/05/2024
Project: Scientefic Calculator Using TKinter
'''
from tkinter import *
import math
import random 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Calc:
  def __init__(self,master):
    #Screen Configuration
    
    self.master = master  
    master.title('Calculator')
    master.geometry('1070x486')
    master.configure(bg='#151515')

    #EntryBox
    self.entrybox  = Entry(master,
                           bg = '#EEEEEE',
                           bd = 10, 
                           font=('Helvetica',30), 
                           width= 30, 
                           relief = 'sunken')
    self.entrybox.grid(row=0, column= 1, columnspan= 5)
  
    #Buttons
    self.create_buttons()

    

   #Create the Buttons
  def create_buttons(self):
    #Button Assignment/Positioning
    button_text = [ 
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),('+',1,3),('sin',1,4),('√',1,5),('!',1,6),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),('-',2,3),('cos',2,4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),('x',3,3),('tan',3,4),('Deg',3,5),('rad', 3, 6),
    ('π', 4, 0),('0', 4, 1), ('.', 4, 2),('÷',4,3),('=', 4, 4),('^n', 4, 5),('⚅', 4, 6),    
    ] 
    special_buttons = [('Clear',2,5),('Del', 2, 6),('=', 4, 4)]
    invest = [(('Investment Calculator',5,2))]

    
    #For Loop To Generate All Buttons (Except Special Buttons)
    for (text,row,col) in button_text:
      button = Button(self.master,
                      bg = '#D8AE7E',
                      font=('Helvetica',13,"bold"),
                      text=text,
                      command = lambda t=text:self.handle_button(t),relief='raised')
      button.grid(row=row, column=col, sticky='nsew')
      button.grid(row=row, column=col, padx=2, pady=10, ipadx=40, ipady=10)

    

    #For Loop To Generate Special Buttons
    for (text,r,c) in special_buttons:
      button =  button = Button(self.master,
                                bg='#F1E5D1',
                                font=('Helvetica',13,"bold"),
                                text=text,
                                command = lambda t= text : self.handle_button(t),relief='raised')
      button.grid(row=r, column=c,sticky = 'nsew')
      button.grid(row=r, column=c, padx=2, pady=10, ipadx=40, ipady=10)
    #Investment Calculator Button
    for (text,r,c) in invest:
      button = Button(self.master,
        bg='#F1E5D1',
        font=('Helvetica',13,"bold"),
        text=text,
        command = lambda t= text : self.handle_button(t),relief='raised')
      button.grid(row=r, column=2, columnspan= 3)
      button.grid(row=r, column=c, padx=2, pady=10, ipadx=40, ipady=10)

  
      
  #Buttons and Button Functionality:
  def handle_button(self,t ):
      exp = self.entrybox.get()
      if t.isdigit() or t =='.':
        self.add_to_entry(t)
      elif t in ['+','-','x','÷']:
        if t not in ['x','÷']:
          self.add_to_entry(f'{t}')
        if t == 'x':
          self.add_to_entry('*')
        if t == '÷':
          self.add_to_entry('/')
      elif t == 'Del':
        self.delete()
      elif t == '=':
        self.evaluate_exp()
      elif t in ['sin','cos','tan']:
        self.calculate_trig(t)      
      elif t == '√':
        try:
          expression = self.entrybox.get()
          answer = math.sqrt(float(expression))
          self.entrybox.delete(0,'end')
          self.entrybox.insert('end',answer)
        except Exception as e:
          self.entrybox.delete(0,'end')
          self.entrybox.insert('end','Error')
          
      elif t == '!':
        try:
          answer = math.factorial(int(exp))
          self.entrybox.delete(0,'end')
          self.entrybox.insert('end',answer)
        except Exception as e:
          self.entrybox.delete(0,'end')
          self.entrybox.insert('end','Error')
      elif t == 'π':
        current_text = self.entrybox.get()
        if current_text and current_text[-1].isdigit():
          self.add_to_entry('*')
        self.add_to_entry(str(math.pi))
      elif  t == "Clear":
        self.clear()
      elif t in ['Deg','rad']:
        try:
          if t == 'Deg':
            answer = math.degrees(eval(exp))
            self.entrybox.delete(0,'end')
            self.entrybox.insert('end',answer)
          elif t == 'rad':
            answer = math.radians(eval(exp))
            self.entrybox.delete(0,'end')
            self.entrybox.insert('end',answer)
        except Exception as e:
          self.entrybox.delete(0,'end')
          self.entrybox.insert('end','Error')
      elif t == "^n":
        self.add_to_entry('^')  
      elif t == '⚅':
        self.clear()
        dice = random.randint(1,6)
        self.add_to_entry(dice) 

      elif t == 'Investment Calculator':
        self.add_to_entry(t)
        self.switch_to_investment_calculator()

  
  #evaluate the expression for [+,-,x,÷,^]
  def evaluate_exp(self):
    try:
      expression = self.entrybox.get().replace('^','**')
      result = eval(expression)
      self.entrybox.delete(0,'end')
      self.entrybox.insert('end',str(result))
      return result

    except Exception as e:
      if str(e) in ['division by zero','float division by zero']:
        self.entrybox.delete(0,'end')
        self.entrybox.insert('end','0')
      else:
        self.entrybox.delete(0,'end')
        self.entrybox.insert('end','Error')
        

  #Add Number to EntryBox
  def add_to_entry(self,t):
    self.entrybox.insert('end', t)

  
  #erase the text(Del)
  def delete(self):
    current_entry = self.entrybox.get()
    if current_entry and current_entry != 'Error':
      self.entrybox.delete(len(current_entry)-1, 'end')
    else:
      self.entrybox.delete(0,'end')
      
  #Clear the EntryBox
  def clear(self):
    self.entrybox.delete(0,'end')


  #Evaluates Trig Function (Sin,Cos,Tan)
  def calculate_trig(self,func):
    try:
      value = float(self.entrybox.get())
      if func == 'sin':
        result = math.sin(math.radians(value))
      if func == 'cos':
        result = math.cos(math.radians(value))
      if func == 'tan':
        result = math.tan(math.radians(value))

      self.entrybox.delete(0,'end')
      self.entrybox.insert('end',str(result))

    except Exception as e:
      self.entrybox.delete(0,'end')
      self.entrybox.insert('end','Error')

  def switch_to_investment_calculator(self):
    self.master.withdraw()
    new_window = Toplevel(self.master)
    investment_calculator = Investment_Calc(new_window)



#Investment Calculator Class
class Investment_Calc:
  def __init__(self, master):
    #Screen Configuration
    self.master = master
    master.title('Investment Calculator')
    master.geometry('1100x486+100+100')
    master.configure(bg='#151515')
    
    #Elements of the screen
    #Title
    self.title = Label(master,
                       text="Investment Calculator",
                       bg='#151515', fg='#F1E5D1',
                       font=('Helvetica', 18, 'bold')).pack()
    
    #Data From User/Elements
    self.principal = Label(master,
                         text= 'Principal Amount:',bg='#151515', fg='#F1E5D1').place(x=50,y=40)
    self.p = Entry(self.master,font=('Helvetica', 16))
    self.p.place(x=180,y=35)
    self.rate = Label(self.master,bg='#151515', fg='#F1E5D1',text="Annual Interest Rate (%):")
    self.rate.place(x=20,y=85)
    self.r = Entry(self.master,font=('Helvetica',16))
    self.r.place(x=180,y=80)
    self.year = Label(self.master,bg='#151515', fg='#F1E5D1',text="Number of Years:").place(x=50,y=130)
    self.y = Entry(self.master,font=('Helvetica',16))
    self.y.place(x=180,y=130)


    
    self.result = Label(self.master,bg='#151515', fg='#F1E5D1',text="Result:",font=('Helvetica',24,'bold'))
    self.result.place(x=10,y=380)
    self.resultField = Entry(self.master,font=('Helvetica',24))
    self.resultField.config(state='disabled')
    self.resultField.place(x=180,y=380)

    

    
    #Calculate Button
    self.button = Button(self.master,
      bg = '#D8AE7E',
      font=('Helvetica',13,"bold"),
      text='Calculate',
      command = lambda :self.calculate_interest_simple(),
      relief= 'raised')
    self.button.place(x=235,y=190)

    
    #Switch Window Button
    self.switch_calculator = Button(self.master,
      bg = '#F1E5D1',
      font=('Helvetica',10,"bold"),
      text='GO BACK',
      command = lambda :self.switch_to_calculator(),
                             relief='raised')
    self.switch_calculator.place(x=245,y=250)
    

  def calculate_interest_simple(self):
    try:
      self.resultField.config(state='normal')
      self.resultField.delete(0,'end')
      p = float(self.p.get())
      r = float(self.r.get())
      t = int(self.y.get())
      
      interest = (p * r * t) / 100
      result = interest + p
      self.resultField.insert('end',f'${result}')
      self.plot_chart(p,r,t)
    
    except Exception as e:
      self.resultField.delete(0,'end')
      self.resultField.config(state='normal')
      self.resultField.insert('end',"Error: Invalid Input")
      self.resultField.config(state='disabled')


  
  def plot_chart(self,p,r,t):
    fig = Figure(figsize = (5, 4),dpi = 100) 
    plot1 = fig.add_subplot(111)

    # Clear existing canvas contents
    for child in self.master.children.values():
        if isinstance(child, FigureCanvasTkAgg):
            child.get_tk_widget().destroy()

    
    # Create a new canvas for the plot
    y = []
    x = []
    for year in range(1,t+1):
      x.append(year)
      interest = ((p*r*year)/100)
      result = p + interest
      y.append(result)
      plot1.bar(x,y,width= 0.5,align='edge',color= '#D8AE7E')
      

      
    plot2 = plot1.twinx()
    plot2.plot(x,y,color= '#D8AE7E')


    
    

    
    # Enhance aesthetics
    fig.patch.set_facecolor('#C0C0C0')
    plot1.set_xlabel('Number Of Year', labelpad= 0.000001)
    plot1.set_ylabel('Total Amount',labelpad= 10.0)
    plot1.set_title('Investment Growth',)
    plot1.grid(True)
    

    for i,value in enumerate(x):
      plot1.text( x[i], y[i], str(f'{y[i]:.2f}'))  
    

    canvas = FigureCanvasTkAgg(fig, master = self.master)
    canvas.draw()
    canvas.get_tk_widget().place(x=600,y=35)
    
  
  def switch_to_calculator(self):
    self.master.withdraw()
    new_window = Toplevel(self.master)
    calc = Calc(new_window)
    

#Main Program
if __name__ == '__main__':

  root = Tk()
  calculator = Calc(root)
  root.mainloop()