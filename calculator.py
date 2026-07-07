import tkinter
import math

button_values = [
  ["AC","+/-","%","÷"],
  ["7","8","9","×"],
  ["4","5","6","-"],
  ["1","2","3","+"],
  ["0",".","√","="]
]

right_symbols = ["÷", "×", "-", "+", "="]

top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5  (Counts how many inner lists i=are in the main list)
column_count = len(button_values[0]) #4  (counts how many items are in the first list)

#print(row_count)
#print(column_count)


#color scheme
color_light_blue = "#9EBEFF"
color_mild_blue = "#6394FF"
color_blue = "#2C67FF"
color_dark_blue = "#000845"
color_white = "white"




#window setup

window = tkinter.Tk()  #create window
window.withdraw()  #hides the window


window.title("calculator")
window.resizable(False, False)  #to make sure user cannot resize the window by dragging on the sides --- one false is for width and one is for height


frame = tkinter.Frame(window) #Placing the frame inside the parent i.e. (window)


#First component
label = tkinter.Label(frame, 
                      text="0", 
                      font=("Arial", 45), 
                      background=color_dark_blue,
                      foreground=color_white, 
                      anchor= "e",
                      width=column_count) #foreground=fontcolor

label.grid(row=0, 
           column=0, 
           columnspan = column_count,                #columnspan = how many columns the label should take  #we = west to east
           sticky="we") 


#buttons (remaining components)
for row in range(row_count):
  for column in range(column_count):          #Hence, for every row python checks all 4 columns
    value = button_values[row][column]        #receives button text from the list
    
    button = tkinter.Button(frame, 
                            text = value, 
                            font = ("Arial", 30),
                            width = column_count - 1, 
                            height = 1,
                            command = lambda value=value: button_clicked(value))
    
    if value in top_symbols:
      button.config(foreground=color_dark_blue, 
                   background=color_mild_blue)
    elif value in right_symbols:
      button.config(foreground=color_white,
                    background=color_light_blue)
    else:
      button.config(foreground=color_dark_blue,
                    background=color_blue)    

    button.grid(row=row+1, column=column, sticky="nsew")
       

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
  global A, B, operator
  A = "0"
  operator = None
  B = None

def format_num(num):
  return str(int(num)) if num.is_integer() else str(num)  

def button_clicked(value):
  global right_symbols, top_symbols, label, A, B, operator    #gloval is used to use a variable from outside the function, not a local new variable inside the function
  
  if value in right_symbols:
    
    if value == "=":
      if A is not None and operator is not None:
        B = label["text"]
        numA = float(A)
        numB = float(B)

        if operator == "+":
          label["text"] = format_num(numA + numB)

        elif operator  == "-":
          label["text"] = format_num(numA - numB)

        elif operator == "÷":
          label['text'] = format_num(numA/numB)

        elif operator == "×":
          label["text"] = format_num(numA*numB)   

        clear_all()    

    elif value in "÷×-+":
      if operator is None:
        A = label["text"]
        label["text"] = "0"
        B = "0"

      operator = value


  elif value in top_symbols:

    if value == "AC":
      clear_all()
      label["text"]="0"

    elif value == "+/-":
      x = label["text"]

      if x != "0":
        new_val = -float(x)                                    #covert text to float, multiply by -1 and convert back to str
        label["text"] = format_num(new_val)

    elif value =="%":
      x = label["text"]

      if x != "0":
        new_x = float(x)/100
        label["text"]= format_num(new_x)

  else: #digits or . or √
    if value == ".":
      if value not in label["text"]:
        label["text"]+= value

    elif value == "√":
      x = label["text"]

      if float(x)>=0:
        root = math.sqrt(float(x))
        label["text"] = format_num(root)

    elif value in "0123456789":
      if label["text"] == "0":
        label["text"] = value #replace 0    
      else:
        label["text"] += value  # append value



#center the window
window.update_idletasks() #Update window with new size dimensions whithout showing it
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

#format  (w)x(h)+(x)+(y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.deiconify() #Shows window again
window.mainloop() # Makes sure window stays open while the code runs



