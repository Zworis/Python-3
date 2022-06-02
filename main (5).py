import time




#De functie om de contactenlijst in te zien aanmaken
def inzien(contacten):
  for key, value in contacten.items():
    print(key, ' : ', value)
    time.sleep(0.1)
  time.sleep(0.5)

#De functie voor verwijderen aanmaken
def verwijderen(contacten):
  keuze = input("Wilt u: \n1: Aan de hand van naam verwijderen? \n2: Aan de hand van nummer verwijderen?")
  if keuze == "1":
     naam_verwijderen = input("Welke naam wilt u verwijderen?")
     if naam_verwijderen in contacten:
        del contacten[Naam_Verwijderen]
     else:
        print("De naam die u wou verwijderen staat niet in uw contactlijst.")
        
  elif keuze == "2":
     nummer_verwijderen = input("Welk nummer wilt u verwijderen?")
     for key, value in contacten.items():
        if nummer_verwijderen == value:
          print("Verwijderen...")
          del contacten[key]
          time.sleep(1)
          print("Suceesvol verwijderd")
          return
     print("Het nummer wat u wou verwijderen staat niet in uw contactlijst")


#De functie om contacten aan te maken definiëren
def contact_aanmaken(contacten):
    naam = input("Wat is de naam van het contact die u wilt toevoegen?")
    nummer = input("Wat is het nummer van het persoon dat u wilt toevoegen?")
    contacten[naam] = nummer

#De functie voor een contact wijzigen definiëren
def wijzigen(contacten):
  keuze = input("Wilt u: \n1: De naam van een contact veranderen? \n2: Het nummer van een contact veranderen")
  if keuze == "1":
      keuze = input("Wilt u: \n1: via de naam het contact vinden? \n2: Via het nummer het contact vinden?")
      if keuze == "1":
        naam = input("Welk contact zijn naam wilt u veranderen?")
        if naam in contacten:
          nieuwe_naam = input("Hoe wilt u het contact noemen?")
          contacten[nieuwe_naam] = contacten[naam]
          del contacten[naam]
        else:
          print("Het naam waat u heeft ingevoerd staat niet in uw contactlijsten")
      elif keuze == "2":
        nummer = input("Wat is het nummer van het contact dat u wilt wijzigen?")
        if nummer in contacten.values():   
          nieuwe_naam = input("Wat is de nieuwe naam die u het contact wilt geven?")
          for key, value in contacten.items():
           if nummer == value:
             contacten[nieuwe_naam] = contacten[key]
             del contacten[key]
             return
        else:
          print("Het nummer wat u heeft opgegeven staat niet in uw contacten")
  elif keuze =="2":
      keuze = input("Wilt u: \n1: via de naam het contact vinden? \n2: Via het nummer het contact vinden?")
      if keuze == "1":
        naam = input("Wat is de naam van het contact dat u wilt veranderen?")
        if naam in contacten:
          nieuwe_nummer = input("Wat is het nieuwe nummer van het contact?")
          contacten[naam] = nieuwe_nummer
        else:
          print("Het naam wat u heeft ingevoerd staat niet in uw contacten lijst")
      elif keuze == "2":
        nummer = input("Wat is het nummer van het contact dat u wilt wijzigen?")
        if nummer in contacten.values():
          nieuwe_nummer = input("Wat is het nieuwe nummer voor dat contact?")
          for key, value in contacten.items():
           if nummer == value:
             contacten[key] = nieuwe_nummer
             return
        else:
          print("Het nummer wat u heeft ingevoerd is niet geldig")
  else:
      print("U heeft geen goed input gegeven, probeer opnieuw en antwoord met een cijfer wat bij de functie staat.")

LIJST = [inzien, verwijderen, contact_aanmaken, wijzigen]

def contactenlijst(opties, lijst_van_contacten):
  if int(opties) >= 0 and int(opties) <= 4:
    LIJST[int(opties)-1](lijst_van_contacten)


def menu():
  print("Als u het programma wilt verlaten moet u 'Quit!' in typen.\n\n")
  time.sleep(0.2)
  print("Wilt u:")
  time.sleep(0.5)
  print("1: De contacten lijst inzien?")
  time.sleep(0.2)
  print("2: Een contact verwijderen?")
  time.sleep(0.2)
  print("3: Een contact toevoegen?")
  time.sleep(0.2)
  print("4: Een contact aanpassen?")


def main():
  contacten = {
    "Apple" : "0800 0200 570",
    "Peter" : "38790771788",
    "Jochem" : "43913816337",
    "Cas":"45257405926",
    "Jeen" : "22682338392"
  }
  
  menu()
  while (task := input()) != "Quit!":
    # print("Wilt u:")
    # time.sleep(0.5)
    # print("1: De contacten lijst inzien?")
    # time.sleep(0.2)
    # print("2: Een contact verwijderen?")
    # time.sleep(0.2)
    # print("3: Een contact toevoegen?")
    # time.sleep(0.2)
    # print("4: Een contact aanpassen?")
    # task = input()

    try:
      if isinstance(int(task), int) == True:
        contactenlijst(task, contacten)
    except:
      pass
    # if task == "Quit!":
    #   quit()
    menu()
  
  quit()


main()