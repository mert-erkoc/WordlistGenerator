import itertools

def get_target_info():
    t_name = input("Target's Name: ")
    t_surname = input("Target's Surname: ")
    t_birthyear = input("Target's Birth Year: ")
    t_petname = input("Target's Pet's Name: ")

    return {
        "name": t_name,
        "surname": t_surname,
        "birthyear": t_birthyear,
        "petname": t_petname
    }

def case_variations(word):
    return {
        word.lower(),
        word.upper(),
        word.capitalize()
    }

def generate_wordlist(info):
    name = info["name"]
    surname = info["surname"]
    year = info["birthyear"]
    pet = info["petname"]

    base_words = [name, surname, year, pet]

    all_variants = []
    for word in base_words:
        all_variants.append(list(case_variations(word)))

    combos = []
    for r in range(1, 4):  # name, name+surname, name+surname+year gibi
        for selected_words in itertools.combinations(all_variants, r):
            for product in itertools.product(*selected_words):
                combos.append("".join(product))

    suffixes = ["", "1234", "!", "@", "2025", "_", "01"]
    final_wordlist = set()

    for combo in combos:
        for suffix in suffixes:
            final_wordlist.add(combo + suffix)

    return list(final_wordlist)

def save_to_file(wordlist, filename="wordlist.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for word in wordlist:
            f.write(word + "\n")

def load_custom_wordlist(path="turkce_wordlist.txt"):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            words = {line.strip() for line in f if line.strip()}
        print(f"ℹ️ Loaded {len(words)} entries from '{path}'")
        return words
    except FileNotFoundError:
        print(f"⚠️ Wordlist file '{path}' not found.")
        return set()


def main():
    info = get_target_info()
    custom_words = generate_wordlist(info)

    use_extra = input("Include Turkish wordlist? (y/n): ").strip().lower()
    if use_extra == "y":
        extra_words = load_custom_wordlist()
        merged = set(custom_words).union(extra_words)
        print(f"✅ Merged custom wordlist with Turkish wordlist. Total: {len(merged)} words.")
    else:
        merged = set(custom_words)
        print(f"✅ Generated custom wordlist only. Total: {len(merged)} words.")


    filename = input("Enter filename to save wordlist (default: wordlist.txt): ").strip()
    if not filename:
        filename = "wordlist.txt"

    save_to_file(list(merged), filename)
    print(f"\n📁 Wordlist saved as '{filename}'")



if __name__ == "__main__":
    main()