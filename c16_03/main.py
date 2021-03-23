note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

# Question 4
# Question 4 c
def moyenne_tuples(liste,nom=None,matiere=None):
  res = []
  liste_eleve=[]
  for a in liste :
    liste_eleve= [x for x in liste if x[0] == nom or nom == None]
    liste_matiere= [x for x in liste_eleve if x[1] == matiere or matiere == None]
    res = [x[2] for x in liste_matiere ]
    moy = sum(res)/len(res)
  return moy

print("Question 4 a")
print(moyenne_tuples(notes,"eleve1",))

print("Question 4 b")
print(moyenne_tuples(notes,"eleve1","math"))


#Question 5

notes_enregistrées = []
class Note:
  def __init__(self, eleve, matiere, valeur):
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    self = notes_enregistrées.append(self)


  def afficher(self):
    print('Eleve:', self.eleve, 'Matiére :', self.matiere, 'Note :', self.valeur)
  
  def __str__(self):
    return f"Eleve: {self.eleve} Matiére : {self.matiere} Note : {self.valeur}"


onotes = []
for a in notes:
  onotes.append(Note(a[0],a[1],a[2]))
#Pour afficher l'ensemble des notes avec la fonction Note.afficher()
#for x in range(len(onotes)) :
#  Note.afficher(onotes[x])

print("Question 6")
#Afficher l'ensemble des notes avec la fonction prin()
for x in range(len(onotes)) :
  print(onotes[x])

print("Question 7")
#Démonstration de la sauvegarde des notes de facon automatique
for x in range(len(notes_enregistrées)) :
  print(notes_enregistrées[x])

print("Question 8")

def moyenne_Notes(nom=None,matiere=None):
  liste = notes_enregistrées
  res = []
  liste_eleve=[]
  for a in liste :
    liste_eleve= [x for x in liste if x.eleve == nom or nom == None]
    liste_matiere= [x for x in liste_eleve if x.matiere == matiere or matiere == None]
    res = [x.valeur for x in liste_matiere ]
    moy = sum(res)/len(res)
  return moy

print(moyenne_Notes())

print("Question 9")

class demo :
  def __init__(self,x):
    self.instances = []
    self.instances.append(x)
  
#  @classmethod
#  def moyenne(cls):
#    return sum(cls.instances)/len(cls.instances)
#demo(5)
#print(demo.moyenne())