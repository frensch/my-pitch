from midparser import MidParser
from os import listdir
from os.path import isfile, join
import csv

mypath = 'c:/temp/midi'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

tracks = []
midparser = MidParser()
for f in onlyfiles:#[500:550]:
    try:
        #print(f)
        midparser.run(mypath + '/' + f)
        if midparser.hasVocal:
            tracks.extend(midparser.notesInfos)
        midparser.notesInfos = []
    except:
        continue

print('vocais',len(midparser.notesInfosVocal))
print('non vocais',len(midparser.notesInfosNonVocal))

with open('total.csv', mode='w') as total_file:
    fieldnames = ['average_note', 'range_notes', 'average_duration', 'average_silence', 'average_diff_notes', 'instrument', 'simultaneously', 'min', 'max', 'trackName', 'filename', 'vocal']
    writer = csv.DictWriter(total_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for notesInfo in tracks:
        writer.writerow({'average_note': notesInfo.sumNotes/notesInfo.countNotes , 'range_notes': notesInfo.maxNote-notesInfo.minNote, \
        'average_duration': notesInfo.notesDuration/notesInfo.countNotes, 'average_silence': notesInfo.notesSilence/notesInfo.countNotes, \
        'average_diff_notes': notesInfo.sumPitchDiff/notesInfo.countNotes, 'instrument': notesInfo.instrument, 'simultaneously': notesInfo.notesSimultaneously, \
        'max': notesInfo.maxNote, 'min': notesInfo.minNote, 'trackName': notesInfo.trackName, 'filename': notesInfo.fileName, 'vocal': notesInfo.vocalTrack})
