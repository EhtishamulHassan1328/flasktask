from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generated RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=512,
    backend=default_backend()
)

# Extracted public key
public_key = private_key.public_key()

# Serialized keys to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Saved keys to files
with open('private_key.pem', 'wb') as f:
    f.write(private_pem)

with open('public_key.pem', 'wb') as f:
    f.write(public_pem)
