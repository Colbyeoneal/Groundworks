from dataclasses import dataclass
from typing import List
import sys

@dataclass
class Level:
    name: str
    target: int
    description: str
    bonus_power: int
    unlocks: List[str]


LEVELS = [
    Level(
        name="Workshop",
        target=20,
        description="Make your first widgets by hand.",
        bonus_power=1,
        unlocks=["buy"]
    ),
    Level(
        name="Factory",
        target=100,
        description="Unlock a small factory and scale production.",
        bonus_power=2,
        unlocks=["machine"]
    ),
    Level(
        name="Automation",
        target=400,
        description="Automate production and multiply output.",
        bonus_power=3,
        unlocks=["auto"]
    ),
    Level(
        name="AI R&D",
        target=1500,
        description="Use AI to optimize output and win the game.",
        bonus_power=5,
        unlocks=["research"]
    ),
]


class Game:
    def __init__(self):
        self.widgets = 0
        self.power = 1
        self.level_index = 0
        self.upgrade_cost = 10
        self.auto_active = False
        self.machine_active = False
        self.research_points = 0

    @property
    def level(self) -> Level:
        return LEVELS[self.level_index]

    def status(self) -> str:
        unlocked = [cmd for level in LEVELS[: self.level_index + 1] for cmd in level.unlocks]
        actions = ["make", "status", "help", "quit"]
        if "buy" in unlocked:
            actions.append("buy")
        if "machine" in unlocked:
            actions.append("machine")
        if "auto" in unlocked:
            actions.append("auto")
        if "research" in unlocked:
            actions.append("research")
        return (
            f"Level: {self.level.name}\n"
            f"Widgets: {self.widgets}\n"
            f"Power: {self.power} widgets per make\n"
            f"Upgrade cost: {self.upgrade_cost} widgets\n"
            f"Next level target: {self.level.target} widgets\n"
            f"Unlocked actions: {', '.join(sorted(actions))}\n"
        )

    def make(self) -> str:
        gain = self.power + (5 if self.machine_active else 0)
        if self.auto_active:
            gain += 2
        self.widgets += gain
        message = f"You made {gain} widgets. Total: {self.widgets}."
        return message + self.check_level()

    def buy(self) -> str:
        if self.widgets < self.upgrade_cost:
            return f"Need {self.upgrade_cost - self.widgets} more widgets to upgrade."
        self.widgets -= self.upgrade_cost
        self.power += 1
        self.upgrade_cost = int(self.upgrade_cost * 1.8)
        return f"Upgrade purchased! Power is now {self.power}. Next upgrade costs {self.upgrade_cost}."

    def machine(self) -> str:
        if self.machine_active:
            return "Machine is already active."
        if self.widgets < 50:
            return "Need 50 widgets to build the machine."
        self.widgets -= 50
        self.machine_active = True
        return "Machine built! Each make now produces +5 extra widgets."

    def auto(self) -> str:
        if self.auto_active:
            return "Automation is already running."
        if self.widgets < 200:
            return "Need 200 widgets to turn the factory fully automatic."
        self.widgets -= 200
        self.auto_active = True
        return "Automation engaged! You get +2 bonus widgets each make."

    def research(self) -> str:
        if self.widgets < 500:
            return "Need 500 widgets to fund AI research."
        self.widgets -= 500
        self.research_points += 1
        self.power += 3
        return (
            "AI research completed! Power increased by 3. "
            f"Research points: {self.research_points}."
        )

    def check_level(self) -> str:
        if self.widgets >= self.level.target and self.level_index < len(LEVELS) - 1:
            self.level_index += 1
            self.power += self.level.bonus_power
            next_level = self.level.name
            return f"\n*** Level up! Now in {next_level}. {self.level.description} ***"
        if self.level_index == len(LEVELS) - 1 and self.widgets >= self.level.target:
            return "\n*** You reached the final level and finished the game! Congratulations! ***"
        return ""

    def help_text(self) -> str:
        return (
            "Commands:\n"
            "  make      - produce widgets using current power\n"
            "  status    - show current progress and available actions\n"
            "  buy       - increase widget production power\n"
            "  machine   - build a small machine for extra widgets per make\n"
            "  auto      - enable automation for a production bonus\n"
            "  research  - unlock AI improvements for higher power\n"
            "  help      - show this help text\n"
            "  quit      - exit the game\n"
        )


def main() -> None:
    game = Game()
    print("Welcome to Groundworks: a simple incremental production game!")
    print("Type 'help' to see commands. Reach the final level to win.")
    print(game.status())

    while True:
        action = input("\n> ").strip().lower()
        if action in {"q", "quit", "exit"}:
            print("Thanks for playing Groundworks!")
            break
        if action in {"make", "m"}:
            print(game.make())
        elif action == "status":
            print(game.status())
        elif action == "buy":
            print(game.buy())
        elif action == "machine":
            print(game.machine())
        elif action == "auto":
            print(game.auto())
        elif action == "research":
            print(game.research())
        elif action == "help":
            print(game.help_text())
        else:
            print("Unknown command. Type 'help' for available actions.")

        if game.level_index == len(LEVELS) - 1 and game.widgets >= game.level.target:
            print("You have completed the game! Great job.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)