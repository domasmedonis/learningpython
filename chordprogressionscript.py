from music21 import stream, chord, note

# Create a stream (container for the chords)
chord_progression = stream.Stream()

# Define some common chords for the progression
# i - VII - VI - V (in C minor)

# Chord i (C minor)
chord_i = chord.Chord(["C4", "Eb4", "G4"])
chord_i.quarterLength = 2.0  # Duration for each chord

# Chord VII (Bb major)
chord_VII = chord.Chord(["Bb4", "D5", "F5"])
chord_VII.quarterLength = 2.0

# Chord VI (Ab major)
chord_VI = chord.Chord(["Ab4", "C5", "Eb5"])
chord_VI.quarterLength = 2.0

# Chord V (G major)
chord_V = chord.Chord(["G4", "B4", "D5"])
chord_V.quarterLength = 2.0

# Append these chords to the chord progression
chord_progression.append(chord_i)
chord_progression.append(chord_VII)
chord_progression.append(chord_VI)
chord_progression.append(chord_V)



# Optional: Save as MIDI to listen to the progression
chord_progression.write('midi', fp='trap_chord_progression.mid')
