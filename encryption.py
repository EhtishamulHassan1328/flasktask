import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# def encrypt_grade(grade):
#     # Generate an RSA key pair
#     key = RSA.generate(2048)
#     public_key = key.publickey()

#     # Encrypt the grade using the public key
#     enc_grade = base64.b64encode(public_key.encrypt(grade.encode(), None)[0]).decode('utf-8')
#     return enc_grade

# Usage
# grade = "A"
# encrypted_grade = encrypt_grade(grade)
# print(encrypted_grade)

def encrypt_grade(grade):
    with open('public_key.pem', 'r') as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(grade.encode())
    enc_grade = base64.b64encode(encrypted_data)
    
    return enc_grade.decode('utf-8')


def decrypt_grade(encrypted_grade):
    with open('private_key.pem', 'r') as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_grade.encode()))
    
    return decrypted_data.decode('utf-8')



grade="A"
a1= encrypt_grade(grade)
print(a1)
a2=decrypt_grade(a1)

print(a2)
# Code for Encryption
# def encrypt_grade(grade):
#     with open('public_key.pem', 'r') as f:
#         public_key = RSA.import_key(f.read())

#     enc_grade = base64.b64encode(public_key.encrypt(grade.encode(), None)[0]).decode('utf-8')
 
#     # print(public_key)
#     # enc_grade = base64.b64encode(rsa.encrypt(grade.encode(), public_key)).decode('utf-8')
#     # return base64.b64encode(enc_grade).decode('utf-8')
#     return enc_grade





# grade="A"

# print(encrypt_grade(grade))

# Code for Decryption
# def decrypt_grade(grade):
#     decgrade = base64.b64decode(grade).decode('utf-8')
#     dec_grade= rsa.decrypt(decgrade.decode(), private_key)
#     return dec_grade


# import base64


# def encrypt_grade(grade,public_key):
#     # Generate an RSA key pair
#     key = public_key
#     public_key = key.publickey()

#     # Encrypt the grade using the public key
#     enc_grade = base64.b64encode(public_key.encrypt(grade.encode(), None)[0]).decode('utf-8')
#     return enc_grade

# # Usage
# grade = "A"
# encrypted_grade = encrypt_grade(grade)
# print(encrypted_grade)