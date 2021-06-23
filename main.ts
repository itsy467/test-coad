input.onPinPressed(TouchPin.P0, function () {
    basic.clearScreen()
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        `)
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showLeds(`
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . # . # .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
})
input.onPinPressed(TouchPin.P2, function () {
    basic.clearScreen()
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # # .
        . . . # .
        . # # # .
        . # . . .
        . # # # .
        `)
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    basic.showLeds(`
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . # . # .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        `)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # # . .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showLeds(`
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # # . .
        `)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.clearScreen()
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . # # . .
        . . # . .
        . . # . .
        . . # . .
        `)
})
basic.forever(function () {
    basic.showLeds(`
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . # # .
        . # # . .
        # # . . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . # #
        . . # # .
        . # # . .
        # # . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . #
        . . . # #
        . . # # .
        . # # . .
        # # . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . # #
        . . # # .
        . # # . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . #
        . . . # #
        . . # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        . . . # #
        `)
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        `)
})
