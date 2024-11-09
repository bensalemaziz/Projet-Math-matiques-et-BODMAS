# myPythonFonctions.py

import random

# Dictionnaire des opérateurs
operatorDict = {
    1: '+',
    2: '-',
    3: '*',
    4: '**'
}

# Génère une liste d'opérateurs en évitant les doubles exposants
def generateOperatorList():
    operatorList = []
    for i in range(4):
        op = operatorDict[random.randint(1, 4)]
        # Éviter deux ** consécutifs
        while len(operatorList) > 0 and operatorList[-1] == '**' and op == '**':
            op = operatorDict[random.randint(1, 3)]
        operatorList.append(op)
    return operatorList

# Génère une question mathématique sous forme de chaîne
def generateQuestion():
    operandList = [random.randint(0, 9) for _ in range(5)]
    operatorList = generateOperatorList()
    questionString = f"{operandList[0]}"
    for i in range(4):
        questionString += f" {operatorList[i]} {operandList[i + 1]}"
    questionString = questionString.replace("**", "^")  # Pour l'affichage utilisateur
    return questionString

# Évalue la question
def evaluateQuestion(questionString):
    questionEval = questionString.replace("^", "**")  # Remettre ** pour eval()
    result = eval(questionEval)
    return result

# Demande et vérifie la réponse de l'utilisateur
# Demande et vérifie la réponse de l'utilisateur
def getUserAnswer(questionString, correctAnswer):
    while True:
        try:
            userAnswer = int(input(f"Résolvez : {questionString} = "))
            if userAnswer == correctAnswer:
                print("Correct ! Bien joué.")
                return 1
            else:
                print(f"Incorrect. La bonne réponse était {correctAnswer}.")
                return 0
        except ValueError:
            print("Veuillez entrer un nombre entier.")

# mathGame.py

import myPythonFonctions as mpf


def main():
    try:
        # Demande du nom de l'utilisateur
        userName = input("Entrez votre nom : ")
        userScore = 0

        userChoice = "0"
        while userChoice != "-1":
            # Générer une question
            questionString = mpf.generateQuestion()
            correctAnswer = mpf.evaluateQuestion(questionString.replace("^", "**"))

            # Obtenir la réponse de l'utilisateur
            score = mpf.getUserAnswer(questionString, correctAnswer)
            userScore += score

            # Demander si l'utilisateur veut continuer
            userChoice = input("Appuyez sur Entrée pour continuer ou tapez -1 pour arrêter : ")

        print(f"Merci d'avoir joué, {userName}! Votre score est {userScore}.")

    except Exception as e:
        print("Une erreur s'est produite. Le programme se terminera.")
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
