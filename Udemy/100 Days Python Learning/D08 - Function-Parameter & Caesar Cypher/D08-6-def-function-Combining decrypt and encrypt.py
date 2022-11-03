"""Phase 3: Combining Decrypting & Encrypting"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet.extend(alphabet)  # for repeating the list when shifted text is outside from the range


"""My Approaches"""
# Todo 1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(texting, shifting, directioning):
    crypt_text = ""
    for letter in texting:
        pos = alphabet.index(letter)
        if direction == "encode":
            new_pos = pos + shifting
        elif direction == "decode":
            new_pos = pos - shifting
        crypt_text += alphabet[new_pos]
    print("My approaches")
    print(f'The {direction}d text is "{crypt_text}"')


# Todo 2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(texting=text, shifting=shift, directioning=direction)


"""Course Approaches"""
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        # statement untuk mengganti arah ketika user meminta decode, karena encode logic nya normal (positif)
        shift_amount *= -1
        # logic ketika decode, untuk encode shift nya tetap memakai angka normal
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print("\nCourse's Approaches")
    print(f"Here's the {direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)