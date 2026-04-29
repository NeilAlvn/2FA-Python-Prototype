import pyotp
import qrcode
import time

def main():
    print("=====================================")
    print("   1. THE SETUP PHASE (One-Time)     ")
    print("=====================================\n")

    # 1. Generate a Secret
    # This generates a 32-character base32 secret string.
    user_secret = pyotp.random_base32()
    print(f"Secret generated: {user_secret}")

    # 2. Create the Provisioning URI
    # This formats the secret, app name, and user email into a standard URL format
    # that Google Authenticator knows how to read.
    totp_auth_uri = pyotp.totp.TOTP(user_secret).provisioning_uri(
        name="email",
        issuer_name="MyPythonPrototype"
    )

    # 3. Show a QR Code
    # We turn the URI into a QR code image and save it to the current folder.
    print("Generating QR code...")
    qr_image = qrcode.make(totp_auth_uri)
    qr_filename = "2fa_setup_qr.png"
    qr_image.save(qr_filename)
    
    print(f"\n✅ ACTION REQUIRED:")
    print(f"Open your folder and look at '{qr_filename}'.")
    print("Scan it with Google Authenticator (or Authy, Apple Passwords, etc.).\n")
    
    input("Press Enter once you have scanned the QR code into your app...")

    print("\n=====================================")
    print("   2. THE LOGIN PHASE (Every Time)   ")
    print("=====================================\n")

    # We initialize the TOTP object using the same secret we saved during setup.
    totp = pyotp.TOTP(user_secret)

    # Simulate the login loop
    while True:
        print("\n--- New Login Attempt ---")
        user_input = input("Enter the 6-digit code from your app (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Exiting prototype. Goodbye!")
            break

        # 4. Calculate and Compare
        # The verify() method calculates what the code SHOULD be right now based 
        # on the server's clock, and checks if the user's input matches.
        if totp.verify(user_input):
            print("✅ SUCCESS! The code matches. Logging you in...")
        else:
            print("❌ DENIED! Invalid or expired code. Try again.")

if __name__ == "__main__":
    main()