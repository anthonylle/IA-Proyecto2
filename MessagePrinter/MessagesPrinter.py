from ConsoleControl.ConsoleControl import ConsoleControl

"""
Created on Mon Nov 12 02:38:10 2018

@author: Jake
"""

# class to print messages in console with a specific style 
class MessagePrinter(ConsoleControl):
    
    #--------------------------------------------------------------------------
    #input : a string, 'cls' i for windows and 'clear' for ubunrun or other
    #function: constructor
    def __init__(self, system):
        ConsoleControl.__init__(self, system)
        
    #--------------------------------------------------------------------------
    #input : a string with the text to show
    #function: get a string value from the console, printer a little message
    #          always with yellow color
    #output: a string value
    def input_option(self, message):
        self.font_selector("bright","","yellow")
        print(message,end="")
        my_input = input()
        self.reset_all()
        return my_input   
    
    #--------------------------------------------------------------------------
    #input : a string with the message
    #function: print alert message in the console
    #          always with red color
    #output: none
    def alert(self, message):
        self.font_selector("bright","","red")
        print(message)
        self.reset_all()
 
    #--------------------------------------------------------------------------
    #input : three string with the style and other with the message
    #function: print simple message in console, with a specific style
    #output: none       
    def print_message(self, style, back, fore, message):    
        self.font_selector(style,back, fore)
        print(message)
        self.reset_all()
        
    #--------------------------------------------------------------------------
    #input : three string with the style and other with the message
    #function: to clear the console after print simple message in console, with a specific style, 
    #output: none 
    def clear_print(self, style, back, fore, message):            
        self.clear_console()
        self.font_selector(style,back, fore)
        print(message)
        self.reset_all()            


#http://patorjk.com/software/taag/#p=display&v=0&f=Big&t=