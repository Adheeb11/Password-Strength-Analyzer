# Password Strength Analyzer

A simple command-line tool written in Python that evaluates how strong a password is and offers suggestions to improve it.

## Features

- **Strength scoring** — Rates passwords as Weak, Medium, Strong, or Very Strong
- **Rule-based checks** — Length, uppercase, lowercase, digits, and special characters
- **Common password detection** — Flags easily guessable passwords like `password` or `123456`
- **Actionable feedback** — Lists specific improvements for weak or medium passwords
- **Password suggestion** — Generates a random 12-character strong password when yours needs improvement

## Requirements

- Python 3.6 or later
- No external dependencies (uses only the standard library: `re`, `string`, `secrets`)

## Usage

Run the script from a terminal:

```bash
python pass_strength_check.py
```

When prompted, enter a password. The tool prints the strength rating and, if needed, suggestions plus a suggested alternative.

### Example

```
Enter Password: hello

Password Strength: Weak

Suggestions:
- Password should be at least 8 characters long.
- Add at least one uppercase letter (A-Z).
- Add at least one number (0-9).
- Add at least one special character (!,@,#,$,etc.).

Suggested Strong Password:
kT9#mQx2!pL@
```

## How Scoring Works

The analyzer awards points based on these criteria:

| Criterion              | Points |
|------------------------|--------|
| At least 8 characters  | +1     |
| At least 12 characters | +1     |
| Uppercase letter (A–Z) | +1     |
| Lowercase letter (a–z) | +1     |
| Digit (0–9)            | +1     |
| Special character      | +1     |

**Maximum score:** 6

| Score | Rating       |
|-------|--------------|
| 0–2   | Weak         |
| 3–4   | Medium       |
| 5     | Strong       |
| 6     | Very Strong  |

Passwords that match a known common password list receive a warning in the suggestions, even if they score well on other checks.

## Project Structure

```
pass_strength_analyzer/
├── pass_strength_check.py   # Main script
└── README.md
```

## License

This project is provided for educational and personal use.
