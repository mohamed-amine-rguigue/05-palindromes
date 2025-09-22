"""Fonctions de palindrome"""
#### Fonction secondaire

def ispalindrome(p):
    """A-t-on des palindromes?"""
    a=0
    for k in p:
        if k != p[(len(p)-1-a)]:
            return False
        a+=1
    return True

#### Fonction principale
def main():
    """Test de différents palindromes"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
