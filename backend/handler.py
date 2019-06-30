import json
from querymusics import QueryMusics

qm = QueryMusics()

def searchForPitchRange(minpitch, maxpitch):
    
    #return {'musics':[{'title':'paradise city', 'artist':'guns n roses'}, {'title':'don\'t cry', 'artist':'guns n roses'}]}
    ret = qm.search(minpitch, maxpitch)
    print(ret)
    return ret

def convertTonesToNumbers(tone):
    tones = ['C','C#','D','D#','E','F', 'F#','G', 'G#','A','A#','B']
    toneLetter = tone[:-1]
    octave = int(tone[-1:]) + 1
    baseNumber = tones.index(toneLetter)
    toneNumber = 12*octave + baseNumber
    print(tone, toneNumber)
    return toneNumber

def musicsinmypitch(event, context):
    
    
    if not event['queryStringParameters'] or not event['queryStringParameters']['min'] or not event['queryStringParameters']['max']:
        return {'statusCode': 422, 'body': 'Faltando parametros: min e max'}
    minpitchTones = event['queryStringParameters']['min']
    maxpitchTones = event['queryStringParameters']['max']

    minpitch = convertTonesToNumbers(minpitchTones)
    maxpitch = convertTonesToNumbers(maxpitchTones)


    print("PTICH", minpitch, maxpitch)
    match = searchForPitchRange(minpitch, maxpitch)
    return {"statusCode": 200, "body": (match.to_json())}
