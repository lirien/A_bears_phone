import sys
sys.path.append('app')
from sound_manager import SoundManager

sound = SoundManager()
sound.play(sys.argv[1])
