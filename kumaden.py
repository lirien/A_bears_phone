import time
import sys
sys.path.append('app')
from game_state import GameState

DEBOUNCE = 0.1

def main():
    state = GameState()
    while True:
        state.update()
        time.sleep(DEBOUNCE)


main()
