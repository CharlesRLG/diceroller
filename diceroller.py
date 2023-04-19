import random as rd
import re

rd.seed()

dice_pattern = r"(\d+)[dD](\d+)"

print("")

def roll_dice(how_many:int = 1, sides:int = 6) -> tuple[int, ...]:
    """
    Lancez un certain nombre de dés.

    :param how_many : nombre de dés à lancer, facultatif, la valeur par défaut est 1.

    :param faces : nombre de faces par dé, facultatif, la valeur par défaut est 6. Les valeurs attendues sont 4, 6, 8, 10, 12, 20 et 100.
    
    :raises ValueError : levée si le nombre de dés est négatif ou nul ou si le nombre de faces n'est pas celui attendu.
    
    :return : un tuple de résultats de dés

    """
    # if sides not in [4, 6, 8, 10, 12, 20, 100, 1000]:
    #     raise ValueError(f'Non valide number of dice sides, got {sides}')

    if how_many < 1:
        raise ValueError(f"Au moins un dé doit être lancé, obtenu {how_many}")

    dices_values = [rd.randint(1, sides) for _ in range(how_many)]
    return tuple(dices_values)


def parse_dice_request(sentence:str) -> tuple[int, int]:
    """
    Analyser une chaîne pour extraire le nombre de dés et leur nombre de faces.
    :param sentence : une chaîne contenant le motif attendu.

    """
    result = re.search(dice_pattern, sentence)
    if not result:
        raise ValueError(f"Le pattern du dé n'a pas été trouvé {sentence}")

    return int(result.group(1)), int(result.group(2))


def interaction_loop():
    """
    Interaction CLI loop. Appel la foncton pour uiliser l'application avec le CLI.

    """
    while True:
        # answer = input("Lancer un dé ? (q pour quitter) (exemple taper 1d6) : ")
        numbreDice = input("Combien de Dés voulez-vous lancer ? (1, 2, 3, ...) (q pour quitter)")
        typeDice = input("Quel type de Dé voulez-vous lancer ? (6, 8, 10, ou autre) (q pour quitter)")
        answer = numbreDice + "d" + typeDice

        if answer in ("qdq" or "qdQ" or "Qdq" or "QdQ"):
            print("-                                                             -")
            print("-----> Vous aurez plus de chance la prochaine fois !")
            print("-                                                             -")
            print("-----> Au revoir !")
            print("-                                                             -")
            break

        try:
            dices_number, dices_face = parse_dice_request(answer)
            dices_values = roll_dice(dices_number, dices_face)
            print("-                                                             -")
            print(f"-----> Vos résultat sont sur une base de dé {dices_face}")
            print("-                                                             -")
            print(f"-----> Valeurs : {dices_values}")
            print("-                                                             -")
            print(f"-----> Pour un total de : {sum(dices_values)}")
            print("-                                                             -")
            print(f"-----> Et une moyenne de : {(sum(dices_values))/(dices_number)}")
            print("-                                                             -")

        except ValueError:
            print("-                                                             -")
            print("-----> Ce ou ces dé(s) ne peut/peuvent être lancé !")
            print("-                                                             -")
            


if __name__ == "__main__":
    interaction_loop()