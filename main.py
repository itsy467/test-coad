def on_pin_pressed_p0():
    basic.clear_screen()
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        """)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
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

def on_pin_pressed_p2():
    basic.clear_screen()
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # # .
        . . . # .
        . # # # .
        . # . . .
        . # # # .
        """)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
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
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
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
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        """)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . . .
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
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . . .
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

def on_pin_pressed_p1():
    basic.clear_screen()
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # # . .
        . . # . .
        . . # . .
        . . # . .
        """)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    basic.show_leds("""
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # # .
        . # # . .
        # # . . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . # #
        . . # # .
        . # # . .
        # # . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . #
        . . . # #
        . . # # .
        . # # . .
        # # . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . # #
        . . # # .
        . # # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . . # #
        . . # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        . . . # #
        """)
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        """)
basic.forever(on_forever)
