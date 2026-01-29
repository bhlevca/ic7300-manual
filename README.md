# IC-7300 Interactive Manual 📻

[![CI](https://github.com/bhlevca/ic7300-manual/actions/workflows/ci.yml/badge.svg)](https://github.com/bhlevca/ic7300-manual/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, interactive guide to the ICOM IC-7300 HF/50MHz transceiver built with Streamlit. Designed for beginners with step-by-step instructions, visual diagrams, and export capabilities.

![IC-7300](https://www.icomamerica.com/lineup/products/IC-7300/images/IC-7300_main.png)

## ✨ Features

- **Tabbed Navigation** - Easy access to all sections via intuitive tabs
- **Interactive Panel Diagrams** - SVG diagrams of front and rear panels with detailed control descriptions
- **Expandable Sections** - Chapter content organized with collapsible sections
- **Step-by-Step Wizards** - Guided procedures for common tasks (First Power On, Antenna Tuning, FT8 Setup)
- **Full-Text Search** - Search across all documentation
- **Quick Reference** - Band frequencies, button shortcuts, menu tree
- **Responsive Design** - Works on desktop and mobile browsers

## 📚 Content Coverage

### Hardware Orientation
- Front panel layout with annotated SVG diagrams
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

### Digital Modes
- USB audio and CAT control setup
- WSJT-X (FT8/FT4) configuration
- Fldigi setup
- Audio levels and ALC settings

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/bhlevca/ic7300-manual.git
cd ic7300-manual

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Run the application
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Development Installation

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run linting
ruff check .
black --check .

# Run tests
pytest
```

## 📁 Project Structure

```
ic7300-manual/
├── app.py                      # Main Streamlit application
├── pyproject.toml              # Project configuration & dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── CHANGELOG.md                # Version history
├── CONTRIBUTING.md             # Contribution guidelines
├── components/
│   ├── __init__.py
│   ├── interactive.py          # Panel control definitions
│   ├── navigation.py           # Navigation helpers
│   ├── search.py               # Search functionality
│   └── wizards.py              # Step-by-step wizards
├── content/
│   ├── chapters/               # Markdown documentation
│   │   ├── 01_introduction.md
│   │   ├── 02_front_panel.md
│   │   ├── 03_rear_panel.md
│   │   └── ...
│   └── quick_refs/             # Quick reference tables
│       ├── band_frequencies.md
│       ├── button_shortcuts.md
│       └── menu_tree.md
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions CI
```

## 🖥️ Usage

### Running Locally

```bash
streamlit run app.py
```

### Running with Docker (coming soon)

```bash
docker build -t ic7300-manual .
docker run -p 8501:8501 ic7300-manual
```

## 🛠️ Technologies

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Python](https://www.python.org/)** - Programming language
- **SVG** - Scalable vector graphics for diagrams
- **Markdown** - Documentation format

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute

- 📝 Improve documentation and content
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 🌐 Add translations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- ICOM for creating the excellent IC-7300 transceiver
- The amateur radio community for their support and feedback
- All contributors to this project

## 📞 Contact

- GitHub Issues: [Report a bug](https://github.com/bhlevca/ic7300-manual/issues)
- Author: Bogdan Hlevca

## ⚠️ Disclaimer

This is an unofficial, community-created manual. It is not affiliated with or endorsed by ICOM. Always refer to the official ICOM documentation for authoritative information.

---

**73 de the IC-7300 Manual Team!** 📻
