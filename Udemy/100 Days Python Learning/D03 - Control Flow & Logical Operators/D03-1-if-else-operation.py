#if/else operation
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can get in!")
else:
  print("Go back next time Kid!")

#command if / else adalah merupakan pasangan
# if "syarat dari variable yang ada":
#  perintah selanjutnya jika memenuhi kriteria, pada line ini (setelah if) maka indent akan maju satu tab sebagai tanda bahwa line tsb merupakan koneksi dari if
# else: <jika syarat tidak terpenuhi> dan tidak boleh maju satu tab karena ini merupakan command kebalikan meskipun salah satu koneksi dari if
#  perintah jika tidak memenuhi kriteria, format dan keterangan sama dengan line setelah if
#operation yang dipakai ">=" greater than or equal to, "==" equal to, "!=" not equal to