import sys
import tty
import termios



# 💡 Ce script transforme les flèches directionnelles en n, s, e, w, cette fonction ne touche pas au moteur du jeu actuel.
def get_arrow_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)
        if ch1 == "\x1b":  # Séquence d'échappement
            ch2 = sys.stdin.read(1)
            if ch2 == "[":
                ch3 = sys.stdin.read(1)
                if ch3 == "A":
                    return "n"  # Flèche haut
                elif ch3 == "B":
                    return "s"  # Flèche bas
                elif ch3 == "C":
                    return "e"  # Flèche droite
                elif ch3 == "D":
                    return "w"  # Flèche gauche
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return None
