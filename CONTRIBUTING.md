# Contributing to IC-7300 Interactive Manual

First off, thank you for considering contributing to the IC-7300 Interactive Manual! It's people like you that make this resource valuable for the amateur radio community.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct: be respectful, inclusive, and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (screenshots, error messages)
- **Describe the behavior you observed and what you expected**
- **Include your environment** (OS, Python version, Streamlit version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any alternatives you've considered**

### Adding Content

We welcome contributions to the manual content! You can help by:

- **Improving existing chapters** - Fix errors, clarify instructions, add tips
- **Adding new chapters** - Cover topics not yet documented
- **Creating wizards** - Step-by-step guides for common procedures
- **Adding translations** - Help make the manual accessible to more operators

#### Content Guidelines

- Write for beginners - assume minimal prior knowledge
- Use clear, concise language
- Include practical tips and warnings where appropriate
- Follow the existing markdown formatting conventions
- Test any procedures on an actual IC-7300 if possible

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Install dependencies**: `pip install -e ".[dev]"`
3. **Make your changes**
4. **Test your changes**: Run `streamlit run app.py` and verify
5. **Format your code**: `black .` and `ruff check .`
6. **Commit your changes** with a clear commit message
7. **Push to your fork** and submit a pull request

#### Pull Request Guidelines

- Follow the existing code style
- Update documentation as needed
- Add tests if applicable
- Keep PRs focused - one feature/fix per PR
- Reference any related issues

## Development Setup

```bash
# Clone the repository
git clone https://github.com/bhlevca/ic7300-manual.git
cd ic7300-manual

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run the application
streamlit run app.py
```

## Project Structure

```
ic7300-manual/
├── app.py                 # Main Streamlit application
├── components/            # Python modules
│   ├── interactive.py     # Panel control definitions
│   ├── navigation.py      # Navigation helpers
│   ├── search.py          # Search functionality
│   └── wizards.py         # Step-by-step wizards
├── content/
│   ├── chapters/          # Markdown documentation
│   └── quick_refs/        # Quick reference tables
└── assets/                # Images and diagrams
```

## Style Guide

### Python

- Follow PEP 8
- Use type hints where practical
- Write docstrings for functions
- Maximum line length: 100 characters

### Markdown Content

- Use ATX-style headers (`#`, `##`, `###`)
- Include code blocks with language hints
- Use tables for structured data
- Add emoji for visual interest (💡 tips, ⚠️ warnings)

## Questions?

Feel free to open an issue for any questions about contributing. We're happy to help!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
