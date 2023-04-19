from colorChord import *
from ToMidi import *


melody = []
# 第一句
melody.append(Note('14', duration=1))
melody.append(Note('24', duration=0.5))
melody.append(Note('34', duration=1))
melody.append(Note('24', duration=0.5))
melody.append(Note('14', duration=1))

melody.append(Note('3b4', duration=3))
melody.append(Note('0', duration=1))
# 第二句
melody.append(Note('3b4', duration=1))
melody.append(Note('44', duration=0.5))
melody.append(Note('54', duration=1))
melody.append(Note('44', duration=0.5))
melody.append(Note('3b4', duration=1))

melody.append(Note('34', duration=3))
melody.append(Note('0', duration=1))

# 第三句
melody.append(Note('34', duration=1))
melody.append(Note('4#4', duration=0.5))
melody.append(Note('54', duration=1))
melody.append(Note('44', duration=0.5))
melody.append(Note('3b4', duration=0.5))
melody.append(Note('0', duration=0.5))

melody.append(Note('3b4', duration=1))
melody.append(Note('44', duration=0.5))
melody.append(Note('4#4', duration=1))
melody.append(Note('34', duration=0.5))
melody.append(Note('24', duration=0.5))
melody.append(Note('0', duration=0.5))

melody.append(Note('24', duration=1))
melody.append(Note('34', duration=0.5))
melody.append(Note('44', duration=1))
melody.append(Note('3b4', duration=0.5))
melody.append(Note('2b4', duration=0.5))
melody.append(Note('0', duration=0.5))

melody.append(Note('5b4', duration=3))
melody.append(Note('0', duration=1))

mid = ToMidi()
mid.add_melody(melody)
mid.WriteToFile("test.mid")




