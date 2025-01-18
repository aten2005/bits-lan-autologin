# BITS LAN AutoLogin

This script automates the login process for the BITS Pilani Hyderabad campus LAN network, eliminating the need for manual sign-in.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Required Libraries**: Install necessary Python packages using the provided `requirements.txt` file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aten2005/bits-lan-autologin.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd bits-lan-autologin
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set Up the `.env` File**:
   - Create a file named `.env` in the project directory.
   - Add your BITS LAN credentials in the following format:
     ```
     id="f20xxyyyy"
     password="my-password"
     ```

   Replace `f20xxyyyy` and `my-password` with your actual LAN ID and password.

2. **(Optional) Customize Script**:
   - If necessary, edit the script to match specific network requirements (e.g., URLs, form field names).

## Packaging as an Executable

To make the script easier to use and share, you can package it as a standalone executable file using **PyInstaller**.

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Package the Script**:
   Run the following command to create a single-file executable:
   ```bash
   pyinstaller --onefile -w --add-data=".env:." main.py
   ```
3. **Locate the Executable**:
   After the command completes, the executable will be in the `dist` directory.

4. **Run the Executable**:
   Double-click the executable or run it from the command line.

5. The executable can now be added to the Windows task scheduler to run at regular intervals.

## Usage

Run the script with the following command:
```bash
python main.py
```

The script will read your credentials from the `.env` file and log you into the BITS LAN network automatically.

## Troubleshooting

- **Login Failures**: Double-check your credentials in the `.env` file and ensure they are correct.
- **Environment Issues**: Ensure the `.env` file is in the same directory as `main.py` and correctly formatted.
- **Packaging Issues**: Ensure the `--add-data` option is correctly specified when running `pyinstaller`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
