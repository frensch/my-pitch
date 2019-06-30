from midparser import MidParser
from os import listdir, walk
from os.path import isfile, join
import csv

#mypath = 'c:/temp/midi/outros'
mypath = 'C:/Users/frensch/Downloads/130000_Pop_Rock_Classical_Videogame_EDM_MIDI_Archive[6_19_15]/130000_Pop_Rock_Classical_Videogame_EDM_MIDI_Archive[6_19_15]'

def createDBTRain():
    for r, d, f in walk(mypath):
        for file in f:
            if '.mid' in file:
                filepath = join(r, file)
                print(filepath)

                midparser = MidParser()
                try:
                    #print(f)
                    midparser.run(filepath)
                    if midparser.hasVocal:
                        print('vocais',len(midparser.notesInfosVocal))
                        print('non vocais',len(midparser.notesInfosNonVocal))

                        with open('total.csv', 'a') as fcsv:
                            writer = csv.writer(fcsv)
                            print('................................................')
                            for notesInfo in midparser.notesInfos:
                                writer.writerow([notesInfo.sumNotes/notesInfo.countNotes, notesInfo.maxNote-notesInfo.minNote, notesInfo.notesDuration/notesInfo.countNotes, \
                                    notesInfo.notesSilence/notesInfo.countNotes, notesInfo.sumPitchDiff/notesInfo.countNotes, notesInfo.instrument, notesInfo.notesSimultaneously, \
                                    notesInfo.maxNote, notesInfo.minNote, notesInfo.trackName, notesInfo.fileName, notesInfo.vocalTrack])
                except:
                    print('deu merda')
                    continue

                
def createDBApp():
    for r, d, f in walk(mypath):
        for file in f:
            if '.mid' in file:
                filepath = join(r, file)
                print(filepath)

                midparser = MidParser()
                try:
                    #print(f)
                    midparser.run(filepath)
                
                    with open('total_app.csv', 'a') as fcsv:
                        writer = csv.writer(fcsv)
                        print('................................................')
                        for notesInfo in midparser.notesInfos:
                            writer.writerow([notesInfo.sumNotes/notesInfo.countNotes, notesInfo.maxNote-notesInfo.minNote, notesInfo.notesDuration/notesInfo.countNotes, \
                                notesInfo.notesSilence/notesInfo.countNotes, notesInfo.sumPitchDiff/notesInfo.countNotes, notesInfo.instrument, notesInfo.notesSimultaneously, \
                                notesInfo.maxNote, notesInfo.minNote, notesInfo.trackName, notesInfo.fileName, notesInfo.vocalTrack])
                except:
                    print('deu merda')
                    continue


createDBApp()