import sys
sys.path.append('app')
from game_state import GameState

def main():
    state = GameState()
    while True:
        state.update()

main()
