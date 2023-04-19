import midiutil


class Note:
    pitch: int
    start: float
    duration: float

    # 字典
    note_dict = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    note_dict.update({'Db': 1, 'Eb': 3, 'Gb': 6, 'Ab': 8, 'Bb': 10})
    note_dict.update({'1': 0, '2': 2, '3': 4, '4': 5, '5': 7, '6': 9, '7': 11})
    note_dict.update({'1#': 1, '2#': 3, '4#': 6, '5#': 8, '6#': 10})
    note_dict.update({'2b': 1, '3b': 3, '5b':6 ,'6b': 8, '7b': 10})

    def __init__(self, pitch: str, duration = -1.0, start = -1.0, volume = 100):
        if pitch == '0':
            self.pitch = 0
            self.volume = 0
        else:
            self.pitch = self.Convert_Note_Str_to_Int(pitch)
            self.volume = volume
        self.duration = duration
        self.start = start

    def Convert_Note_Str_to_Int(self, notename: str) -> int:
        # 分割出音符和八度
        note = notename[0:-1]
        octave = notename[-1]

        octave = int(octave)
        # 检查音符和八度是否合法
        if note not in self.note_dict.keys():
            raise ValueError('音符不合法')
        if octave < 0 or octave > 9:
            raise ValueError('八度不合法')
        return self.note_dict[note] + (octave + 1) * 12
    
    def Convert_Note_Int_to_Str(self, noteint: int) -> str:
        # 检查音符是否合法
        if noteint < 0 or noteint > 119:
            raise ValueError('音符不合法')
        note = self.note_dict.keys()[noteint % 12]
        octave = noteint // 12 - 1
        return note + str(octave)


# BUG: 如何初始化
# BUG: 如何控制音量
class Chord:
    notes: list[Note]
    start: float
    duration: float
    def __init__(self, notes: list[Note]):
        self.notes = notes

class ToMidi:
    track_melody = []
    track_chords = []
    midiFile: midiutil.MIDIFile


    def __init__(self):
        self.midiFile = midiutil.MIDIFile(2)
        self.midiFile.addTrackName(0, 0, "Melody")
        self.midiFile.addTrackName(1, 0, "Chords")
        self.midiFile.addTempo(0, 0, 120)
        self.midiFile.addTempo(1, 0, 120)
        # 旋律轨：钢琴
        self.midiFile.addProgramChange(0, 0, 0, 0) # 0:钢琴
        # 和弦轨：弦乐
        self.midiFile.addProgramChange(1, 0, 0, 40) # 40:弦乐
    
    def add_melody(self, notes:list[Note]):
        self.track_melody = notes

    def add_chords(self, chords:list[Chord]):
        self.track_chords = chords

    def WriteToFile(self, filename:str):
        time = 0
        for note in self.track_melody:
            if note.start < 0:
                note.start = time
            else:
                time = note.start
            if note.duration < 0:
                raise ValueError('音符时值不合法')
            self.midiFile.addNote(0, 0, note.pitch, time, note.duration, note.volume)
            time = time + note.duration

        time = 0
        for chord in self.track_chords:
            if chord.start < 0:
                chord.start = time
            else:
                time = chord.start
            if chord.duration < 0:
                raise ValueError('和弦时值不合法')
            for note in chord.notes:
                self.midiFile.addNote(1, 0, note.pitch, time, note.duration, note.volume)
            time = time + note.duration
        with open(filename, "wb") as output_file:
            self.midiFile.writeFile(output_file)


    
    
