from mainmenu import *


def saltanalysis():
    # Salt Analysis Program
    # Defining systemaic anion tests
    def invalid():
        while True:
            print("We do not have this salt")

    def Carbonatesystematic():
        value = int(
            input("""Add some dilute HCL to your salt,
  Press 1 if you observe Brisk Effervesence
  Press 2 if you do not observe Brisk Effervesence - """))
        if value == 1:
            return "Carbonate"
        else:
            return False

    def Acetatesystematic():
        value = int(
            input(
                """Rub your salt with dilute H2SO4 with the help of a glass rod,
  Press 1 if the vinegar smell intensifies
  Press 2 if the vinegar snell does not intensify - """))
        if value == 1:
            return "Acetate"
        else:
            return False

    def clno3systematic():
        value = int(
            input("""Treat your salt with some concentrated H2SO4,
  Press 1 if you observe Pungent smelling white fumes
  Press 2 if you observe a brown gas
  Press 3 if you do not observe any of the above - """))
        if value == 1:
            return "Chloride"
        elif value == 2:
            return "Nitrate"
        else:
            return False

    def Sulphatesystematic():
        value = int(
            input("""Treat your salt with some BaCl2,
  Press 1 if you observe a white precipitate
  Press 2 if you do not observer a white precipitate - """))
        if value == 1:
            return "Sulphate"
        else:
            return False

    # Systematic anion tests done
    # Defining systematic cation tests
    def Ammoniumsystematic():
        value = int(
            input("""Prepare a salt solution and then add some Na2CO3 to it,
  Press 1 if you DO NOT observe a precipitate
  Press 2 if none of the above - """))
        if value == 1:
            return "Ammonium"
        else:
            return False

    def Group5aluminumsystematic():
        value = int(
            input("""Prepare a dilute solution of your salt,
  Then add some dilute HCl to it,
  Press 1 if you observe White Precipitate
  Press 2 if none of the above - """))
        if value == 1:
            return "Lead"
        else:
            value1 = int(
                input(
                    """Continue by adding a pinch of NH4Cl to the same solution,Shake well,
  Add some NH4OH to the mixture aswell
  Press 1 if you observe a white gelatinous ppt
  Press 2 if none of the above - """))
            if value1 == 1:
                return "Aluminum"
            else:
                value2 = int(
                    input(
                        """Continue by adding some Ammonium Carbonate to your mixture,
  Press 1 if you observe a white ppt
  Press 2 if you do not observe a white ppt - """))
                if value2 == 1:
                    return "Group5"
                else:
                    return False

    # Systematic tests for cation done
    # Confirmatory tests for cation
    def Leadconfirmatory():
        value = int(
            input(
                """Boil some of your salt with water,then add some K2CrO4 to it,
  Press 1 if you observe a yellow ppt
  Press 2 if you do not observe a yellow ppt - """))
        if value == 1:
            return "Lead"
        else:
            return False

    def Group5flame():
        value = int(
            input("""Add some of your salt to a watchglass,
  Add some concetrated HCl to it,
  Rub with a glass rod,
  Hold the glass rod to the flame,
  Press 1 if you observe a Pale green flame
  Press 2 if you observe a Crimson red flame
  Press 3 if you observe a Brick red flame - """))
        if value == 1:
            return "Barium"
        elif value == 2:
            return "Strontium"
        else:
            return "Calcium"

    def Bariumconfirmatory():
        value = int(
            input("""Prepare a acetic acid solution of your salt,
  Add some pottassium chromate to your salt,
  Press 1 if you observe a Yellow ppt,
  Press 2 if none of the above - """))
        if value == 1:
            return "Barium"
        else:
            return False

    def Strontiumconfirmatory():
        value = int(
            input("""Prepare a acetic acid solution of your salt,
  Add some ammonium sulphate to your salt,
  Press 1 if you observe a white ppt,
  Press 2 if none of the above - """))
        if value == 1:
            return "Strontium"
        else:
            return False

    def Calciumconfirmatory():
        value = int(
            input("""Prepare a acetic acid solution of your salt,
  Add some Ammonium Oxalate to your salt,
  Press 1 if you observe a white ppt,
  Press 2 if none of the above - """))
        if value == 1:
            return "Calcium"
        else:
            return False

    def Ammoniumconfirmatory():
        value = int(
            input("""Add few drops of Nessler's reagent to your salt,
  Press 1 if you observe Reddish Brown color
  Press 2 if none of the above - """))
        if value == 1:
            return "Ammonium"

    def Aluminumconfirmatory():
        value = int(
            input(
                """Dip a strip of filter paper in a cobalt nitrate-dilute HNO3 solution of your salt,
  Hold the strip to a flame
  Burn the ash
  Press 1 if you observe blue tinted ash
  Press 2 if none of the above - """))
        if value == 1:
            return "Aluminum"
        else:
            return False

    # Confirmatory tests for cation done
    # Confirmatory tests for anions
    def Acetateconfirmatory():
        value = int(
            input("""Add a few drops of neutral Ferric chloride to your salt,
  Press 1 if you observe a Reddish Brown coloration
  Press 2 if none of th above - """))
        if value == 1:
            return "Acetate"
        else:
            return False

    def Carbonateconfirmatory():
        value = int(
            input("""Add some BaCl2 to your solution,
  Press 1 if you observe a white precipitate
  Press 2 if none of the above - """))
        if value == 1:
            value1 = int(
                input("""Continue by adding some HCl to your mixture,
  Press 1 if you observe Brisk Effervesence
  Press 2 if none of the above - """))
            if value1 == 1:
                return "Carbonate"
            else:
                return False
        else:
            return False

    def Chlorideconfirmatory():
        value = int(
            input("""Prepare a dilute HNO3 solution of your salt,
  Add a few drops of AgNO3 to it,
  Press 1 if you observe a White ppt
  Press 2 if none of the above - """))
        if value == 1:
            value1 = int(
                input("""Continue by adding excess of NH4OH to your mixture,
  Press 1 if your white ppt dissolves
  Press 2 if none of the above - """))
            if value1 == 1:
                return "Chloride"
            else:
                return False
        else:
            return False

    def Sulphateconfirmatory():
        value = int(
            input("""Add some Acetic acid to your salt solution,
  Add some Lead acetate to your mixture,
  Press 1 if you observe a white ppt
  Press 2 if none of the above - """))
        if value == 1:
            return "Sulphate"
        else:
            return False

    def Nitrateconfirmatory():
        value = int(
            input("""Add few drops of Diphenylamine to your salt,
  Press 1 if you observe Deep blue coloration
  Press 2 if none of the above - """))
        if value == 1:
            return "Nitrate"
        else:
            return False

    probableanions = []
    probablecations = []
    notprobableanions = []
    notprobablecations = []
    anionsystematic = ["Carbonate", "Acetate", "clno3", "Sulphate"]
    cationsystematic = ["Ammonium", "Group5aluminum"]
    anionconfirmatory = [
        "Acetate", "Carbonate", "Chloride", "Sulphate", "Nitrate"
    ]
    cationconfirmatory = [
        "Ammonium", "Lead", "Barium", "Strontium", "Calcium", "Aluminum"
    ]
    # Prelimnary Tests
    # Odour Prelimnary
    while True:
        odour = int(
            input("""Enter the odour of the salt if any:
    Press 1 for Ammoniacal odour
    Press 2 for Vinegar odour
    Press 3 for no significant odour - """))
        if odour == 1:
            probablecations.append("Ammonium")
            break
        elif odour == 2:
            probableanions.append("Acetate")
            break
        elif odour == 3:
            notprobableanions.append("Acetate")
            notprobablecations.append("Ammonium")
            break
        else:
            print("Invalid choice, Enter again")
    # Solubility in Water prelimnary
    while True:
        watersoluble = int(
            input("""Is your salt soluble in water?
  Press 1 for yes
  Press 2 for no - """))
        if watersoluble == 1:
            if "Ammonium" not in probablecations:
                probablecations.append("Ammonium")
                if "Ammonium" in notprobablecations:
                    notprobablecations.remove("Ammonium")
            break
        elif watersoluble == 2:
            break
        else:
            print("Invalid choice, Enter again")
    # Solubility in dil HCL Prelimnary
    while True:
        dilhclsoluble = int(
            input("""Is your salt soluble in dilute HCL?
  Press 1 for yes
  Press 2 for no - """))
        if dilhclsoluble == 1:
            if "Lead" not in notprobablecations:
                notprobablecations.append("Lead")
                break
            break
        elif dilhclsoluble == 2:
            break
        else:
            print("Invalid choice, Enter again")
    # Prelimnary tests done
    # Systematic tests anion
    otheranions = []
    for x in anionsystematic:
        if x not in probableanions and x not in notprobableanions:
            otheranions.append(x)
    finalsystematicanion = probableanions + otheranions + notprobableanions
    for x in finalsystematicanion:
        anion = eval(x + "systematic" + "()")
        if anion:
            # Confirmatory tests anion
            conanion = eval(anion + "confirmatory" + "()")
            if conanion:
                break
    # ANION DONE
    # Systematic tests cation
    othercations = []
    for x in cationsystematic:
        if x not in probablecations and x not in notprobablecations:
            othercations.append(x)
    finalsystematiccation = probablecations + othercations + notprobablecations
    for x in finalsystematiccation:
        cation = eval(x + "systematic" + "()")
        if cation == "Group5":
            cation = Group5flame()
        if cation:
            # Confirmatory for cation
            concation = eval(cation + "confirmatory" + "()")
            if concation:
                break
    print("YOUR SALT IS.....:")
    for x in range(5):
        print("...")
    print(concation + " " + conanion)
