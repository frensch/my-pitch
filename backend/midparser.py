import midi

class MidParser():
    #print (pattern)

    class NotesInfo():

        def __init__(self):
            self.vocalTrack = False
            self.countNotes = 0
            self.sumNotes = 0
            self.maxNote = 0
            self.minNote = 10000
            self.notesOn = []
            self.notesOnTime = []
            self.notesOffTime = []
            self.notesSiceLast = 0
            self.notesSilence = 0
            self.notesDuration = 0
            self.timelapsed = 0
            self.timelapsed = 0
            self.sumPitchDiff = 0
            self.instrument = 0
            self.notesSimultaneously = 0
            self.trackName = 'No Name'
            self.fileName = ''

    def __init__(self):
        self.notesInfos = []
        self.notesInfosVocal = []
        self.notesInfosNonVocal = []
        self.hasVocal = False
        self.lastPitch = 0
        

    def run(self, filename):
        self.hasVocal = False
        pattern = midi.read_midifile(filename)
        for track in pattern:
            #if len(track) < 200:
            #    continue
            #print ("track:" + str(len(track)))
            notesInfo = self.NotesInfo()
            notesInfo.fileName = filename
            for event in track:

                notesInfo.timelapsed = notesInfo.timelapsed + event.tick

                if issubclass(type(event), midi.ProgramChangeEvent):
                    if event.get_value() > 0:
                        notesInfo.instrument = event.get_value()


                if issubclass(type(event), midi.TrackNameEvent): #event.name == "Track Name":
                    notesInfo.trackName = event.text
                    if ("Vocal" in event.text or "vocal" in event.text or \
                    "Voice" in event.text or "voice" in event.text) \
                    and ("Back" not in event.text and "back" not in event.text):
                        #print(event.text)
                        notesInfo.vocalTrack = True
                        self.hasVocal = True
                        
                #if not notesInfo.vocalTrack:
                #    continue

                if issubclass(type(event), midi.NoteOnEvent):
                    if event.get_velocity() > 0:
                        if len(notesInfo.notesOn) == 0:
                            notesInfo.notesSilence = notesInfo.notesSilence + (notesInfo.timelapsed - notesInfo.notesSiceLast)
                            notesInfo.notesSiceLast = 0
                        #print('noteon',event.get_pitch(), notesInfo.timelapsed)
                        notesInfo.countNotes = notesInfo.countNotes + 1
                        notesInfo.sumNotes = notesInfo.sumNotes + event.get_pitch()
                        if event.get_pitch() < notesInfo.minNote:
                            notesInfo.minNote = event.get_pitch()
                        if event.get_pitch() > notesInfo.maxNote:
                            notesInfo.maxNote = event.get_pitch()
                        notesInfo.notesOn.append(event.get_pitch())
                        notesInfo.notesOnTime.append(notesInfo.timelapsed)
                        notesInfo.sumPitchDiff = notesInfo.sumPitchDiff + abs(event.get_pitch() - self.lastPitch)
                        self.lastPitch = event.get_pitch()
                        if len(notesInfo.notesOn) > 1:
                            notesInfo.notesSimultaneously = notesInfo.notesSimultaneously + 1

                    else:
                        try:
                            index = notesInfo.notesOn.index(event.get_pitch())
                            notesInfo.notesDuration = notesInfo.notesDuration + (notesInfo.timelapsed - notesInfo.notesOnTime[index])
                            #print('noteoff',event.get_pitch(),notesInfo.timelapsed, (notesInfo.timelapsed - notesInfo.notesOnTime[index]))
                            notesInfo.notesOn.pop(index)
                            notesInfo.notesOnTime.pop(index)
                            notesInfo.notesSiceLast = notesInfo.timelapsed
                        except ValueError as e:
                            #print('error', e)
                            continue

                if issubclass(type(event), midi.NoteOffEvent):
                    try:
                        index = notesInfo.notesOn.index(event.get_pitch())
                        notesInfo.notesDuration = notesInfo.notesDuration + (notesInfo.timelapsed - notesInfo.notesOnTime[index])
                        #print('noteoff',event.get_pitch(),notesInfo.timelapsed, (notesInfo.timelapsed - notesInfo.notesOnTime[index]))
                        notesInfo.notesOn.pop(index)
                        notesInfo.notesOnTime.pop(index)
                    except ValueError as e:
                        #print('error', e)
                        continue

            if notesInfo.countNotes != 0:
                #print('avg:', str(notesInfo.sumNotes/notesInfo.countNotes), 'var', (notesInfo.maxNote-notesInfo.minNote), 'durAvg', notesInfo.notesDuration/notesInfo.countNotes, 'silAvg', notesInfo.notesSilence/notesInfo.countNotes)
                self.notesInfos.append(notesInfo)
                if notesInfo.vocalTrack:
                    self.notesInfosVocal.append(notesInfo)
                else:
                    self.notesInfosNonVocal.append(notesInfo)
                
#midparser = MidParser()
#midparser.run('c:/temp/midi/Creedence_Clearwater_Revival_-_Proud_Mary.mid')

        