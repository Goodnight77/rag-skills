# Contributing to rag-skills

Thank you for your interest in contributing to rag-skills! This document provides guidelines for submitting new skills, reviewing existing skills, and maintaining the repository.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Submitting New Skills](#submitting-new-skills)
- [Skill Review Criteria](#skill-review-criteria)
- [Naming Conventions](#naming-conventions)
- [Testing and Validation](#testing-and-validation)
- [Credit and Attribution](#credit-and-attribution)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Development Setup

### Running Validation

## Submitting New Skills

### Step 1: Choose Your Topic

Before creating a new skill, check that:

1. The topic is not already covered by an existing skill
2. The topic is relevant to RAG systems
3. You have practical experience with the topic

### Step 2: Use the Template

Start with [templates/skill-template.md](templates/skill-template.md):
Use the template as a lightweight reference format: brief illustrative text, no long runnable code, and 3-5 external implementation links folded into the relevant sections instead of a separate `References` block.

### Step 3: Place Your Skill

Organize skills by category:

If your category doesn't exist, create it in the appropriate location.

### Step 4: Validate Your Skill

Run the validation script and fix any errors before submitting.

### Step 5: Submit a Pull Request

1. Commit your changes
2. Push to your fork
3. Open a pull request with a descriptive title

Example PR title: `Add skill: Semantic Chunking for Markdown Documents`

## Skill Review Criteria

When reviewing skills, maintainers evaluate them against these criteria:

### Clarity

- [ ] Is the problem statement clear and specific?
- [ ] Are key concepts well-defined?
- [ ] Are implementation steps logically ordered?
- [ ] Is the writing free of ambiguity?

### Accuracy

- [ ] Are the technical statements correct?
- [ ] Do code examples run as expected?
- [ ] Are references valid and current?
- [ ] Are the metrics/success criteria realistic?

### Completeness

- [ ] All required sections are present
- [ ] Code examples are brief and illustrative, not full implementations
- [ ] Related skills are properly linked
- [ ] Both use cases and anti-patterns are covered

### Practicality

- [ ] The skill addresses a real-world problem
- [ ] The approach is production-viable
- [ ] The complexity matches the difficulty level
- [ ] Dependencies are reasonable and well-known

### Code Quality

- [ ] Code follows Python conventions (PEP 8)
- [ ] Code includes comments for complex logic
- [ ] Code handles errors appropriately
- [ ] Code examples stay lightweight and defer to external implementations

## Naming Conventions

### Skill Files

- Use kebab-case: `semantic-chunking.md`
- Be descriptive: `hybrid-search-bm25-dense.md`
- Keep names under 50 characters

### Categories

Use existing category names:
- `chunking`
- `vector-databases`
- `retrieval-strategies`
- `data-type-handling`
- `performance-optimization`
- `evaluation-metrics`
- `rag-agents`
- `deployment`

### Levels

Use one of:
- `beginner` — Basic concepts, minimal dependencies
- `intermediate` — Some experience required, moderate complexity
- `advanced` — Expert knowledge, complex implementations

If you keep the level field in a skill file, treat it as metadata for filtering rather than a required browsing path in the README.

### Tags

- Use 3-5 relevant tags per skill
- Use lowercase: `["semantic", "nlp", "context"]`
- Avoid overly specific tags
- Focus on searchable terms

## Testing and Validation

### Local Validation

Before submitting, ensure your skill passes validation:

Strict mode treats warnings as errors.

### Link Validation

Verify all internal links work and that external implementation links are placed inline in the relevant step or sentence:

## Credit and Attribution

### Author Field

Include your name in the `author` field:

For organizational contributions:

### Last Updated

Update the `last_updated` field with the current date:

### Co-Authors

For substantial contributions from multiple people, list them in the pull request description:

## Reporting Issues

When reporting issues, include:

- A clear title
- Steps to reproduce
- Expected vs actual behavior
- Environment information
- Screenshots if applicable

### Issue Templates

#### Bug Report

#### Feature Request

## Community Guidelines

### Discussions

- Use GitHub Discussions for questions and ideas
- Be specific in your questions
- Share code snippets when helpful
- Follow up on responses

### Code Review

- Be constructive in your reviews
- Explain the reasoning for suggested changes
- Acknowledge good work
- Be patient with maintainers' time

### Maintainer Response Time

Maintainers aim to respond to:
- Pull requests: Within 7 days
- Issues: Within 7 days
- Discussions: Within 3 days

## Additional Resources

- [Project README](README.md)
- [Skill Template](templates/skill-template.md)
- [GitHub Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)

Thank you for contributing to rag-skills!
