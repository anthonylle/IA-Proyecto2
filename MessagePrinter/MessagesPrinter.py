from ConsoleControl.ConsoleControl import ConsoleControl

"""
Created on Mon Nov 12 02:38:10 2018

@author: Jake
"""

class MessagePrinter(ConsoleControl):
    
    def __init__(self, system):
        ConsoleControl.__init__(self, system)
        
        
    def input_option(self, message):
        self.font_selector("bright","","yellow")
        print(message,end="")
        my_input = input()
        self.reset_all()
        return my_input   

    def alert(self, message):
        self.font_selector("bright","","red")
        print(message)
        self.reset_all()
        
    def print_message(self, style, back, fore, message):    
        self.font_selector(style,back, fore)
        print(message)
        self.reset_all()

    def clear_print(self, style, back, fore, message):            
        self.clear_console()
        self.font_selector(style,back, fore)
        print(message)
        self.reset_all()            


#http://patorjk.com/software/taag/#p=display&v=0&f=Big&t=