#
# PiControl entry point

def start():

    # Init the screen
    cad = pifacecad.PiFaceCAD()
    cad.lcd.blink_off()
    cad.lcd.cursor_off()





if __name__ == "__main__":
    start()
