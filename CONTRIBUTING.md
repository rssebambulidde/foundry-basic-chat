# Contributing Guide

Thank you for your interest in contributing to SamaBrains AI projects.

## Code Standards

### Python Style

- Follow PEP 8.
- Use type hints for function signatures.
- Keep functions focused and testable.
- Add docstrings to public functions when they provide useful context.

### Comments

- Comment why something is done, not what each line does.
- Explain complex logic and important assumptions.
- Document limitations that affect users or maintainers.

### Testing

- Write tests for new features when practical.
- Cover both happy paths and important error cases.
- Use descriptive test names.

## Development Setup

```bash
# Clone and setup
git clone <repository>
cd <project>

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## Making Changes

1. Create a branch:

   ```bash
   git checkout -b feature/description
   ```

2. Make your changes:

   - Keep commits focused.
   - Write descriptive commit messages.
   - Test locally before pushing.

3. Submit for review:

   - Push your branch.
   - Create a pull request.
   - Reference any related issues.

## Commit Message Format

```text
type(scope): brief description

Optional detailed explanation of changes.
- Point 1
- Point 2

Fixes #123
```

Common types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation change
- `refactor`: Code restructuring
- `test`: Test additions or updates
- `perf`: Performance improvement

## Code Review Checklist

- [ ] Code follows the project style.
- [ ] Type hints are present where useful.
- [ ] Documentation is updated where needed.
- [ ] Tests or manual verification were completed.
- [ ] No unnecessary dependencies were added.
- [ ] Error handling is appropriate.
- [ ] No hardcoded secrets or credentials were introduced.

## Reporting Issues

When reporting bugs, include:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant logs or error messages

## License

By contributing, you agree that your contributions are licensed under the MIT License.

## Questions

Contact [contact@samabrains.com](mailto:contact@samabrains.com).
