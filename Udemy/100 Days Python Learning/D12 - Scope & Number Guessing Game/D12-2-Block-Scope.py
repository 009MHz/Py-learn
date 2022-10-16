#Local Scope
def refine_success():
    weapon_level = "+1"
    print(weapon_level)
refine_success() 

#Global Scope
player_health = 10 
def hp_potion():
    potion_strength = 2 
    print(player_health+potion_strength) 
hp_potion()
print(player_health)

#Block Scope
game_lvl = "easy"
enemies = ["Skeleton","Zombie", "Undead"]
if game_lvl == "easy": #1 if statement tidak akan menjadi block scope karena bisa dipanggil dari luar scope (indentation yg bersangkutan)
    new_enemy = enemies[0]
    
print(new_enemy) #2 fungsi yg memanggil value dari dalam scope

game_lvl = "medium"
def spawn_enemy():
    if game_lvl == "medium": #3 if statement menjadi blocksope karena berada di dalam fungsi def()
        med_enemy = enemies[0:2]
print(med_enemy) #4 fungsi ini menjadi tidak valid karena value yg dipanggil menjadi local scope 