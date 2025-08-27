# Wordlist Generator

A simple Python script that generates custom wordlists based on target information.  
Optionally merges with a Turkish wordlist for broader coverage.  

---

## ✨ Features
- Generate wordlists using:
  - Name
  - Surname
  - Birth year
  - Pet name
- Automatic case variations (`lower`, `UPPER`, `Capitalized`)
- Add common suffixes (`1234`, `2025`, `!`, etc.)
- Merge with **Turkish wordlist (`turkce_wordlist.txt`)**
- Save results to a text file

---

## 🚀 Usage

### Run the script
```bash
python wordlist-generator.py


Target's Name: mert
Target's Surname: erkoc
Target's Birth Year: 2004
Target's Pet's Name: karabas
Include Turkish wordlist? (y/n): y
Enter filename to save wordlist (default: wordlist.txt): mywordlist.txt

✅ Merged custom wordlist with Turkish wordlist. Total: 15400 words.
📁 Wordlist saved as 'mywordlist.txt'


🛠 Requirements

Python 3.7+
No external dependencies (only standard library itertools is used)




This project is licensed under the MIT License.
Feel free to use, modify, and share. 🚀
