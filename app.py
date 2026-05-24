
import subprocess
import sys
from pathlib import Path
from commands.add import add_command
from commands.view import view_command
from commands.edit import edit_command
from commands.delete import delete_command
from runTests import testQ


def clear_screen():
    """
    Clear the terminal screen without using os:
    Uses ANSI escape codes which work on most terminals
    (including Windows 10+ cmd/powershell with ANSI enabled).
    """
    # Clear entire screen and move cursor to home position
    print("\033[2J\033[H", end="")


def run_menu_loop():
    while True:
        print("\nWhat Action would you like to perform?")
        print("1. Add")
        print("2. Delete")
        print("3. Edit")
        print("4. View")
        print("5. Clear")
        print("6. Run Test Queries")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            print("You selected: Add")
            add_command()
        elif choice == "2":
            print("You selected: Delete")
            delete_command()
        elif choice == "3":
            print("You selected: Edit")
            edit_command()
        elif choice == "4":
            print("You selected: View")
            view_command()
        elif choice == "5":
            clear_screen()
        elif choice == "6":
            print("Running Test Queries...")
            testQ()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")


def main():
    if "--session" not in sys.argv:
        script_path = Path(__file__).resolve()
        cwd = script_path.parent

        
        subprocess.Popen(
            [sys.executable, str(script_path), "--session"],
            cwd=str(cwd)
        )

        
        return

    run_menu_loop()


if __name__ == "__main__":
    main()
