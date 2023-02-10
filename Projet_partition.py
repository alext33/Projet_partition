import numpy as np
import sounddevice as sd

class Note():

    sps=44100
    
    
    
    def __init__(self,note,octave,rythme=1):
        self.note = note
        self.rythme = rythme
        self.octave = octave
        self.liste_notes = []
        self.notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

        A1= 55 #freq de référence
        demi_tons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        
        for i in range(len(self.notes)):
          frequence = A1 * (2 ** (demi_tons[i] / 12))
          self.liste_notes.append(frequence)

        note_out= self.notes.index(note)
        frequence = self.liste_notes[note_out]
        self.frequence = frequence*2**self.octave
        
    def play(self, tempo):
        sd.play(self.get_waveform(tempo), self.sps)
        

    def get_waveform(self,tempo):
        duree_note = self.rythme*60/tempo
        nb_echantillons = int(duree_note * self.sps)
        each_sample_number = np.linspace(0, duree_note, nb_echantillons)
        waveform = np.sin(2 * np.pi * each_sample_number * self.frequence)
        return waveform



class Partition():
    
    def __init__(self, liste_notes, tempo):
        self.liste_notes = liste_notes
        self.tempo = tempo 
        
    def get_waveform(self):
        waveform= self.liste_notes[0].get_waveform(self.tempo)
        for index, note in enumerate(self.liste_notes):
            if index>0:
                waveform = np.concatenate((waveform,note.get_waveform(self.tempo)))
        return waveform       

    def play(self):
        waveform = self.get_waveform()
        sd.play(waveform, self.liste_notes[0].sps)
        


partition_white_stripes = Partition([Note("E", 2,1), Note("E", 2,1/2), Note("G", 2,1/2),Note("E", 2,1/2),Note("D", 2,1/2),Note("C", 2,2),Note("B", 2,1),Note("E", 2,1), Note("E", 2,1/2), Note("G", 2,1/2),Note("E", 2,1/2),Note("D", 2,1/2),Note("C", 2,1/2),Note("D", 2,1/2),Note("C", 2,1/2),Note("B", 2,1)],120)
partition_smoke_on_the_water = Partition([Note("A", 1,1),Note("C", 1,1),Note("D", 1,2),Note("A", 1,1),Note("C", 1,1),Note("D#", 1,1/2),Note("D", 1,2),Note("A", 1,1),Note("C", 1,1),Note("D", 1,2),Note("D", 1,1/2),Note("C", 1,1),Note("A", 1,1/2),Note("A", 1,1/2)],120)
A=partition_white_stripes.get_waveform()
print(A)

#partition_white_stripes.play()
partition_smoke_on_the_water.play()
