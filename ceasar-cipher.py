import cc_functions as cc

message = input("Message: ").strip()
shift = cc.get_shift()
action = cc.get_action()

match action:
        # Encrypt
        case "E":
            message = cc.caesar_cipher(message, shift)

        # Decrypt
        case "D":
            message = cc.caesar_cipher(message, -shift)

        # Qualquer outro valor
        case _:
            print("Action not supported")
            message=None

if message:
    print("Message: " + message)