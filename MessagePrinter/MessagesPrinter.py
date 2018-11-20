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
        print("_______"+message+"_______")
   

        
    def welcome_message(self, style, back, fore):
            
            self.clear_console()
            self.font_selector(style,back, fore)
            print(" __          __  _                                          ")                                          
            print(" \ \        / / | |                                         ")                                           
            print("  \ \  /\  / /__| | ___ ___  _ __ ___   ___                 ")                   
            print("   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \                ")           
            print("    \  /\  /  __/ | (_| (_) | | | | | |  __/                ")                  
            print("     \/  \/ \___|_|\___\___/|_| |_| |_|\___|                ")                                                                                
            print("                   _                                        ")                                                                                                                         
            print("                  | |                                       ")                                         
            print("                  | |_ ___                                  ")                                   
            print("                  | __/ _ \                                 ")                                  
            print("                  | || (_) |                                ")                                   
            print("                   \__\___/                                 ")                                 
            print("                                                            ")                                                                                                                          
            print("                                  _     _  _                ")                 
            print("                                 | |   | || |               ")                 
            print("   ___ ___  _ __  _ __   ___  ___| |_  | || |_              ")               
            print("  / __/ _ \| '_ \| '_ \ / _ \/ __| __| |__   _|             ")               
            print(" | (_| (_) | | | | | | |  __/ (__| |_     | |               ")               
            print("  \___\___/|_| |_|_| |_|\___|\___|\__|    |_|               ")        
            self.reset_all()

    def title(self, style, back, fore):
        self.font_selector(style,back, fore)
        print("                                  _     _  _                ")                 
        print("                                 | |   | || |               ")                 
        print("   ___ ___  _ __  _ __   ___  ___| |_  | || |_              ")               
        print("  / __/ _ \| '_ \| '_ \ / _ \/ __| __| |__   _|             ")               
        print(" | (_| (_) | | | | | | |  __/ (__| |_     | |               ")               
        print("  \___\___/|_| |_|_| |_|\___|\___|\__|    |_|               ")        
        self.reset_all()
        

#http://patorjk.com/software/taag/#p=display&v=0&f=Big&t=