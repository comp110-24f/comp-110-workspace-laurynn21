""" Challenge Question 00"""

__author__ = "730460185"


# Define the function
def mimic(message: str) -> str:
    """Message should be mimiced back to me"""
    return message


def main() -> None:
    """To print the result of calling mimic"""

    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
