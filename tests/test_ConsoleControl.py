"""
    tests Consoleself.control Class
"""
from ConsoleControl.ConsoleControl import ConsoleControl
from colorama import init, Fore, Back, Style, Cursor
from unittest import mock
from io import StringIO
import os


class Test_ConsoleControl():

    init()
    control = ConsoleControl()
    #------------------ Fore color --------------------------------------------
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color(self, mock_stdout):
        
        self.control.fore_color("")
        assert (mock_stdout.getvalue() == Fore.RESET)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color0(self, mock_stdout):
        
        self.control.fore_color("black")
        assert (mock_stdout.getvalue() == Fore.BLACK)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color1(self, mock_stdout):
        
        self.control.fore_color("red")
        assert (mock_stdout.getvalue() == Fore.RED)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color2(self, mock_stdout):

        self.control.fore_color("green")
        assert (mock_stdout.getvalue() == Fore.GREEN)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color3(self, mock_stdout):

        self.control.fore_color("yellow")
        assert (mock_stdout.getvalue() == Fore.YELLOW)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color4(self, mock_stdout):

        self.control.fore_color("blue")
        assert (mock_stdout.getvalue() == Fore.BLUE)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color5(self, mock_stdout):
        
        self.control.fore_color("magenta")
        assert (mock_stdout.getvalue() == Fore.MAGENTA)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color6(self, mock_stdout):
        
        self.control.fore_color("cyan")
        assert (mock_stdout.getvalue() == Fore.CYAN)   
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fore_color7(self, mock_stdout):
        
        self.control.fore_color("white")
        assert (mock_stdout.getvalue() == Fore.WHITE) 

    #------------------ back_color --------------------------------------------
    
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color(self, mock_stdout):
        
        self.control.back_color("")
        assert (mock_stdout.getvalue() == Back.RESET)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color0(self, mock_stdout):
        
        self.control.back_color("black")
        assert (mock_stdout.getvalue() == Back.BLACK)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color1(self, mock_stdout):

        self.control.back_color("red")
        assert (mock_stdout.getvalue() == Back.RED)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color2(self, mock_stdout):

        self.control.back_color("green")
        assert (mock_stdout.getvalue() == Back.GREEN)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color3(self, mock_stdout):
        
        self.control.back_color("yellow")
        assert (mock_stdout.getvalue() == Back.YELLOW)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color4(self, mock_stdout):
        
        self.control.back_color("blue")
        assert (mock_stdout.getvalue() == Back.BLUE)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color5(self, mock_stdout):

        self.control.back_color("magenta")
        assert (mock_stdout.getvalue() == Back.MAGENTA)
         
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color6(self, mock_stdout):
        
        self.control.back_color("cyan")
        assert (mock_stdout.getvalue() == Back.CYAN)   
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_back_color7(self, mock_stdout):
        
        self.control.back_color("white")
        assert (mock_stdout.getvalue() == Back.WHITE)     
        
    #--------------------- style_selector -------------------------------------
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_style_selector1(self, mock_stdout):

        self.control.style_selector("dim")
        assert (mock_stdout.getvalue() == Style.DIM) 

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_style_selector2(self, mock_stdout):

        self.control.style_selector("bringht")
        assert (mock_stdout.getvalue() == Style.BRIGHT)     
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_style_selector3(self, mock_stdout):

        self.control.style_selector("normal")
        assert (mock_stdout.getvalue() == Style.NORMAL)  
 
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_style_selector4(self, mock_stdout):

        self.control.style_selector("")
        assert (mock_stdout.getvalue() == Style.RESET_ALL)  
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_style_selector5(self, mock_stdout):

        self.control.style_selector("reset")
        assert (mock_stdout.getvalue() == Style.RESET_ALL)
         
    #--------------------- font_selector --------------------------------------
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_font_selector(self,  mock_stdout):
        self.control.font_selector("","","")
        assert (mock_stdout.getvalue() == Style.RESET_ALL+Fore.RESET+Back.RESET)
        
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_font_selector2(self,  mock_stdout):
        self.control.font_selector("normal","white","white")
        assert (mock_stdout.getvalue() == Style.NORMAL+Fore.WHITE+Back.WHITE)        

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_font_selector3(self,  mock_stdout):
        self.control.font_selector("normal","black","black")
        assert (mock_stdout.getvalue() == Style.NORMAL+Fore.BLACK+Back.BLACK)
        
    #--------------------- font_selector --------------------------------------
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_reset_all(self,  mock_stdout): 
        
        self.control.reset_all()
        assert( mock_stdout.getvalue() == Back.RESET+' '+Fore.RESET+' '+Style.RESET_ALL)
        
        
    
    
    