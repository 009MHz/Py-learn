################### Scope ####################

enemies = 1 #2 variable ini disebut global scope, jika di print di luar fungsi dibawah akan memanggil sesuai data yang ada (1)

def increase_enemies():
  enemies = 2 #1 variable ini disebut local scope jika fungsi dicall akan memanggil value dari enemies di dalam fungsi (2)
  print(f"enemies inside function: {enemies}") #memanggil nomor #1

increase_enemies()
print(f"enemies outside function: {enemies}") #memanggil nomor 2

#Local Scope
def refine_success():
    weapon_level = "+1"
    print(weapon_level)
refine_success() #3 fungsi ini akan memanggil perintah untuk printing value dari weapon_level (+1)
#print(weapon_level) #4 akan menghasilkan error "weapon_level" not defined, karena memanggil data di luar fungsi, sedangkan data yg dimaksud berada di dalam fungsi

#Global Scope
player_health = 10 #5 disebut dengan "namespace"
def hp_potion():
    potion_strength = 2 #7 local scope untuk memberi fungsi di luar dari value yg diberikan (10)
    print(player_health+potion_strength) #7 tetap akan bisa memanggil value dari luar dan dari dalam fungsi
hp_potion()
print(player_health) #6 akan memanggil no.5 karena berada di luar fungsi & tidak akan terjadi error (global scope)