"""Phase 1: Encrypting"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet.extend(alphabet)  # for repeating the list when shifted text is outside from the range


# Todo 1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_new, shift_new):  # usahakan jangan pakai "text" & "shift" untuk memisahkan antara parameter & argument
    cypher_text = ""  # key untuk final touch
    for text_check in text_new:  # looping text one by one pada word yg diinput user
        # Todo 2: shift each letter of the 'text' forwards in the alphabet by the shift amount
        text_pos = alphabet.index(text_check)  # konversi huruf menjadi angka urutan afabet dalam list
        new_pos = text_pos + shift_new  # merubah urutan alfabet setalah di shifting
        new_text = alphabet[new_pos]  # konversi urutan baru ke menjadi alfabet baru
        cypher_text += new_text  # menggabungkan huruf yang dipanggil menjadi string baru
    print(f'The encoded text is "{cypher_text}".')


# Todo 3: Call the encrypt function and pass in the user inputs.
encrypt(text_new=text, shift_new=shift)
