from character import Hero, Enemy
from weapon import short_bow, iron_sword, bazuuka

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

bazuuka_uses = 1

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    # print(f"Health of {hero.name}: {hero.health}")
    # print(f"Enemy of {enemy.name}: {enemy.health}")
    
    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

    if bazuuka_uses >= 1: 
        hero.equip(bazuuka)
        bazuuka_uses -= 1
        print(f"Using bazuuka! Uses left: {bazuuka_uses}")
    else: 
        hero.drop()