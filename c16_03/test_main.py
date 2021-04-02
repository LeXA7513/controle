from .main import Note

def test_ajout():
  Note.vider()
  assert Note == None
  Note('eleve1','math', 12)
  a='eleve1'
  b='math'
  c=12
  assert Note.instances[0].eleve == a and  Note.instances[0].matiere == b and Note.instances[0].valeur == c 