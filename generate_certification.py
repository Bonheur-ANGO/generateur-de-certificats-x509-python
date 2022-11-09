import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from generate_key import generate_key
import json


with open("certification_autorithy.json", "r") as certification:
    CA = json.load(certification)


def generate_cert(organisation, domain, locality, country, postal_code, algo_signature : str):
    key = None
    #création de la clée privée
    if key is None:
        key = generate_key(algo_signature)
    #a
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, locality),
        x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organisation),
        x509.NameAttribute(NameOID.COMMON_NAME, domain),
        x509.NameAttribute(NameOID.POSTAL_CODE, postal_code)
    ])
    certfile = open(f"certificates/{organisation}/{organisation}-new.csr")
    certdata = certfile.read().encode("utf-8")
    loadcsr = x509.load_pem_x509_csr(data=certdata)

    #signature de la clée
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        loadcsr.subject
    ).public_key(
        loadcsr.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(key, hashes.SHA256())




    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)

    with open(f"certificates/{organisation}/{organisation}-new.crt", 'wb') as c:
        c.write(cert_pem)


    print("Le certificat a bien été généré")
