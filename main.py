from MultiTerm import *
termsize = os.get_terminal_size()
termsize = (termsize.columns, termsize.lines)
SCREEN = Screen(termsize,(0,0))
Ground = canvas((termsize[0],4))
Ground.fill("█")
SCREEN.blit(str(Ground),(0,termsize[1]-4),Fore.GREEN,RESET)
particles = []

while True:
    SCREEN.draw()
