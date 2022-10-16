alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#alphabet = alphabet.extend(alphabet)
alphabet.extend(alphabet) #command untuk mengulang list jika user berusaha input huruf yang berada diakhir list yg menyebabkan hasil yg baru di luar jangkauan list
def encrypt(text_new,shift_new): #usahakan jangan pakai "text" & "shift" untuk memisahkan antara parameter & argument
    cypher_text ="" #parameter untuk membuat string kosong
    for text_check in text_new: #looping text one by one pada word yg diinput user
        text_pos = alphabet.index(text_check) #key untuk konversi huruf menjadi angka urutan afabet yang dipanngil
        new_pos = text_pos + shift_new #key untuk merubah posisi awal urutan alfabet
        new_text = alphabet[new_pos] #key untuk mengkonversi urutan alfabet yg baru menjadi alfabet baru
        cypher_text += new_text #key untuk menggabungkan huruf yang dipanggil menjadi string baru
    print(f'The endoded text is "{cypher_text}".')

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text_new=text,shift_new = shift)

# another approach tanpa menggunakan alphabet extend
