# LeetCode Solutions

This repository contains my progress through LeetCode problems, documenting my journey as I work through algorithmic challenges and data structure problems.

## Repository Purpose

- **Track Progress**: Store my work as I progress through LeetCode problems
- **Learning Documentation**: Record both successful solutions and learning from mistakes
- **Solution Evolution**: Show the progression from initial attempts to optimized solutions

## Solution Approach

### Initial Solutions
- First solutions pushed are generally my own work
- Represents my initial understanding and approach to each problem
- May be partial or incomplete solutions

### Iterative Improvement
- When I can only come up with a partial solution, I review what went wrong
- Push corrected solutions that may be partially or completely AI-assisted
- Focus on understanding the concepts and techniques used

### Testing Strategy
- Tests are generally AI-generated to ensure comprehensive coverage
- Each problem includes multiple test cases covering edge cases and examples from the problem statement

## Repository Structure

Each problem is organized in its own directory with the following structure:

```
<Problem Number>. <Problem Name>/
├── README.md       # Problem description and examples
├── solution.py     # Solution implementation
└── test.py        # Comprehensive test cases
```

## Running Tests

To run tests for a specific problem:

```bash
cd "<Problem Number>. <Problem Name>"
python test.py
```

To run tests for all problems:

```bash
find . -name "test.py" -execdir python {} \;
```
