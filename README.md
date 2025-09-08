# Smart Task Manager

A beautiful and feature-rich terminal-based task management application built with Python and the Rich library.

![Smart Task Manager](https://img.shields.io/badge/Python-3.8%2B-blue)
![Rich Library](https://img.shields.io/badge/Rich-13.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

Smart Task Manager is a command-line application that helps you organize your tasks with a visually appealing interface. It features a custom ASCII art logo, color-coded tasks, priority levels, and category organization - all within your terminal.

## Features

- ✨ Beautiful terminal UI with custom ASCII art logo
- 📝 Add, edit, and delete tasks
- 🎯 Set priority levels (High, Medium, Low)
- 📂 Organize tasks by categories
- ✅ Mark tasks as complete/incomplete
- 📊 View task statistics and completion rates
- 💾 Persistent data storage (JSON)
- 🎨 Color-coded interface based on task status and priority

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.8 or higher installed
3. Install the required dependencies:

```bash
pip install rich
```

## Usage

Run the application with:

```bash
python smart_task_manager.py
```

### Navigation

- Use numbers to select menu options
- Follow the interactive prompts to manage tasks
- Tasks are automatically saved to `todo_data.json`

## Project Structure

```
smart-task-manager/
├── smart_task_manager.py  # Main application file
├── todo_data.json         # Task data storage (created automatically)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Technical Details

This application demonstrates several advanced Python concepts:
- Object-oriented programming
- File I/O operations with JSON
- Terminal UI development with Rich library
- Data persistence
- Error handling

## Contributing

Feel free to fork this project and submit pull requests for any enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Mahdi Nazari**  
Email: nazarimahdi.pro@gmail.com  
GitHub: [Your GitHub Profile URL]

## Acknowledgments

- Thanks to the [Rich](https://github.com/Textualize/rich) library for making terminal applications beautiful
- Inspired by the need for simple yet powerful task management tools

---

**Note**: This project was developed as a portfolio piece to demonstrate Python programming skills and clean code practices.