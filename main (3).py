import time
Contacten = {
  "Apple" : "0800 0200 570",
  "Peter" : "38790771788",
  "Jochem" : "43913816337",
  "Cas":"45257405926",
  "Jeen" : "22682338392"
}
def contactenlijst(opties):
  global Contacten
  if opties == "1":
    for key, value in Contacten.items():
      print(key, ' : ', value)
      time.sleep(0.1)
    time.sleep(0.5)
  elif opties == "2":
    keuze = input("Wilt u: \n1: Aan de hand van naam verwijderen? \n2: Aan de hand van nummer verwijderen?")
    if keuze == "1":
      Naam_Verwijderen = input("Welke naam wilt u verwijderen?")
      if Naam_Verwijderen in Contacten:
        del Contacten[Naam_Verwijderen]
      else:
        print("De naam die u wou verwijderen staat niet in uw contactlijst.")
        
    elif keuze == "2":
      Nummer_Verwijderen = input("Welk nummer wilt u verwijderen?")
      for key, value in Contacten.items():
         if Nummer_Verwijderen == value:
           print("Verwijderen...")
           del Contacten[key]
           time.sleep(1)
           print("Suceesvol verwijderd")
           return
      print("Het nummer wat u wou verwijderen staat niet in uw contactlijst")
           
  elif opties == "3":
    naam = input("Wat is de naam van het contact die u wilt toevoegen?")
    nummer = input("Wat is het nummer van het persoon dat u wilt toevoegen?")
    Contacten[naam] = nummer
    
  elif opties == "4":
    keuze = input("Wilt u: \n1: De naam van een contact veranderen? \n2: Het nummer van een contact veranderen")
    if keuze == "1":
      keuze = input("Wilt u: \n1: via de naam het contact vinden? \n2: Via het nummer het contact vinden?")
      if keuze == "1":
        Naam = input("Welk contact zijn naam wilt u veranderen?")
        if Naam in Contacten:
          Nieuwe_Naam = input("Hoe wilt u het contact noemen?")
          Contacten[Nieuwe_Naam] = Contacten[Naam]
          del Contacten[Naam]
        else:
          print("Het naam waat u heeft ingevoerd staat niet in uw contactlijsten")
      elif keuze == "2":
        Nummer = input("Wat is het nummer van het contact dat u wilt wijzigen?")
        if Nummer in Contacten.values():   
          Nieuwe_Naam = input("Wat is de nieuwe naam die u het contact wilt geven?")
          for key, value in Contacten.items():
           if Nummer == value:
             Contacten[Nieuwe_Naam] = Contacten[key]
             del Contacten[key]
             return
        else:
          print("Het nummer wat u heeft opgegeven staat niet in uw contacten")
    elif keuze =="2":
      keuze = input("Wilt u: \n1: via de naam het contact vinden? \n2: Via het nummer het contact vinden?")
      if keuze == "1":
        Naam = input("Wat is de naam van het contact dat u wilt veranderen?")
        if Naam in Contacten:
          Nieuwe_Nummer = input("Wat is het nieuwe nummer van het contact?")
          Contacten[Naam] = Nieuwe_Nummer
        else:
          print("Het naam wat u heeft ingevoerd staat niet in uw contacten lijst")
      elif keuze == "2":
        Nummer = input("Wat is het nummer van het contact dat u wilt wijzigen?")
        if Nummer in Contacten.values():
          Nieuwe_Nummer = input("Wat is het nieuwe nummer voor dat contact?")
          for key, value in Contacten.items():
           if Nummer == value:
             Contacten[key] = Nieuwe_Nummer
             return
        else:
          print("Het nummer wat u heeft ingevoerd is niet geldig")
    else:
      print("U heeft geen goed input gegeven, probeer opnieuw en antwoord met een cijfer wat bij de functie staat.")
      

while True:
  task = input("Wilt u: \n1: De contacten lijst inzien? \n2: Een contact verwijderen? \n3: Een contact toevoegen? \n4: Een contact aanpassen?\n")
  if isinstance(int(task), int) == True:
    pass
  contactenlijst(task)
