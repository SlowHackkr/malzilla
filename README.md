# 🦠 Malzilla — Malware Analyzer

Malzilla is a simple, VirusTotal-style malware file scanner built with Flask. It allows users to upload files and receive an instant analysis report, including file type, cryptographic hashes, and YARA rule matches for basic malware detection.

---

## Features

- **File Upload & Analysis:** Upload suspicious files (e.g., `.exe`, `.pdf`, `.zip`, `.docx`, etc.) for analysis.
- **File Type Detection:** Uses `python-magic` and `filetype` to determine MIME type and file description.
- **Cryptographic Hashes:** Computes MD5, SHA1, and SHA256 hashes for file identification.
- **YARA Rule Scanning:** Optionally scans files with YARA rules for malware signatures (if rules are provided).
- **Modern UI:** Clean, responsive interface styled with Tailwind CSS.
- **Extensible:** Easily add more analysis modules or integrate with external services.

---

## How It Works

1. **Upload:** User selects and uploads a file via the web interface.
2. **Analysis:** The backend extracts file information, computes hashes, and (optionally) scans with YARA rules.
3. **Report:** Results are displayed in a clear, readable report.

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/malzilla.git
cd malzilla/malzilla
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:**  
> - For file type detection, `python-magic` may require system libraries (`libmagic`).  
> - On Windows, you may also need `python-magic-bin`:
>   ```
>   pip install python-magic-bin
>   ```

### 4. (Optional) Add YARA Rules

If you want YARA scanning, add a `yara_rules.yar` file in the project directory with your YARA rules.

### 5. Run the Application

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Usage

1. Click "Choose File" and select a file to analyze.
2. Click "Upload & Analyze".
3. View the analysis report, including:
   - File name, type, and size
   - MD5, SHA1, SHA256 hashes
   - YARA rule matches (if any)

---

## Project Structure

```
malzilla/
├── app.py                # Main Flask app
├── utils/
│   └── analyzer.py       # File analysis logic
├── templates/
│   └── index.html        # Frontend template
├── static/
│   ├── css/style.css     # Styles
│   └── js/main.js        # JS enhancements
├── uploads/              # Uploaded files (auto-created)
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── ...                   # Other config files
```

---

## Security Notice

- **Do not use this in production as-is.**
- This tool is for educational/demo purposes only.
- Uploaded files are saved to disk and not scanned in a sandbox.
- No authentication or advanced security is implemented.

---

## Extending Malzilla

- Add more analysis modules (e.g., integrate with VirusTotal API, static/dynamic analysis).
- Improve frontend with more detailed reports or charts.
- Add authentication and user management.

---

## License

This project is open-source. See [LICENSE](LICENSE) for details.

---

## Credits

- Built with [Flask](https://flask.palletsprojects.com/)
- File type detection via [python-magic](https://github.com/ahupp/python-magic) and [filetype](https://github.com/h2non/filetype.py)
- YARA scanning via [yara-python](https://github.com/VirusTotal/yara-python)

---

## Contact

For questions or suggestions, please open an issue or contact the maintainer.

