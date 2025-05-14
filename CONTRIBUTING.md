# Contributing to AWS Icon Game

Thank you for your interest in contributing to the AWS Icon Game! This document provides guidelines and instructions for contributing.

## Ways to Contribute

There are several ways you can contribute to this project:

1. **Report bugs**: If you find a bug, please create an issue describing the problem, how to reproduce it, and your environment details.

2. **Suggest features**: Have an idea for a new feature? Open an issue to suggest it.

3. **Improve documentation**: Help improve the README, add comments to code, or create additional documentation.

4. **Submit code changes**: Fix bugs or add new features by submitting pull requests.

## Development Setup

1. Fork the repository on GitHub.

2. Clone your fork locally:
   ```
   git clone https://github.com/your-username/aws-icon-game.git
   cd aws-icon-game
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a branch for your changes:
   ```
   git checkout -b feature/your-feature-name
   ```

## Pull Request Process

1. Update the README.md with details of changes if applicable.

2. Make sure your code follows the existing style.

3. Make sure all tests pass.

4. Submit a pull request to the main repository.

## Code Style

- Follow PEP 8 style guidelines for Python code.
- Use meaningful variable and function names.
- Add comments to explain complex logic.

## Adding New AWS Services

To add new AWS services to the game:

1. Add the service to the `load_aws_services` method in `aws_icon_game.py`.
2. Create or obtain an icon for the service and place it in the `images` directory.
3. Update the placeholder icon generator if necessary.

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.

## Questions?

If you have any questions about contributing, please open an issue and we'll be happy to help!
