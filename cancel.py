"""Operations with cancel of reservation.

Functions:
    cancel_confirm
        Cancel of reservation.

"""

from tkinter import messagebox
from global_objects import *


def cancel_confirm():
    """Cancel of reservation."""

    cancel_menu = tkinter.Toplevel()
    cancel_menu.overrideredirect(True)
    cancel_menu.configure(background='lightcyan')
    x = menu.winfo_screenwidth() // 2
    y = menu.winfo_screenheight() // 2
    cancel_menu.geometry(f'{x}x{y}+{x // 2}+{y // 2}')

    def cancel_click():
        """Click on button."""
        m = int(selected.get())
        my_reserves[my_rates[m].place].cancel(my_rates[m].num)
        del my_rates[m]

        cancel_menu.destroy()

        cancel_confirm()

    def cancel_back():
        """Back to the main menu."""
        lbl.destroy()
        btn.destroy()
        btn2.destroy()

        for j in sel_list:
            j.destroy()

        cancel_menu.destroy()

    selected = tkinter.IntVar(cancel_menu)
    sel_list = []

    for n, i in enumerate(my_rates):
        sel_list.append(tkinter.Radiobutton(
            cancel_menu,
            font="Arial 10",
            text=f'Билет {n + 1}. {my_planes[i.place]} Пункт назначения '
                 f'{i.place}. Место {i.num}. Стоимость билета '
                 f'{i.price:.2f} руб.',
            value=n,
            justify=tkinter.LEFT,
            variable=selected,
            background='lightcyan'))

        sel_list[-1].pack(pady=5)

    lbl = tkinter.Label(cancel_menu,
                        font="Arial 10",
                        background='lightcyan',
                        text='Выберите номер билета для отмены брони')
    lbl.pack(pady=5)

    btn = tkinter.Button(cancel_menu,
                         font="Constantia 11",
                         background='darkblue',
                         foreground='azure',
                         text="Подтвердить",
                         command=cancel_click)
    btn.pack(pady=5)

    btn2 = tkinter.Button(cancel_menu,
                          font="Constantia 11",
                          background='darkblue',
                          foreground='azure',
                          text="Назад",
                          command=cancel_back)
    btn2.pack(pady=5)

    if not my_rates:
        messagebox.showinfo(message='Нет забронированных билетов')
        cancel_back()
