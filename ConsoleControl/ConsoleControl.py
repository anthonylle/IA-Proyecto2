from colorama import init, Fore, Back, Style, Cursor
import os
"""
Created on Mon Nov 12 03:19:34 2018
https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html
@author: Jake
"""

class ConsoleControl(object):
    
        # cls i for windows
        def __init__(self, system = 'cls'):
            init()
            self.system = system
        
        def fore_color(self, color = "reset"):
            
            print(Fore.RESET, end="")
            if color == "black":
                print(Fore.BLACK,end="")
            
            elif color == "red":
                print(Fore.RED,end="")
            
            elif color == "green":
                print(Fore.GREEN,end="")
            
            elif color == "yellow":
                print(Fore.YELLOW,end="")
             
            elif color == "blue":
                print(Fore.BLUE,end="")
  
            elif color == "magenta":
                print(Fore.MAGENTA,end="")
              
            elif color == "cyan":
                print(Fore.CYAN,end="")
              
            elif color == "white":
                print(Fore.WHITE,end="")
        
        def back_color(self, color = "reset"):
            print(Back.RESET,end="")
            if color == "black":
                print(Back.BLACK,end="")
                
            elif color == "red":
                print(Back.RED,end="")
                
            elif color == "green":
                print(Back.GREEN,end="")
                
            elif color == "yellow":
                print(Back.YELLOW,end="")
                 
            elif color == "blue":
                print(Back.BLUE,end="")
                  
            elif color == "magenta":
                print(Back.MAGENTA,end="")
                  
            elif color == "cyan":
                print(Back.CYAN,end="")
                  
            elif color == "white":
                print(Back.WHITE,end="")
               
        
        def style_selector(self, style = "reset"):
            style = str(style)
            print(Style.RESET_ALL , end="")
            if style == "dim":
                print(Style.DIM,end="")
                
            elif style == "bringht":
                print(Style.BRIGHT,end="")

            elif style == "normal":
                print(Style.NORMAL,end="")  

        def font_selector(self, style, back, fore):
            self.style_selector(style)
            self.fore_color(fore)
            self.back_color(back)
          
        def clear_console(self):
            os.system(self.system)
           
            
        def cursor_position(self, row, column):
            print(Cursor.POS(row,column),end="")
            
        def cursor_position2(self, row, column):
            print(Cursor.UP(row)+Cursor.FORWARD(column), end="")   
            
        def reset_all(self):
            print(Back.RESET,end="")
            print(Fore.RESET, end="")
            print(Style.RESET_ALL, end="")