# Caesar Cipher Decryptor

Bu Python programı, verilen bir metni Caesar şifreleme algoritmasını kullanarak çözmek için kullanılır.

## Kullanım

1. `decrypt_caesar_cipher` fonksiyonu, şifreli metni ve kaydırma miktarını alarak metni çözer.
   ```python
   decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
from caesar_cipher import decrypt_caesar_cipher

# Örnek şifreli metin ve kaydırma miktarı
encrypted_text = "Khoor, Zruog!"
shift = 3

# Metni çöz
decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
print("Çözülmüş metin:", decrypted_text)

Bu README dosyası, `decrypt_caesar_cipher` fonksiyonunu kullanarak şifreli metni çözmenin nasıl yapıldığını ve örnek bir kullanımını açıklar.
