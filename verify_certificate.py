import os
#vérifie la validité du certificat en lançant la commande opennssl
def verify(organisation):
    os.system(f"openssl x509 -in certificates/{organisation}/{organisation}-new.crt -text -noout")
