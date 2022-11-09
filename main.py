from generate_certification import generate_cert
from certification_signing_request import csr
from verify_certificate import verify

#on demande les informations de la compagnie
def askUserInformation():
    print("Tout d'abord veuillez entrer les informations de votre entreprise")
    organisation = input("Veuillez entrer le nom de votre organisation : ")
    domain = input("Veuillez entrer votre nom de domaine : ")

    locality = input("Veuillez entrer votre la ville : ")

    postal_code = ""

    while postal_code == "":
        try:
            str_postal_code = ""
            while len(str_postal_code) < 5:
                str_postal_code = input("Veuillez entrer votre code Postal : ")
            postal_code = int(str_postal_code)
        except:
            print("Veuillez entrer un code postal valide")

    company_infos = {
        "organisation": organisation,
        "locality": locality,
        "country": "FR",
        "postal_code": str(postal_code),
        "common_name": domain
    }

    return company_infos

#demande de l'algorithme de signature souhaitée
def askSignatureAlgo():

    choice = 0
    while not (choice == 1 or choice == 2):
        try:
            ask_choice = input("Veuillez choisir votre algorithme de signature :\n "
                               "1 - RSA \n "
                               "2 - DSA\n")
                               #"3 - ECDSA\n"
                               #"4 - ED448\n"
                               #"5 - ED25519\n")
            choice = int(ask_choice)
        except:
            print("\nVeuillez choisir entre 1 et 2\n")

    if choice == 1:
       return  "RSA"
    if choice == 2:
        return "DSA"
    """if choice == 3:
        return "ECDSA"
    if choice == 4:
        return "ED448"
    if choice == 5:
        return "ED25519"""



#programme principal
def main():
    print("**********Bienvenue sur notre application de génération de certificats**********")
    choice = 0
    while not (choice == 1 or choice == 2) :
        try:
            ask_choice = input("Que souhaitez vous faire comme opération ? \n "
                               "1 - Générer un certificat \n "
                               "2 - Vérifier la validité d'un certificat\n")
            choice = int(ask_choice)
        except:
            print("\nVeuillez choisir entre 1 ou 2\n")

    if choice == 1:
        company_infos = askUserInformation()
        algo_signature = askSignatureAlgo()
        csr(company_infos['organisation'])
        generate_cert(company_infos['organisation'],
                      company_infos['common_name'],
                      company_infos['locality'],
                      company_infos['country'],
                      company_infos['postal_code'], algo_signature)
    if choice == 2:
        print("Veuillez noter qu'il faudrait que open ssl soit installé sur votre ordinateur afin de vérifier la validité du certificat")
        org = input("Veuillez entrer le nom de l'organisation dont vous souhaitez vérifier la validité du certificat : ")
        verify(org)



main()
