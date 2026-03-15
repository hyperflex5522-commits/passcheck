# PassCheck

PassCheck is a CLI password security tool built in Python.

## Features

- Password strength analysis
- Password list scanner
- Hash cracking using wordlists
- Colored CLI output
- Progress bars

## Usage

Check password strength:

```bash
passcheck -p Password123!
```

Scan password list:

```bash
passcheck -f wordlists/test.txt
```

Crack hash:

```bash
passcheck -H HASH -w wordlist.txt
```

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/passcheck.git
cd passcheck
pip install -r requirements.txt
```
