from goblin import Goblin
from hero import Hero

ARENA_NAME = "Aura bura"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("house")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    NewGobblin= Goblin("house")
    print("Omg I can feel the haha phonk coming, aura is arriving")

    aura = Hero("aura")
    auraAttackNumber = aura.attack()
    goblin.take_damage(auraAttackNumber)
    if goblin.health > 0:
        goblinAttackNumber = goblin.attack()
        print("Ou sart shes coming baclk, RUN AURA!")
        aura.take_damage(goblinAttackNumber)


if __name__ == "__main__":
    main()

