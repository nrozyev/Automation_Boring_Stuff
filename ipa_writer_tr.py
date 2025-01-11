ipa_col_tr = {
    "a": ["a", ["armut", "fal", "elma"],"ɑː", ["ağrı", "kağnı", "dağ"]],
    "b": "b",
    "c": "d͡ʒ",
    "ç": "t͡ʃ",
    "d": "d",
    "e": ["e", ["erik", "kel", "akide"], "eː", ["eğri", "değnek", "yeğ"]],
    "f": "f",
    "g": ["ɡ",["gaz", "yorgun", "diyalog"], "ɟ", ["gavur", "kevgir"]],
    "ğ": "ɣ",
    "h": "h",
    "i": ["i", ["ilaç", "kil", "kedi"], "i͡ɟ", ["iğne", "mevkiine", "tebliğ"]],
    "ı": ["ɯ", ["ıhlamur", "tıp", "kazı"], "ɯ͡ɟ", ["ığdır", "sığlık", "tığ"]],
    "j": "ʒ",
    "k": ["c", ["keçi", "ekşi", "bölük"], "k", ["kabak", "bakla", "çocuk"]],
    "l": ["l", ["leylek", "delik", "kil"], "ɮ", ["lala", "kalın", "pul"]],
    "m": "m",
    "n": ["n", ["nar", "inek", "sorun"], "ŋ", ["mangal", "ring"]],
    "o": ["o", ["orman", "kol", "vazo"], "o͡ɟ", ["oğlan", "doğru", "doğ"]],
    "ö": ["œ", ["ördek", "göl", "banliyö"], "œ͡ɟ", ["öğlen", "açıköğretim"]],
    "p": "p",
    "r": "ɾ",
    "s": "s",
    "ş": "ʃ",
    "t": "t",
    "u": ["u", ["uçak", "kuş", "koku"], "u͡ɟ", ["uğur", "buğra", "başbuğ"]],
    "ü": ["y", ["ülke", "gül", "öykü"], "y͡ɟ", ["düğme"]],
    "v": ["v", ["vadi", "tava", "ev"], "w", ["tavuk"]],
    "y": "j",
    "z": "z"}

ipa_word = str()
the_word = str()

def letter_to_ipa(letter):
    
    match letter:
        case "b" | "c" | "ç" | "d" | "f" | "ğ" | "h" | "j" | "m" | "p" | "r" | "s" | "ş" | "t" | "y" | "z":
            return ipa_col_tr[letter]
        case "a" | "e" | "i" | "ı" | "o" | "ö" | "u" | "ü":
            print(ipa_col_tr[letter])
            answer = input("Yanında 'ğ' harfi var mı?, küçük harfle y veya n yazın:")
            return ipa_col_tr[letter][2] if answer == "y" else ipa_col_tr[letter][0]
        case "g":
            print(ipa_col_tr[letter])
            answer = input("'g' harfi yumuşak mı sert mi? Yumuşaksa y, değilse n yazın:")
            return ipa_col_tr[letter][2] if answer == "y" else ipa_col_tr[letter][0]
        case "k":
            print(ipa_col_tr[letter])
            answer = input("'k' harfi yumuşak mı sert mi? Yumuşaksa y, değilse n yazın:")
            return ipa_col_tr[letter][0] if answer == "y" else ipa_col_tr[letter][2]
        case "l":
            print(ipa_col_tr[letter])
            answer = input("'l' harfi yumuşak mı sert mi? Yumuşaksa y, değilse n yazın:")
            return ipa_col_tr[letter][0] if answer == "y" else ipa_col_tr[letter][2]
        case "n":
            print(ipa_col_tr[letter])
            answer = input("'n' harfi damaktan mı değil mi? Damaktansa y, değilse n yazın:")
            return ipa_col_tr[letter][2] if answer == "y" else ipa_col_tr[letter][0]
        case "v":
            print(ipa_col_tr[letter])
            answer = input("'v' harfi kalın mı değil mi? Kalınsa y, değilse n yazın:")
            return ipa_col_tr[letter][2] if answer == "y" else ipa_col_tr[letter][0]
        
if __name__ == "__main__":

    while True:
        letter = input("Please enter a Turkish letter or 'x' to terminate:")
        if letter == "x":
            break
        else:
            the_word += letter
            letter_ipa = letter_to_ipa(letter)
            ipa_word += letter_ipa
            print(ipa_word)

    with open ("ipa_words_converted.txt", "a+", encoding = "utf-8") as fobj:
        fobj.write("\n")
        fobj.write(f'<phoneme alphabet="ipa" ph="{ipa_word}">{the_word}</phoneme>\n')
        fobj.write("Primary stress: ˈ Secondary stress: ˌ Syllable boundary: . Long: ː Linking: ‿ \n")
    