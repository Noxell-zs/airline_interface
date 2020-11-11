"""Initialization of graphic interface."""

import tkinter


menu = tkinter.Tk()
menu.title('Airline')
window_x = menu.winfo_screenwidth() // 2
window_y = menu.winfo_screenheight() // 2
menu.configure(background='lightcyan')
menu.iconbitmap(r'.\icon.ico')

menu.geometry(f'{window_x}x{window_y}+{window_x//2}+{window_y//2}')

my_planes = {}
my_reserves = {}
my_zones = {}
my_rates = []
