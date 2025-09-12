def get_shift():
    while True:
        try:
            shift = int(input("Number of shifts: "))
            return shift
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_action():
    while True:
        action = input("E - Encrypt / D - Decrypt: ").strip().upper()
        if action in ("E", "D"):
            return action
        else:
            print("Invalid action! Please type E or D.")

def caesar_cipher(message, shift):

    result = ""

    for char in message:

        # Se for letra
        if char.isalpha():
            # ord() retorna o código ASCII
            base = ord('A') if char.isupper() else ord('a')
            # ord(char) - base normaliza para começar do zero
            result += chr((ord(char) - base + shift) % 26 + base)

        # Se for número
        elif char.isdigit():
            base = ord('0')
            result += chr((ord(char) - base + shift) % 10 + base)

        # Se não for letra e nem número, fica inalterado
        else:
            result += char

    return result