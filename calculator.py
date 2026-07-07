import tkinter

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

color_light_blue = "#9EBEFF"
color_mild_blue = "#6394FF"
color_blue = "#2C67FF"
color_dark_blue = "#000845"
color_white = "white"

#window setup

window = tkinter.Tk()  #create window
window.title("calculator")
window.resizable(False, False)  #to make sure user cannot resize the window by dragging on the sides --- one false is for width and one is for height

frame = tkinter.Frame(window) #Placing the frame inside the parent i.e. (window)
#First component
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_blue,
                      foreground=color_white) #foreground=fontcolor

label.grid(row=0, column=0)

for row in range(row_count):
  for column in range(column_count):          #Hence, for every row python checks all 4 columns
    value = button_values[row][column]        #receives button text from the list
    button = tkinter.Button(frame, text = value, font = ("Arial", 30),
                            width = column_count - 1, height = 1,
                            command = lambda value=value: button_clicked(value))
    button.grid(row=row+1, column=column)
       

frame.pack()

def button_clicked(value):
  pass

window.mainloop() # Makes sure window stays open while the code runs
