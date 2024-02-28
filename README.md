# Soundboard Description



## Introduction

Welcome to the GitHub repository of the Soundboard App! This SoundboardApp allows you to create a simple soundboard using the `tkinter` library of Python and `pygame` for playing sounds.

## Table of Contents

- [Installation](#installation)
- [Running the Soundboard](#running-the-soundboard)
- [Loading and Saving Configurations](#loading-and-saving-configurations)
- [Customizing Keys](#customizing-keys)
- [Troubleshooting](#troubleshooting)
- [Contribute](#contribute)

## Installation

### Prerequisites

Make sure you have the following installed on your computer before you begin:

- Python (recommended version 3.x)
- `Tkinter` (usually included with Python)
- Pygame library (`pip install pygame`)

### Clone Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to save the files of the SoundboardApp.
3. Execute the following command to clone the repository:

```bash
git clone https://github.com/x-actly/soundboard.git
```

## Running the Soundboard

Open the terminal or command prompt and navigate to the SoundboardApp directory:

```bash
cd soundboard-folder
```

Launch the SoundboardApp by executing the following command:

```bash
python main.py
```

## Loading and Saving Configurations

### Load Configuration

- Click the "Load Config" button in the Soundboard window.
  A file selection dialog will appear; choose an existing configuration file (.ini) and click "Open."
  The buttons on the soundboard will be configured according to the loaded file.

### Save Configuration

- Click the "Save Config" button in the Soundboard window.
  The current configuration will be saved in the default file `config.ini`.
  Alternatively, you can click "Save Config" and then "Save As" to choose a different filename and location.

## Customizing Keys

- To customize a key on the soundboard:
  Right-click on the desired key.
  A dialog box will appear:
  Enter a new name for the key.
  Select a sound file (.mp3 or .wav) by clicking "Browse."
  The new configuration will be automatically saved.

## Troubleshooting

- If you encounter issues:
  Check if Python and `Tkinter` are installed correctly.
  Ensure that the Pygame library is installed with `pip install pygame`.
  Verify if the sound files are in supported formats (mp3 or wav).
  For additional assistance, check the GitHub Issues page or create a new issue.

## Contribute

- If you have programming skills and want to contribute to the SoundboardApp:
  Fork the repository on GitHub.
  Make your changes and improvements.
  Submit a pull request to the original repository.
  Get involved! Your contributions are highly welcome!
