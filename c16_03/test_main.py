from .main import Note
from .main import moyenne_Notes

def test_ajout():
  Note.vider()
  assert Note == None
  Note('eleve1','math', 12)
  assert Note.instances[0].eleve == 'eleve1' and  Note.instances[0].matiere == 'math' and Note.instances[0].valeur == 12
  Note('eleve2','eco', 13)
