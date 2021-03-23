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
    res = round(sum(res)/len(res),2)
  return print(res)

# Question 4 a
moyenne_tuples(notes,"eleve1",)

# Question 4 b
moyenne_tuples(notes,"eleve1","math")


# Question 5 
class Note:
  def __init__(self, eleve, matiere, valeur):
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('Eleve:', self.eleve, 'Matiére :', self.matiere, 'Note :', self.valeur)
  
  def __str__(self):
    return f"Eleve: {self.eleve} Matiére : {self.matiere} Note : {self.valeur}"

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)
onotes = []

#RAJOUTER en PLUS aprés le cour du 16/03 de midi
for a in notes:
  onotes.append(Note(a[0],a[1],a[2]))

for x in range(len(onotes)) :
  Note.afficher(onotes[x])

# Question 6

for x in range(len(onotes)) :
  print(onotes[x])

# Question 7

notea = ('LeXA', 'art', 17)
noteb = ('LeXA', 'poterie', 11)
notec = ('LeXA', 'dessin', 14.5)
noted = ('Patrick', 'art', 18)
notee = ('Patrick', 'dessin', 8)
notef = ('Gérard', 'dessin', 12)
noteg = ('Gérard', 'dessin', 11.5)
noteh = ('Gérard', 'art', 16)

notes_enregistrés = [notea, noteb, notec, noted, notee, notef,noteg,noteh]

# À la fin de la méthode init une ligne pour ajouter la note que vos venez de créer à la liste. Elle est referencée par self. ???????????????????????

# Question 8
def moyenne_Notes(nom="tous le monde",matiere="toutes les matiéres"):
  liste = notes_enregistrés
  res=0
  n=0
  for a in liste :
    if (nom == "tous le monde"):
      if (matiere == "toutes les matiéres") :
          res=res+a[2]
          n=n+1
      else :
        if (a[1]== str(matiere)):
         res=res+a[2]
         n=n+1      
    else :
      if (a[0]== str(nom)) :
          if (matiere == "toutes les matiéres") :
              res=res+a[2]
              n=n+1
          else :
            if (a[1]== str(matiere)):
              res=res+a[2]
              n=n+1
  res=round(res/n,2)
  return print(f"La moyenne de {nom}, pour {matiere} est de {res}/20.")

moyenne_Notes()

#Question 9

