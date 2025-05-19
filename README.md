# AWS Service Icon Game

A fun and educational game to test your knowledge of AWS service icons!

![AWS Icon Game Screenshot](screenshot.png)

## Overview

The AWS Service Icon Game is a simple yet engaging application that helps users learn to identify AWS service icons. Players are presented with an AWS service icon and must select the correct service name from multiple options. The game continues until the player loses three lives.

## Features

- Interactive GUI built with Tkinter
- Comprehensive collection of AWS service icons (56 services)
- Multiple difficulty levels (Easy, Medium, Hard)
- Category selection to focus on specific AWS service types
- Visual timer with color changes for Medium and Hard modes
- Visual feedback for correct/incorrect answers
- Score tracking with heart-based lives system
- Game over screen with restart option
- Services organized by AWS categories:
  - Compute
  - Storage
  - Database
  - Networking & Content Delivery
  - Security, Identity & Compliance
  - Management & Governance
  - Application Integration
  - Developer Tools
  - Analytics
  - Machine Learning
  - API Services

## Requirements

- Python 3.6+
- Tkinter (usually comes with Python)
- Pillow (PIL Fork)
- Requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/aws-icon-game.git
   cd aws-icon-game
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. AWS service icons:
   The game includes placeholder icons for all services. For a better experience, you can replace these with official AWS icons:
   
   a. Download official AWS icons from the [AWS Architecture Icons page](https://aws.amazon.com/architecture/icons/)
   
   b. Extract the ZIP file and find the service icons you need
   
   c. Rename them to match the filenames used in the game and place them in the `images/` directory

## How to Play

1. Run the game:
   ```
   python aws_icon_game.py
   ```

2. You will be presented with an AWS service icon and three possible service names.

3. Click on the button with the name that matches the icon.

4. If correct, your score increases and a new icon appears.

5. If incorrect, you lose a life. The game ends when you lose all three lives.

6. After the game ends, you can choose to play again or quit.

## Customizing the Game

### Adding More Services

You can easily extend the game by adding more AWS services to the `load_aws_services` method in the `AWSIconGame` class. Each service needs a name and an icon filename.

### Changing Difficulty

To adjust the difficulty, you can modify the game to:
- Show more or fewer answer options
- Group services by category
- Add time limits for answers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- AWS for their amazing services and icons
- The Python community for the excellent libraries

---

Created with ❤️ for the AWS Community
