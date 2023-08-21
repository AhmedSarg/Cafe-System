from a_splash_screen import SplashScreen
from b_login_screen import LoginScreen
import sys

sys.path.insert(0, "values")
sys.path.insert(0, "icons")
from tkinter import *
from customtkinter import *
from fonts import *
from colors import *

splashScreen = SplashScreen()


def splashToLogin():
    splashScreen.root.destroy()
    LoginScreen()


splashScreen.root.after(1000, splashToLogin)

splashScreen.loop()
