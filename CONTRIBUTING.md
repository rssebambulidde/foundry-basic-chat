# Contributing to SamaBrains AI Projects
Thank you for your interest in contributing to our AI engineering projects!
## Code Standards
### Python Style

# Contributing Guide

---

Thank you for your interest in contributing to our AI engineering projects!

---

## Code Standards

### Python Style

- Follow PEP 8
- Use type hints for function signatures
- Keep functions focused and testable
- Add docstrings to all public functions

### Commenting

- Comment "why", not "what"
- Explain complex logic
- Document assumptions and limitations
- Include example usage for utilities

### Testing

- Write tests for new features
- Test both happy path and error cases
- Maintain >80% code coverage
- Use descriptive test names

---

## Development Setup

```bash
# Clone and setup
git clone <repository>
cd <project>

# Virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies with dev extras
pip install -r requirements.txt
```

---

## Making Changes

1. **Create a branch:**
   ```bash
   git checkout -b feature/description
   ```

2. **Make changes:**
   - Keep commits atomic and focused
   - Write descriptive commit messages
   - Test locally before pushing

3. **Submit for review:**
   - Push your branch
   - Create a pull request
   - Reference any related issues

---

## Commit Message Format

```text
type(scope): brief description

Optional detailed explanation of changes.
- Point 1
- Point 2

Fixes #123
```

**Types:**

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code restructuring
- `test:` Test additions/updates
- `perf:` Performance improvements

---

## Code Review Checklist

- [ ] Code follows PEP 8 style guide
- [ ] Type hints are present
- [ ] Docstrings are complete
- [ ] Tests pass locally
- [ ] No unnecessary dependencies added
- [ ] Error handling is appropriate
- [ ] Comments explain the why
- [ ] No hardcoded secrets or credentials

---

## Reporting Issues

When reporting bugs, include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs or error messages

---

## License

By contributing, you agree your code is licensed under MIT.

---

**Questions?** Contact us at [contact@samabrains.com](mailto:contact@samabrains.com)
cd <project>

# Virtual environment
python -m venv venv
venv\\Scripts\\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies with dev extras
pip install -r requirements.txt
```

## Making Changes

1. **Create a branch:**
   ```bash
   git checkout -b feature/description
   ```

2. **Make changes:**
   - Keep commits atomic and focused
   - Write descriptive commit messages
   - Test locally before pushing

3. **Submit for review:**
   - Push your branch
   - Create a pull request
   - Reference any related issues

## Commit Message Format

```
type(scope): brief description

Optional detailed explanation of changes.
- Point 1
- Point 2

Fixes #123
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code restructuring
- `test:` Test additions/updates
- `perf:` Performance improvements

## Code Review Checklist

- [ ] Code follows PEP 8 style guide
- [ ] Type hints are present
- [ ] Docstrings are complete
- [ ] Tests pass locally
- [ ] No unnecessary dependencies added
- [ ] Error handling is appropriate
- [ ] Comments explain the why
- [ ] No hardcoded secrets or credentials

## Reporting Issues

When reporting bugs, include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs or error messages

## License

By contributing, you agree your code is licensed under MIT.

---

**Questions?** Contact us at [contact@samabrains.com](mailto:contact@samabrains.com)
"