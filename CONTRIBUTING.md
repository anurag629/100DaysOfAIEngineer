# Contributing to 100 Days of AI Engineer

Thank you for your interest in contributing to the 100 Days of AI Engineer project! This document provides guidelines and instructions for contributing.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

---

## Code of Conduct

By participating in this project, you agree to:

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards other community members
- Accept constructive criticism gracefully

---

## How Can I Contribute?

### 1. Reporting Bugs or Issues

If you find a bug or issue, please:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with a clear title and description
3. **Include details**:
   - What you expected to happen
   - What actually happened
   - Steps to reproduce
   - Your environment (OS, Python version, etc.)

### 2. Suggesting Enhancements

Have an idea to improve the curriculum? We'd love to hear it!

1. **Check existing issues** for similar suggestions
2. **Create a new issue** with the tag `enhancement`
3. **Describe your suggestion** clearly:
   - What problem does it solve?
   - How would it benefit learners?
   - Any implementation ideas?

### 3. Fixing Broken Links

Found a broken link in the resources?

1. **Locate the file** containing the broken link
2. **Find a suitable replacement** resource
3. **Submit a pull request** with the fix
4. Include a brief explanation of the change

### 4. Adding Code Examples

We welcome additional code examples!

1. **Focus on clarity** over complexity
2. **Add comments** explaining key concepts
3. **Follow the existing structure** in `daily_checklists/dayXX/code/`
4. **Test your code** before submitting
5. Include a docstring explaining what the code demonstrates

### 5. Improving Documentation

Help make our documentation better:

- Fix typos or grammatical errors
- Clarify confusing explanations
- Add missing information
- Improve formatting and structure

### 6. Sharing Your Journey

Completed the challenge or made significant progress?

1. Add your name to `HALL_OF_FAME.md`
2. Share your experience in the Discord community
3. Create a blog post or video about your journey
4. Help others who are starting out

---

## Getting Started

### Prerequisites

- Git installed on your machine
- GitHub account
- Basic knowledge of Markdown
- Python 3.8+ (for code contributions)

### Fork and Clone

1. **Fork the repository** to your GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/100DaysOfAIEngineer.git
   cd 100DaysOfAIEngineer
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/anurag629/100DaysOfAIEngineer.git
   ```

4. **Create a new branch** for your contribution:
   ```bash
   git checkout -b fix/broken-link-day15
   # or
   git checkout -b feature/add-code-example-day05
   ```

---

## Contribution Guidelines

### Branch Naming Conventions

Use descriptive branch names:

- `fix/broken-link-dayXX` - For fixing broken links
- `feature/add-example-dayXX` - For adding new examples
- `docs/update-readme` - For documentation updates
- `enhancement/improve-dayXX` - For curriculum improvements

### Commit Message Guidelines

Write clear, concise commit messages:

**Good Examples:**
```
Fix broken YouTube link in day30 README
Add NumPy matrix operations example for day01
Update PROJECT_GUIDE.md with detailed requirements
Improve explanation of transformers in day62
```

**Bad Examples:**
```
Fixed stuff
Update
Changes
asdf
```

**Format:**
```
<type>: <short description>

<optional longer description>
<optional reference to issue>
```

**Types:**
- `fix:` - Bug fixes
- `feat:` - New features
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### File Structure Guidelines

When adding code examples:

```
daily_checklists/dayXX/
├── README.md
├── code/
│   ├── example_name.py          # Your code here
│   └── README.md                # Optional: explain examples
├── notebooks/
│   └── example_notebook.ipynb   # Optional: Jupyter notebooks
└── notes.md
```

---

## Pull Request Process

### Before Submitting

1. **Sync with upstream**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test your changes**:
   - Run code examples to ensure they work
   - Check all links are valid
   - Verify markdown formatting

3. **Review your changes**:
   ```bash
   git diff
   ```

### Submitting Your PR

1. **Push your branch**:
   ```bash
   git push origin your-branch-name
   ```

2. **Create Pull Request** on GitHub

3. **Fill out the PR template**:
   - **Title**: Clear, descriptive title
   - **Description**: What changes you made and why
   - **Related Issue**: Link to relevant issue if applicable
   - **Testing**: How you tested your changes

4. **Wait for review**: Maintainers will review your PR
   - Be responsive to feedback
   - Make requested changes promptly
   - Be patient - reviews may take time

### PR Review Criteria

Your PR will be evaluated on:

- **Quality**: Does it improve the project?
- **Accuracy**: Is the information/code correct?
- **Clarity**: Is it easy to understand?
- **Consistency**: Does it match the existing style?
- **Completeness**: Is it fully implemented?

---

## Style Guidelines

### Markdown Guidelines

- Use clear, concise language
- Follow existing formatting patterns
- Use headers appropriately (H1 for title, H2 for sections, etc.)
- Include code blocks with appropriate syntax highlighting
- Keep lines under 120 characters when possible

### Python Code Guidelines

Follow PEP 8 with these specifics:

```python
# Good: Clear, commented, well-structured
def calculate_accuracy(predictions, labels):
    """
    Calculate classification accuracy.

    Args:
        predictions (np.ndarray): Model predictions
        labels (np.ndarray): True labels

    Returns:
        float: Accuracy score between 0 and 1
    """
    correct = (predictions == labels).sum()
    total = len(labels)
    return correct / total


# Bad: No comments, unclear
def calc(p, l):
    return (p == l).sum() / len(l)
```

**Guidelines:**
- Use descriptive variable names
- Add docstrings to functions
- Include inline comments for complex logic
- Keep functions focused and small
- Add type hints when appropriate

### Resource Link Guidelines

When adding or fixing resource links:

- **Verify the link works** before submitting
- **Use descriptive link text**: `[NumPy Tutorial](URL)` not `[Click here](URL)`
- **Prefer stable sources**: Official docs, well-maintained repos, reputable sites
- **Check for HTTPS**: Use secure links when available
- **Avoid paywalls**: Don't link to content requiring payment

---

## Testing Your Contributions

### For Code Examples

```bash
# Run your Python script
python daily_checklists/day01/code/your_example.py

# Check for syntax errors
python -m py_compile your_example.py

# Optional: Run with different Python versions
python3.8 your_example.py
python3.9 your_example.py
```

### For Links

- Click every link you add or modify
- Ensure they lead to the expected content
- Check they work in different browsers if relevant

### For Documentation

- Preview your Markdown changes locally
- Check formatting renders correctly
- Verify any code blocks have correct syntax highlighting

---

## Community

### Get Help

- **Discord**: Join the [CODERCOPS Discord](https://discord.gg/9eFXYntYa8)
- **Issues**: Open a GitHub issue with your question
- **Discussions**: Use GitHub Discussions for broader topics

### Stay Connected

- Follow updates on the repository
- Participate in Discord discussions
- Share your progress using `#100DaysOfAIEngineer`
- Help others who are learning

---

## Recognition

Contributors who make significant improvements will be:

- Recognized in project documentation
- Mentioned in release notes
- Added to contributors list
- Featured in the community (with permission)

---

## Questions?

If you have questions about contributing, please:

1. Check this document thoroughly
2. Search existing issues
3. Ask in the Discord community
4. Open a new issue with the `question` tag

---

## Thank You!

Every contribution, no matter how small, helps make this resource better for everyone. Thank you for taking the time to contribute to 100 Days of AI Engineer!

**Remember**: We all started somewhere. Don't be afraid to contribute, even if you're new to open source. We're here to help you learn!

---

**Happy Contributing! 🚀**

*Last Updated: 2025*
