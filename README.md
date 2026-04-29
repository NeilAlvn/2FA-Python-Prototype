# 🔐 2FA-Python-Prototype System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-010101?style=for-the-badge&logo=letsencrypt&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A lightweight, terminal-based Python prototype demonstrating the core mechanics of Time-Based One-Time Password (TOTP) Two-Factor Authentication (2FA). This system provides a transparent look at how backend servers generate secure secrets, create scannable QR codes, and validate live user inputs.

## 📋 Overview

This project strips away complex web frameworks to focus purely on the cryptographic math and logic of 2FA. It serves as an educational tool and a foundational prototype for developers looking to integrate Google Authenticator, Authy, or Apple Passwords functionality into their applications. 

## ✨ Key Features

### 🔍 Core Generation
- **Secret Creation** - Automatically generates highly secure, 32-character base32 secret strings
- **URI Formatting** - Constructs standardized provisioning URIs compatible with all major authenticator apps
- **QR Provisioning** - Dynamically renders the URI into a scannable `.png` image format

### 🔐 Real-Time Validation
- **Live Authentication** - Continuous terminal loop prompting for 6-digit code inputs
- **TOTP Mathematics** - Calculates valid codes on-the-fly based on the server's internal clock
- **Time-Window Security** - Demonstrates exact 30-second cryptographic expiration windows

## 🚀 Technologies Used

### Core Engine
- **Python 3** - Primary application logic and loop execution
- **PyOTP** - Cryptographic handling of the TOTP algorithm and secret generation

### Visual Output
- **QRCode** - Matrix barcode generation for the provisioning URI
- **Pillow (PIL)** - Image processing backend required for rendering the final image

## 📋 Prerequisites

Before installation, ensure you have:

- **Python 3.7+** installed
- **Terminal/Command Prompt** access
- **Authenticator App** (Google Authenticator, Authy, Microsoft Authenticator) installed on your mobile device
- **Image Viewer** capable of opening `.png` files

## 🔧 Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YourUsername/2FA-Python-Prototype.git](https://github.com/YourUsername/2FA-Python-Prototype.git)
   cd 2FA-Python-Prototype
Install Python dependencies

Bash
pip install -r requirements.txt
(Alternatively: pip install pyotp qrcode[pil])

Run the prototype

Bash
python 2fa_prototype.py
📁 Project Structure
Plaintext
2FA-Python-Prototype/
├── 2fa_prototype.py         # Main application and logic script
├── requirements.txt         # Python dependencies list
├── README.md                # Project documentation
└── output/                  # Generated files (created at runtime)
    └── 2fa_setup_qr.png     # The generated QR code image
🎯 Usage
1. The Setup Phase
Launch the script. The system will instantly generate a base32 secret.

Check your project directory for 2fa_setup_qr.png.

Open your preferred mobile authenticator app and scan the generated QR code.

2. The Verification Phase
Return to your terminal and press Enter to confirm scanning.

Type the 6-digit code currently displayed on your mobile device.

Watch the system validate or deny the code based on the current time window!

🔐 Security Features
Base32 Encoding - Industry-standard secret string generation

Ephemeral Codes - Passwords that naturally self-destruct after 30 seconds

Offline Validation - Verification relies strictly on synchronized time, requiring no internet ping to a third-party server

🛠️ Configuration
You can easily customize the issuer name and test email by editing these lines directly in 2fa_prototype.py:

Python
    # Configure your app identity here
    totp_auth_uri = pyotp.totp.TOTP(user_secret).provisioning_uri(
        name="user@yourdomain.com",
        issuer_name="MyPythonPrototype"
    )
🔧 Troubleshooting
Common Issues
Code Always Denied:

Cause: Time desynchronization.

Solution: Ensure your mobile phone's clock and your computer's system clock are perfectly synced to the exact second via the internet. TOTP relies strictly on matching timestamps.

ModuleNotFoundError:

Cause: Missing libraries in your active Python environment.

Solution: Re-run pip install pyotp qrcode[pil] and ensure you are operating in the correct virtual environment.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository

Create a feature branch (git checkout -b feature/NewFeature)

Commit your changes (git commit -m 'Add NewFeature')

Push to the branch (git push origin feature/NewFeature)

Open a Pull Request

🚧 Future Enhancements
[ ] Add SQLite integration to simulate storing users and secrets

[ ] Implement Backup Code generation (10 single-use fallback codes)

[ ] Add rate-limiting to prevent brute-force terminal entries

[ ] Build a simple Flask web wrapper to replace the terminal interface

[ ] Support SHA-256 and SHA-512 cryptographic hashes

🙏 Acknowledgments
Built to demonstrate core RFC 6238 implementation

Inspired by enterprise security requirements

Special thanks to the maintainers of the pyotp library

⭐ If you find this project useful, please consider giving it a star!

