import os
import sys
import subprocess

# Mappe der oppgavene ligger (python/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, "python")

# Menyvalg koblet til filnavn
FILES = {
    "1": "Question1.py",
    "2": "Question2.py",
    "3": "Question3.py",
    "4": "Question4.py",
    "5": "Question5.py",
}


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def run_question(choice: str):
    """Kjører valgt Python-fil som eget script."""
    file_name = FILES[choice]
    full_path = os.path.join(QUESTIONS_DIR, file_name)

    if not os.path.exists(full_path):
        print(f"❌ Fant ikke fil: {full_path}")
        return

    clear_screen()
    print(f"Running Question {choice} ({file_name})...")
    print("=" * 50)
    print()

    try:
        # Kjører med samme Python-tolker som Replit bruker
        subprocess.run([sys.executable, full_path])
    except Exception as e:
        print(f"\n❌ Klarte ikke å kjøre {file_name}: {e}")

    print("\n" + "=" * 50)
    input("\nPress Enter to return to menu...")


def main():
    while True:
        clear_screen()
        print("=== Python Exam – Oppgavevelger ===\n")
        print("Velg en oppgave:")
        print("1. Question1")
        print("2. Question2")
        print("3. Question3")
        print("4. Question4")
        print("5. Question5")
        print("0. Avslutt")

        choice = input("\nDitt valg: ").strip()

        if choice == "0":
            clear_screen()
            print("Avslutter...")
            sys.exit(0)

        if choice in FILES:
        # kjør valgt oppgave
            run_question(choice)
        else:
            print("Ugyldig valg.")
            input("Trykk ENTER for å fortsette...")


if __name__ == "__main__":
    main()
