"""Phase 2: Decrypting"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet.extend(alphabet)  # for repeating the list when shifted text is outside from the range

# Todo 1: Create function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
    decr_text = ""
    # Todo 2: Shift each letter of the 'text' backwards in the alphabet by the shift amount
    for letter in plain_text:
        position = alphabet.index(letter)
        new_pos = position - shift_amount
        decr_text += alphabet[new_pos]
    print(f"The decoded text is '{decr_text}'")


# Todo 3: Check the decrypt result based on user input
decrypt(plain_text=text, shift_amount=shift)
