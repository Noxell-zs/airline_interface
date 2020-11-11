"""Operations with seat reservation.

Functions:
    res_confirm
        Choosing a destination.
    res_base
        Confirmation of reservation.
    res_last
        Choosing a seat.

"""

import zones
import planes
from global_objects import *
from tkinter import messagebox
from tkinter.ttk import Combobox

global res_menu


def res_last(place, num):
    """Confirmation of reservation."""
    my_zones[place].coefficient = num
    my_rates[-1].price = my_zones[place].coefficient

    if not messagebox.askyesno(
            message=f'{my_planes[place]} Пункт назначения {place}. Место '
                    f'{num}. Стоимость билета {my_rates[-1].price:.2f} '
                    f'руб. Оплатить?'):
        my_reserves[place].cancel(num)
        del my_rates[-1]
    res_menu.destroy()


def res_base(place, rate):
    """Choosing a seat."""

    if place not in my_planes:
        my_planes[place] = planes.Plane()
    if place not in my_zones:
        my_zones[place] = zones.Zone(my_planes[place].seats)
    if place not in my_reserves:
        my_reserves[place] = zones.Reserve(my_planes[place].seats)

    my_rates.append(planes.Rate(place, rate))

    def continue_click():
        """Click on button."""
        num = message.get()

        if num.isdigit():
            num = int(num)
            my_rates[-1].num = num

            if my_reserves[place].take(num):
                continue_base(num)

    def continue_base(num):
        """To confirmation of reservation."""
        lbl.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        txt.destroy()
        btn.destroy()
        res_last(place, num)

    lbl = tkinter.Label(res_menu,
                        font="Arial 10",
                        background='lightcyan',
                        width=window_x // 10,
                        text=my_planes[place])
    lbl.pack(pady=5)

    lbl2 = tkinter.Label(res_menu,
                         font="Arial 10",
                         background='lightcyan',
                         width=window_x // 10,
                         text=my_zones[place])
    lbl2.pack()

    lbl3 = tkinter.Label(res_menu,
                         background='cyan',
                         text=my_reserves[place])
    lbl3.pack(pady=5)

    lbl4 = tkinter.Label(res_menu,
                         font="Arial 10",
                         background='lightcyan',
                         height=1,
                         width=window_x // 10,
                         text='Введите свободное место')
    lbl4.pack(pady=5)

    message = tkinter.StringVar(res_menu)
    txt = tkinter.Entry(res_menu,
                        textvariable=message)
    txt.pack(pady=5)

    btn = tkinter.Button(res_menu,
                         font="Constantia 11",
                         background='darkblue',
                         foreground='azure',
                         text="Подтвердить",
                         command=continue_click)
    btn.pack(pady=5)

    btn2 = tkinter.Button(res_menu,
                          font="Constantia 11",
                          background='darkblue',
                          foreground='azure',
                          text="Назад",
                          command=res_menu.destroy)
    btn2.pack(side=tkinter.BOTTOM, pady=5)


def res_confirm():
    """Choosing a destination."""
    global res_menu
    res_menu = tkinter.Toplevel()
    res_menu.overrideredirect(True)
    res_menu.configure(background='lightcyan')
    x = menu.winfo_screenwidth() // 2
    y = menu.winfo_screenheight() // 2
    res_menu.geometry(f'{x}x{y}+{x // 2}+{y // 2}')

    def continue_confirm():
        """Click on button."""
        lbl.destroy()
        lbl2.destroy()
        txt.destroy()
        combo.destroy()
        btn.destroy()
        btn2.destroy()
        res_base(message.get(), message2.get())

    lbl = tkinter.Label(res_menu,
                        font="Arial 15",
                        background='lightcyan',
                        height=1,
                        width=window_x // 10,
                        text="Введите пункт назначения")
    lbl.pack(pady=5)
    message = tkinter.StringVar(res_menu)
    txt = tkinter.Entry(res_menu,
                        width=window_x // 10,
                        textvariable=message)
    txt.pack(pady=5)

    lbl2 = tkinter.Label(res_menu,
                         font="Arial 15",
                         background='lightcyan',
                         width=window_x // 10,
                         text="выберите тариф")
    lbl2.pack(pady=5)

    message2 = tkinter.StringVar(res_menu)
    combo = Combobox(res_menu,
                     width=window_x // 10,
                     textvariable=message2)
    combo['values'] = ('SAI154', 'BBB25', 'CCC9', 'DD4')
    combo.current(0)
    combo.pack(pady=5)

    btn = tkinter.Button(res_menu,
                         font="Constantia 11",
                         background='darkblue',
                         foreground='azure',
                         text="Подтвердить",
                         command=continue_confirm)
    btn.pack(pady=5)

    btn2 = tkinter.Button(res_menu,
                          font="Constantia 11",
                          background='darkblue',
                          foreground='azure',
                          text="Назад",
                          command=res_menu.destroy)
    btn2.pack(side=tkinter.BOTTOM, pady=5)
