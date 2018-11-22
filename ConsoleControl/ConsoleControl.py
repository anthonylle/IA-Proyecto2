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
            self.system = system
        
        def fore_color(self, color = "reset"):
            
            print(Fore.RESET)
            if color == "black":
                print(Fore.BLACK)
            
            elif color == "red":
                print(Fore.RED)
            
            elif color == "green":
                print(Fore.GREEN)
            
            elif color == "yellow":
                print(Fore.YELLOW)
             
            elif color == "blue":
                print(Fore.BLUE)
  
            elif color == "magenta":
                print(Fore.MAGENTA)
              
            elif color == "cyan":
                print(Fore.CYAN)
              
            elif color == "white":
                print(Fore.WHITE)
        
        def back_color(self, color = "reset"):
            print(Back.RESET)
            if color == "black":
                print(Back.BLACK)
                
            elif color == "red":
                print(Back.RED)
                
            elif color == "green":
                print(Back.GREEN)
                
            elif color == "yellow":
                print(Back.YELLOW)
                 
            elif color == "blue":
                print(Back.BLUE)
                  
            elif color == "magenta":
                print(Back.MAGENTA)
                  
            elif color == "cyan":
                print(Back.CYAN)
                  
            elif color == "white":
                print(Back.WHITE)
               
        
        def style_selector(self, style = "reset"):
            style = str(style)
            print(Style.RESET_ALL)
            if style == "dim":
                print(Style.DIM)
                
            elif style == "bringht":
                print(Style.BRIGHT)

            elif style == "normal":
                print(Style.NORMAL)  

        def font_selector(self, style, back, fore):
            self.style_selector(style)
            self.fore_color(fore)
            self.back_color(back)
          
        def clear_console(self):
            os.system(self.system)
           
            
        def cursor_position(self, row, column):
            print(Cursor.POS(row,column))
            
        def cursor_position2(self, row, column):
            print(Cursor.UP(row)+Cursor.FORWARD(column))   
            
        def reset_all(self):
            self.back_color()
            self.fore_color()
            self.style_selector()