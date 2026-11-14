
from importlib import resources
from pathlib import Path


def main():

    print("\n========================")
    print("       SBMPBOX")
    print("========================")

    codes_folder = resources.files("sbmpbox").joinpath("codes")

    files = sorted(
        file for file in codes_folder.iterdir()
        if file.is_file() and file.name.endswith(".txt")
    )

    if not files:
        print("\nNo code files available!")
        return

    print("\nAvailable Python Codes:\n")

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")

    print(f"{len(files) + 1}. Exit")

    choice = input("\nEnter your choice: ")

    if choice.isdigit():

        choice = int(choice)

        if 1 <= choice <= len(files):

            selected_file = files[choice - 1]

            code = selected_file.read_bytes()

            Path(selected_file.name).write_bytes(code)

            print("\nDownloaded:", selected_file.name)

        elif choice == len(files) + 1:
            print("\nThank you for using SBMPBOX!")

        else:
            print("\nInvalid choice!")

    else:
        print("\nPlease enter a valid number!")


if __name__ == "__main__":
    main()
