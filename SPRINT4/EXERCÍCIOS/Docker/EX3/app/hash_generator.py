import hashlib

while True:
    input_string = input("Digite uma string (ou 'exit' para sair): ")
    
    if input_string.lower() == 'exit':
        break

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    print("Hash SHA-1 da string:", sha1_hash)