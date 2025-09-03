# Brute-Force PDF Password Breaker

# Brute-Forcing the pdf files to break the encryption using dictionary attack
import PyPDF2

# Load wordlist from dictionary
with open('dictionary.txt', 'r') as f:
    wordlist = f.read().splitlines()

# Open PDF
pdf_path = 'pdf_file.pdf'
pdfreader = PyPDF2.PdfReader(pdf_path)

# Check if PDF is encrypted
if pdfreader.is_encrypted:
    for word in wordlist:
        result = pdfreader.decrypt(word)
        if result:  # 1 means decryption successful
            print(f"Password found: {word}")
            break
    else:
        print("Password not found in dictionary.")
else:
    print("PDF is not encrypted.")

# Number of pages (works even for encrypted PDFs if decrypted)
print(f"Number of pages: {len(pdfreader.pages)}")

