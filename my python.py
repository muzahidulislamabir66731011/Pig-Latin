def to_pig_latin(word: str) -> str:
    word = word.lower()
    if word[0] in 'aeiou':
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

def main():
    while True:
        try:
            word = input("Write a word (press q to quit): ").strip()
            if word.lower() == "q":
                break

            if not word.isalpha():
                raise ValueError("Please enter letters only, no numbers or symbols.")

            print(to_pig_latin(word))

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
