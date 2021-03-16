note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print(note1)

def moyenne_tuples(liste,nom="tous",matiere="toutes"):
  res=0
  n=0
  for a in liste :
    if (nom == "tous"):
      if (matiere == "toutes") :
          res=res+a[2]
          n=n+1
      else :
        if (a[1]== str(matiere)):
         res=res+a[2]
         n=n+1      
    else :
      if (a[0]== str(nom)) :
          if (matiere == "toutes") :
              res=res+a[2]
              n=n+1
          else :
            if (a[1]== str(matiere)):
              res=res+a[2]
              n=n+1
  res=round(res/n,2)
  return print(res)

moyenne_tuples(notes,"eleve1")
moyenne_tuples(notes,"eleve1","math")

### 5 
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('Eleve:', self.eleve, 'Matiére :', self.matiere, 'Note :', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)
onotes = []
#for a in notes:
# onotes.append(Note(a))
