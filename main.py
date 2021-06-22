def on_button_pressed_a():
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . # . # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . # . # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . . .
        . # # . .
        . # . . .
        . # # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # # . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . . .
        . # # . .
        . # . . .
        . # # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # # . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
