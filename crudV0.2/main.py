import notes
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
def menu():
    logger.info("\n📌 Notes manager ")
    logger.info("1📌. Add note ")
    logger.info("2📌. Show all notes ")
    logger.info("3📌. Update note ")
    logger.info("4📌. Remove a note ")
    logger.info("5📌. Exit ")


def main():
    notes.create_table()
    
    while True:
        menu()
        choice = input("\nChouse ure actions:  ")
        if choice == '1':
            title = input("Enter the title: ")
            content = input("Enter the body: ")
            notes.create_note(title, content)
            logger. info("CHECK✅ the note has been added")

        elif choice == '2':
            all_notes = notes.read_notes()
            
            if all_notes:
                logger.info("\n The list of all ure notes")

                for note in all_notes:
                    logger.info(f"\n ID: {note[0]} \n Body: {note[2]}")
        elif choice =='3':
            note_id = input("Enter the note id 4 updating: ")
            title = input("Enter new title: ")
            content = input("Enter new body: ")
            notes.update_note(note_id)
            logger. info("CHECK✅ Note has been updated")

        elif choice =='4':
            note_id = input("Enter the note id 4 deleting: ")
            notes.delete_note(note_id)
            logger. info("CHECK✅ Note has been deleted")

        elif choice =='5':
            logger. info("CHECK✅ Excit ")
            break
        else:
            logger.warning("wrong. try again")

if __name__ == "__main__":
    main()