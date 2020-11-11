"""Descriptions of the business process of reserve seats in the airline

Reservation of seat.
Cancel of reservation.

Run the main program:
    python -m main


:Author:
    Замолоцкий Семен Андреевич, КИ20-17/1б

"""

import about_box
from global_objects import *
from reservation import res_confirm
from cancel import cancel_confirm


def main():
    """Main module; example of menu."""

    btn_res = tkinter.Button(menu,
                             font="Constantia 20",
                             text="Забронировать место",
                             width=window_x // 20,
                             pady=1,
                             background='darkblue',
                             foreground='azure',
                             command=res_confirm)
    btn_res.pack(pady=5)

    btn_cancel = tkinter.Button(menu,
                                font="Constantia 20",
                                text="Отменить бронь",
                                width=window_x // 20,
                                pady=1,
                                background='darkblue',
                                foreground='azure',
                                command=cancel_confirm)
    btn_cancel.pack(pady=5)

    btn_exit = tkinter.Button(menu,
                              font="Constantia 20",
                              text="Выход",
                              width=window_x // 20,
                              pady=1,
                              background='darkblue',
                              foreground='azure',
                              command=menu.destroy)
    btn_exit.pack(pady=5)

    about = tkinter.Button(menu,
                           text="О программе",
                           background='darkblue',
                           foreground='azure',
                           command=about_box.main)
    about.pack(expand=1, anchor=tkinter.SW)

    menu.mainloop()


if __name__ == '__main__':
    main()
