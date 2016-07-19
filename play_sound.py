import sys
sys.path.append('app')
from sound_manager import SoundManager

manager = SoundManager()
for sound in sys.argv[1:]:
    manager.play(sound)
