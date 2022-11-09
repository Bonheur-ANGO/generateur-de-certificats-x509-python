import datetime
import os
from generate_key import generate_key
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import json

def csr(organisation):
    with open("registration_authority.json", "r") as certification:
        RA = json.load(certification)
        key = generate_key("RSA")

    # création de la demande de signature par l'autorité d'enregistrement
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, RA["country"]),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, RA["locality"]),
        x509.NameAttribute(NameOID.LOCALITY_NAME, RA["locality"]),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, RA["organisation"]),
        x509.NameAttribute(NameOID.COMMON_NAME, RA["common_name"]),
        x509.NameAttribute(NameOID.POSTAL_CODE, RA["postal_code"]),
        x509.NameAttribute(NameOID.PSEUDONYM, RA["pseudo"])
    ])).sign(key, hashes.SHA256())

    path = os.getcwd() + f"\certificates\{organisation}"
    os.mkdir(path, 0o666)
    with open(f"certificates/{organisation}/{organisation}-new.csr", "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))
