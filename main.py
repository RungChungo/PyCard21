cards=[" A"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q"," K"]
suits=["\u2660","\u2665","\u2667","\u2662"]

def prRed(skk): return ("\x1b[38;2;255;0;0m\x1b[48;2;255;255;255m{}\033[00m" .format(skk))

def prBlk(skk): return ("\x1b[38;2;0;0;0m\x1b[48;2;255;255;255m{}\033[00m" .format(skk))

