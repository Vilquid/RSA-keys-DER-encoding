from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def main():
    # Generation of RSA key
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Export of the private key
    private_key = key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    # Export of the public key
    public_key = key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)

    print("Private key : " + str(private_key))
    print("Private key (hex) : " + private_key.hex())
    print("Public key : " + str(public_key))
    print("Public key (hex) : " + public_key.hex())


if __name__ == '__main__':
    main()
