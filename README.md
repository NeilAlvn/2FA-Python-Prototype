🔐 2FA-Python-Prototype
A lightweight, terminal-based Python prototype demonstrating how Time-Based One-Time Password (TOTP) Two-Factor Authentication (2FA) works under the hood. 📱

📋 Overview
This project strips away web frameworks to focus purely on the core math and logic of generating 2FA secrets, creating QR codes, and validating user inputs in real-time. It is the perfect learning tool for understanding exactly how authenticator apps communicate securely with backend servers.

✨ Features
🎯 Setup Phase Simulation: Generates a secure base32 secret and a standardized provisioning URI

📷 QR Code Generation: Automatically creates a scannable QR code readable by standard authenticator apps

⚡ Real-time Validation: A continuous terminal loop that prompts for a 6-digit code and validates it

⏱️ Time-Window Security: Demonstrates how codes naturally expire after 30 seconds

📁 Project Structure
Plaintext
2FA-Python-Prototype/
├── 2fa_prototype.py         # Main application and logic script
├── requirements.txt         # Python dependencies list
└── README.md                # Project documentation
📋 Prerequisites
🐍 Python 3.7 or higher

📱 An Authenticator App (Google Authenticator, Authy, Apple Passwords, etc.)

💻 A terminal or command prompt

🔧 Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/2FA-Python-Prototype.git
cd 2FA-Python-Prototype
Install required dependencies:

Bash
pip install -r requirements.txt
(Alternatively: pip install pyotp qrcode[pil])

💡 Usage
Basic Usage
Run the prototype script in your terminal:

Bash
python 2fa_prototype.py
Next Steps Once Running
The script will generate an image file named 2fa_setup_qr.png in your folder.

Open the image and scan it with your authenticator app.

Return to the terminal, press Enter, and test your live 6-digit codes!

📦 Dependencies
The project relies on a few essential Python libraries for cryptography and image generation. Install all dependencies using the command above.

Common dependencies include:

🔐 pyotp - For generating secrets and handling the TOTP mathematical algorithm

⬛ qrcode - For turning the provisioning URI into a scannable image file

🖼️ Pillow (PIL) - Image processing backend required by the qrcode library

⚙️ How It Works
Secret Generation: The server creates a random 32-character base32 secret string linked to the user.

URI Creation: Formats the secret, app name, and user email into a standard provisioning URL.

QR Provisioning: Converts the URI into a QR code for the user to scan with their phone.

TOTP Math & Comparison: Calculates what the 6-digit code SHOULD be right now based on the server's clock, and checks if the user's input matches.

🔧 Troubleshooting
Common Issues
Issue: "Invalid or expired code" error keeps appearing even when typing correctly.

Solution: ✅ Ensure your phone's clock and your computer's clock are synced perfectly. TOTP relies strictly on synchronized server/client time.

Issue: QR Code image won't open or generate.

Solution: ✅ Check your project folder for 2fa_setup_qr.png and open it with your OS's default image viewer. Ensure you have write permissions in the directory.

Issue: Missing dependencies error (ModuleNotFoundError).

Solution: ✅ Run pip install pyotp qrcode[pil] to ensure the packages are installed in your active Python environment.

🤝 Contributing
Contributions are welcome! If you'd like to improve this project:

🍴 Fork the repository

🌿 Create a feature branch (git checkout -b feature/improvement)

💾 Commit your changes (git commit -am 'Add new feature')

📤 Push to the branch (git push origin feature/improvement)

🔀 Create a Pull Request

🚀 Future Improvements
[ ] 💾 Add database simulation (e.g., SQLite) to store user secrets

[ ] 🔑 Implement Backup Code generation and validation

[ ] 🌐 Create a simple Flask/FastAPI web wrapper for the logic

[ ] 🎨 Add a basic HTML/CSS frontend to replace the terminal output

[ ] 🛡️ Add rate-limiting to prevent brute-force attacks on the terminal prompt

📄 License
This project is open source. Please check the repository for license details.

🙏 Acknowledgments
🔐 The developers of the pyotp and qrcode Python libraries

🛡️ The open-source cybersecurity community

📧 Contact
For questions, issues, or suggestions, please open an issue on the GitHub repository.

📚 References
PyOTP Documentation

RFC 6238 - TOTP: Time-Based One-Time Password Algorithm

Python QRCode Library

⚠️ Note: This project is an educational prototype. If you are implementing 2FA in a production application, always provide Backup Codes. If a user loses their phone or deletes their authenticator app without backup codes, they will be locked out of their account forever.
