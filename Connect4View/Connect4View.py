from MessagePrinter.MessagesPrinter import MessagePrinter

# class to use as part game's view 
class Connect4View(MessagePrinter):
    #--------------------------------------------------------------------------
    #input : a string, 'cls' i for windows and 'clear' for ubunrun or other
    #function: constructor, store great messages
    def __init__(self, system):
        
        MessagePrinter.__init__(self, system)
        """
        sets all the strings able to be print furter 
        """
        self.welcome_message = "".join([ " __          __  _                                          \n",
                                        " \ \        / / | |                                         \n",
                                        "  \ \  /\  / /__| | ___ ___  _ __ ___   ___                 \n",
                                        "   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \                \n",
                                        "    \  /\  /  __/ | (_| (_) | | | | | |  __/                \n",
                                        "     \/  \/ \___|_|\___\___/|_| |_| |_|\___|                \n",
                                        "                   _                                        \n",
                                        "                  | |                                       \n",
                                        "                  | |_ ___                                  \n",
                                        "                  | __/ _ \                                 \n",
                                        "                  | || (_) |                                \n",
                                        "                   \__\___/                                 \n",
                                        "                                                            \n",
                                        "                                  _     _  _                \n",
                                        "                                 | |   | || |               \n",
                                        "   ___ ___  _ __  _ __   ___  ___| |_  | || |_              \n",
                                        "  / __/ _ \| '_ \| '_ \ / _ \/ __| __| |__   _|             \n",
                                        " | (_| (_) | | | | | | |  __/ (__| |_     | |               \n",
                                        "  \___\___/|_| |_|_| |_|\___|\___|\__|    |_|    \n\n"])

        self.title = "".join([  "                                  _     _  _     \n",
                                "                                 | |   | || |    \n",
                                "   ___ ___  _ __  _ __   ___  ___| |_  | || |_   \n",
                                "  / __/ _ \| '_ \| '_ \ / _ \/ __| __| |__   _|  \n",
                                " | (_| (_) | | | | | | |  __/ (__| |_     | |    \n",
                                "  \___\___/|_| |_|_| |_|\___|\___|\__|    |_|  \n\n"])
    
        self.winner = "".join([" __     __         _                                 \n",
                                " \ \   / /        ( )                                \n",
                                "  \ \_/ /__  _   _|/__   _____  __      _____  _ __  \n",
                                "   \   / _ \| | | | \ \ / / _ \ \ \ /\ / / _ \| '_ \ \n",
                                "    | | (_) | |_| |  \ V /  __/  \ V  V / (_) | | | |\n",
                                "    |_|\___/ \__,_|   \_/ \___|   \_/\_/ \___/|_| |_|\n",
                                "                                                     \n\n" ])
    
        self.lost = "".join([" __     __           _                       _               _   \n",
                            " \ \   / /          | |                     | |             | |  \n",
                            "  \ \_/ /__  _   _  | |__   __ ___   _____  | |     ___  ___| |_ \n",
                            "   \   / _ \| | | | | '_ \ / _` \ \ / / _ \ | |    / _ \/ __| __|\n",
                            "    | | (_) | |_| | | | | | (_| |\ V /  __/ | |___| (_) \__ \ |_ \n",
                            "    |_|\___/ \__,_| |_| |_|\__,_| \_/ \___| |______\___/|___/\__|\n",
                            "                                                                 \n\n"])
                            
        self.draw = "".join(["  _____                     \n",
                            " |  __ \                    \n",
                            " | |  | |_ __ __ ___      __\n",
                            " | |  | | '__/ _` \ \ /\ / /\n",
                            " | |__| | | | (_| |\ V  V / \n",
                            " |_____/|_|  \__,_| \_/\_/  \n",
                            "                            \n\n"])                            
    
            
        self.main_menu = "".join([" -------------------  Main menu --------------------\n\n",
                                  "       >>> 1. New game\n\n",
                                  "       >>> 2. How to play\n\n",
                                  "       >>> 3. Exit\n\n"])

        self.new_game_menu = "".join([" ----------------- New game  --------------------\n\n",
                                      "         >>> 1. Type of game\n\n",
                                      "         >>> 2. Level game\n\n",
                                      "         >>> 3. Level game\n\n",
                                      "         >>> 4. Start\n\n",
                                      "         >>> 5. Back\n\n"])

        self.type_game_menu = "".join([" ----------------  Type of game -----------------\n\n",
                                       "         >>> 1. Computer vs computer\n\n",
                                       "         >>> 2. Human vs human\n\n" ,
                                       "         >>> 3. Human vs Computer\n\n",
                                       "         >>> 4. Back\n\n"])
    
        self.how_to_play = "".join([" ----------------- How to play  -----------------\n\n",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n ",
                                    " xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"])
            
        self.player1_wins_title = "".join(["__________.__                            ____   __      __.__               \n", 
                                           "\______   \  | _____  ___.__. __________/_   | /  \    /  \__| ____   ______\n", 
                                           " |     ___/  | \__  \<   |  |/ __ \_  __ \   | \   \/\/   /  |/    \ /  ___/\n",
                                           " |    |   |  |__/ __ \\\___  \  ___/|  | \/   |  \        /|  |   |  \\\___ \ \n", 
                                           " |____|   |____(____  / ____|\___  >__|  |___|   \__/\  / |__|___|  /____  >\n", 
                                           "                    \/\/         \/                   \/          \/     \/ \n"])

        self.player2_wins_title = "".join(["__________.__                           ________     __      __.__               \n",
                                           "\______   \  | _____  ___.__. __________\_____  \   /  \    /  \__| ____   ______\n", 
                                           " |     ___/  | \__  \<   |  |/ __ \_  __ \/  ____/  \   \/\/   /  |/    \ /  ___/\n",
                                           " |    |   |  |__/ __ \\\___  \  ___/|  | \/       \   \        /|  |   |  \\\___ \ \n", 
                                           " |____|   |____(____  / ____|\___  >__|  \_______ \   \__/\  / |__|___|  /____  >\n", 
                                           "                    \/\/         \/             \/         \/          \/     \/ \n"])
    
    #--------------------------------------------------------------------------
    #input : none
    #function: print the tittle
    #output: none
    def view_title(self):
        """
            Prints the Connect4 title
        """
        self.clear_print("bright","","cyan", self.title)

    #--------------------------------------------------------------------------
    #input : none
    #function: print the winner
    #output: none        
    def view_winner(self):
        """
            Prints You've Von title
        """
        self.clear_console()
        self.clear_print("bright","","yellow",self.winner)
        self.input_option(self,">>> Main menu: ")

    #--------------------------------------------------------------------------
    #input : none
    #function: print the lost
    #output: none
    def view_lost(self):
        """
            Prints You've Lost title
        """
        self.clear_console()
        self.alert(self.lost)
        self.input_option(self,">>> Main menu: ")

    #--------------------------------------------------------------------------
    #input : none
    #function: print draw message
    #output: none       
    def view_draw(self):
        """
            Prints Draw title
        """
        self.clear_console()
        self.alert(self.draw)
        self.input_option(">>> Main menu: ")
 
    #--------------------------------------------------------------------------
    #input : none
    #function: print a menu with input option
    #output: none       
    def view_menu(self, menu, space):
        """
            Prints in console the menu title
        """
        #self.view_title()
        self.print_message("bright","","white", menu)
        option = self.input_option(space)
        return option
    #--------------------------------------------------------------------------
    #input : none
    #function: print the main menu
    #output: none     
    def view_main_menu(self):
        self.clear_console()
        self.print_message("bright","","cyan", self.welcome_message)
        return self.view_menu(self.main_menu,"       >>> ")

    #--------------------------------------------------------------------------
    #input : none
    #function: print the new game menu
    #output: none  
    def view_new_game_menu(self):
        """
            Prints the new menu title
        """
        self.view_title()
        return self.view_menu(self.new_game_menu, "         >>> ")

    #--------------------------------------------------------------------------
    #input : none
    #function: print the type game menu
    #output: none     
    def view_type_game_menu(self):
        """
            Prints type of the game menu 
        """
        self.view_title()
        return self.view_menu(self.type_game_menu, "         >>> ")
    #--------------------------------------------------------------------------
    #input : none
    #function: print thow to play
    #output: none     
    def view_how_to_play(self):
        """
            Prints how to play menu
        """
        self.view_title()
        return self.view_menu(self.how_to_play,">>> Back [enter]:  ")

    #--------------------------------------------------------------------------
    #input : none
    #function: asks for column option
    #output: none     
    def column_option(self):
        """
            Prints select a number column input
        """
        return self.input_option(">>>> Select a number column: ")
 
    #--------------------------------------------------------------------------
    #input : none
    #function: asks for the level game
    #output: none    
    def select_level(self):
        """
            Prints select level input
        """
        return int(self.input_option(">>>> Select level (1 - 4): "))
        
    #--------------------------------------------------------------------------
    #input : none
    #function: print invalid option
    #output: none              
    def invalid_option(self):
        """
            Prints in red invalid option
        """
        self.alert("___    Invalid option D:  ____")

    def player1_wins(self, style, back, fore):
        """
            #input : none
            #function: print the wiiner 2
            #output: none 
            Prints Player2 Wins title
        """
        self.clear_console()
        self.font_selector(style,back, fore)
        print(self.player1_wins_title)
        self.reset_all()
        

    def player2_wins(self, style, back, fore):
        """
            #input : none
            #function: print the wiiner 1
            #output: none 
            Prints Player2 Wins title
        """
        self.clear_console()
        self.font_selector(style,back, fore)
        print(self.player2_wins_title)
        self.reset_all()        
        