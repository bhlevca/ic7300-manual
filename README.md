# IC-7300 Interactive Manual 📻

A comprehensive, interactive guide to the ICOM IC-7300 HF/50MHz transceiver built with Streamlit. Designed for beginners with step-by-step instructions, visual diagrams, and export capabilities.

![IC-7300](https://www.icomamerica.com/lineup/products/IC-7300/images/IC-7300_main.png)

## 🎯 Features

- **Interactive Navigation**: Hierarchical sidebar with collapsible chapters
- **Clickable Diagrams**: Interactive front/rear panel diagrams with tooltips
- **Step-by-Step Wizards**: Guided procedures with Next/Previous navigation
- **Full-Text Search**: Search across all content
- **Dark/Light Mode**: Toggle between display modes
- **Export Options**: Generate PDF or Word documents
- **Multi-Platform**: Digital mode guides for Windows and Linux

## 📚 Content Coverage

### Hardware Orientation
- Front panel layout with annotated diagrams
- Rear panel connections (antenna, ground, USB, ACC)
- Touch screen interface guide
- Button combinations and shortcuts

### Core Operations
- Power-on and initial setup
- Menu navigation
- Band selection and frequency entry
- Tuning techniques using waterfall display
- Mode selection (SSB, CW, AM, FM, RTTY, DATA)

### Antenna & SWR
- Built-in SWR meter usage
- Internal antenna tuner operation
- Interpreting SWR readings
- Manual and automatic tuning
- External tuner compatibility

### Spectrum Scope & Waterfall
- Center vs Fixed display modes
- Reference level adjustment
- Sweep speed settings
- Waterfall color customization
- Using the mini scope

### Digital Modes
- USB audio and CAT control setup
- WSJT-X (FT8/FT4) configuration
- Fldigi setup
- JS8Call configuration
- Audio levels and ALC settings
- Time synchronization

### Platform Guides
- Windows driver installation
- Linux (Ubuntu) setup
- Raspberry Pi configuration

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
# Clone the repository
git clone https://github.com/yourusername/ic7300-manual.git
cd ic7300-manual

# Run Streamlit app
streamlit run app.py
```

### Export Documents

```bash
# Generate PDF
python export/pdf_generator.py --output manual.pdf

# Generate Word document
python export/docx_generator.py --output manual.docx
```

## 📁 Project Structure

```
ic7300-manual/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── content/
│   ├── chapters/               # Markdown content per section
│   │   ├── 01_introduction.md
│   │   ├── 02_front_panel.md
│   │   ├── 03_rear_panel.md
│   │   ├── 04_basic_operations.md
│   │   ├── 05_spectrum_scope.md
│   │   ├── 06_antenna_swr.md
│   │   ├── 07_digital_modes.md
│   │   ├── 08_wsjt_ft8.md
│   │   ├── 09_fldigi_setup.md
│   │   ├── 10_js8call.md
│   │   └── 11_troubleshooting.md
│   ├── images/                 # Annotated diagrams, screenshots
│   └── quick_refs/             # Cheat sheets, reference tables
│       ├── button_shortcuts.md
│       ├── menu_tree.md
│       └── band_frequencies.md
├── export/
│   ├── pdf_generator.py        # WeasyPrint PDF export
│   └── docx_generator.py       # python-docx Word export
├── components/
│   ├── navigation.py           # Sidebar navigation component
│   ├── search.py               # Full-text search functionality
│   ├── interactive.py          # Interactive diagrams, tooltips
│   └── wizards.py              # Step-by-step procedure wizards
└── assets/
    ├── diagrams/               # SVG/PNG panel diagrams
    └── screenshots/            # Radio screen captures
```

## 🔧 Configuration

### IC-7300 Settings for Digital Modes

The following settings should be configured on your IC-7300 for digital mode operation:

| Setting | Path | Value |
|---------|------|-------|
| DATA MOD | MENU > SET > Connectors | USB |
| USB MOD Level | MENU > SET > Connectors | 40-50% |
| CI-V USB Baud Rate | MENU > SET > Connectors | 115200 |
| CI-V USB Echo Back | MENU > SET > Connectors | ON |
| Mode | Main screen | USB-D |

### Software Requirements

| Software | Version | Purpose |
|----------|---------|---------|
| WSJT-X | 2.6+ | FT8/FT4/WSPR |
| Fldigi | 4.1+ | PSK31/RTTY/CW |
| JS8Call | 2.2+ | JS8 Mode |
| Meinberg NTP | Latest | Time sync (Windows) |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- ICOM Inc. for the IC-7300 transceiver
- The amateur radio community for sharing their knowledge
- K0PIR, M0NWK, WA7EWC and other hams who documented their setups
- W1HKJ for Fldigi and Flrig software

## 📞 Resources

- [ICOM IC-7300 Official Page](https://www.icomamerica.com/lineup/products/IC-7300/)
- [ICOM IC-7300 Full Manual (PDF)](https://www.icomjapan.com/support/manual/2271/)
- [WSJT-X Official Site](https://wsjt.sourceforge.io/)
- [Fldigi Wiki](https://sourceforge.net/p/fldigi/wiki/Home/)
- [JS8Call](http://js8call.com/)

---

*Created by amateur radio operators, for amateur radio operators. 73!*
