# echo.py


# the function takes a string as a parameter
def echo(text: str, repetitions: int = 3) -> str:
    """Imitiate a real-world echo."""
    # takes the last three characters of the input
    echo_section = text[-3:]
    # creates the fading echo
    echo_fade = [echo_section[i:] for i in range(repetitions)]
    # this is the format of the output
    return text + "\n" + "\n".join(echo_fade) + "\n."


if __name__ == "__main__":
    # asking user for an imput
    text = str(input("Yell something at a mountain: "))
    # printing the echo function
    print(echo(text))
