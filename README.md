# Unit-Converter
 A simple web app that can convert between different units of measurement. It can convert units of length, weight, and temperature. The user can input a value and select the units to convert from and to. The application will then display the converted value.

 This project is based on the [roadmap.sh Unit Converter project](https://roadmap.sh/projects/unit-converter).

## Features

- Convert between different units of measurement:
    - Length: Millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
    - Weight: Milligram, gram, kilogram, ounce, pound.
    - Temperature: Celsius, Fahrenheit, Kelvin.
- Separate pages for length, weight, and temperature conversions.

## Requirements

- Python 3
- uv

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install dependencies

The project uses `uv` for dependency management.

Run:

```bash
uv sync
```

This creates a `.venv` virtual environment if one does not already exist and synchronizes the installed dependencies with the versions specified in `uv.lock`.

## Usage

Start the FastAPI development server:

```bash
uv run fastapi dev
```

Open your browser and navigate to:

http://127.0.0.1:8000

Select Length, Weight, or Temperature, enter a value, choose the units to convert from and to, and click **Convert**.

The application processes the submitted form on the server and displays the converted value.

## Running Tests

Run the test suite with:

```bash
python3 -m unittest
```