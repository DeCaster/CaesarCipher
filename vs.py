def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Karakterin ASCII değerini al
            ascii_value = ord(char)
            # Küçük harfler için
            if char.islower():
                decrypted_text += chr((ascii_value - 97 - shift) % 26 + 97)
            # Büyük harfler için
            elif char.isupper():
                decrypted_text += chr((ascii_value - 65 - shift) % 26 + 65)
        else:
            # Harf olmayan karakterleri aynen ekle
            decrypted_text += char
    return decrypted_text

# Örnek şifreli metin ve kaydırma miktarı
encrypted_text = "Khoor, Zruog!"
shift = 3

# Metni çöz
decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
print("Çözülmüş metin:", decrypted_text)
