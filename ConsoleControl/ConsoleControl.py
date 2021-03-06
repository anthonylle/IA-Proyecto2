from colorama import init, Fore, Back, Style, Cursor
import os
"""
Created on Mon Nov 12 03:19:34 2018
https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html
@author: Jake
"""

# class to control console's style letter's color, background's color and position 
class ConsoleControl(object):
    
    # cls i for windows and clear for ubunrun or other
    def __init__(self, system = 'cls'):
        init()
        self.system = system

    #--------------------------------------------------------------------------
    def fore_color(self, color = "reset"):
        """
            #input : color: a string with the letter's color
            #function: choose the letter's color
            #output: none    
            Recibes a color string and sets a font color stile
        """
        if( color == "" or color =="reset" ):
            
            print(Fore.RESET, end="")
            
        else:

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


    #--------------------------------------------------------------------------        
    def back_color(self, color = "reset"):
        """
          #input : color: a string with the backgrond's color
          #function: choose the backgrond's color in line console
          #output: none 
        """
        if( color == "" or color =="reset" ):
            print(Back.RESET,end="")
        else:
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

    #-------------------------------------------------------------------------- 
    def style_selector(self, style = "reset"):
        """
        #input : color: a string with the letter's style
        #function: choose the letter's style
        #output: none     
        """
        style = str(style)
        if style == "" or style == "reset":
            print(Style.RESET_ALL , end="")
        else:
            if style == "dim":
                print(Style.DIM,end="")
                
            elif style == "bringht":
                print(Style.BRIGHT,end="")
    
            elif style == "normal":
                print(Style.NORMAL,end="")  
    #--------------------------------------------------------------------------

    def font_selector(self, style, back, fore):
        """
            input : three string with style for console's line
            function: set style for console's line
            output: none
        """
        self.style_selector(style)
        self.fore_color(fore)
        self.back_color(back)
        
    #--------------------------------------------------------------------------
    
    def clear_console(self):
        """
            input : none
            function: clear all the console
            output: none  
        """
        os.system(self.system)

    #--------------------------------------------------------------------------
      
    def reset_all(self):
        """
            input : none
            function: set the original console's style
            output: none    
        """
        print(Back.RESET,Fore.RESET,Style.RESET_ALL,end="")