
# PySet Library / Библиотека PySet

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://pypi.org/project/pyset-sorting)

---

## English

### Overview

PySet is a powerful Python library that automatically sorts and organizes objects into sets based on their properties. It classifies numbers (positive, negative, even, odd, decimal) and words (palindromes, by length, by first letter) without any manual work.

### Features

| Feature | Description |
|---------|-------------|
|  **Number Classification** | Positive, negative, zero, even, odd, decimal, integer |
|  **Word Classification** | By length, palindromes, vowel/consonant start |
|  **Automatic Sorting** | Objects are classified automatically when added |
|  **Set Operations** | Union, intersection, difference, symmetric difference |
|  **Filtering** | Custom conditions, range queries, prime numbers |
|  **Statistics** | Get counts and information about all sets |
|  **CLI Interface** | Interactive command line tool |
|  **Specialized Classes** | NumberSet and WordSet for specific use cases |

### Installation

#### Using pip (recommended)

```bash
# install from PyPI
pip install pyset-sorting

# or install with specific version
pip install pyset-sorting==1.0.0
```

#### From source

```bash
# clone repository
git clone https://github.com/yourusername/pyset.git
cd pyset

# install in development mode
pip install -e .

# or regular installation
pip install .
```

### Quick Start

```python
from pyset import PySet

# create instance
ps = PySet()

# add data (mixed types)
ps.add(5, -3, 10, -8, 0, 3.14, 2.5, -1.7)
ps.add("python", "java", "level", "radar", "world")

# get sets
print(ps.get_positive())      # {5, 10, 3.14, 2.5}
print(ps.get_negative())      # {-3, -8, -1.7}
print(ps.get_even())          # {10, -8}
print(ps.get_palindrome())    # {'level', 'radar'}

# filter words by length
words = ps.get_words_by_length(4, 6)
print(words)  # {'java', 'world', 'level'}

# get statistics
stats = ps.get_stats()
print(f"Total items: {stats['total_items']}")
print(f"Numbers: {stats['total_numbers']}")
print(f"Words: {stats['total_words']}")
```

### Working with Numbers

```python
from pyset import PySet, NumberSet

# using generic PySet
ps = PySet()
ps.add(1, 2, 3, 4, 5, -1, -2, -3, 0, 3.14, 2.71)

print("Positive:", ps.get_positive())
print("Negative:", ps.get_negative())
print("Even:", ps.get_even())
print("Odd:", ps.get_odd())
print("Decimal:", ps.get_decimal())
print("Prime numbers:", ps.get_primes())
print("Numbers in range [-2, 3]:", ps.get_numbers_in_range(-2, 3))

# using specialized NumberSet
ns = NumberSet()
ns.add_range(1, 20)  # add numbers from 1 to 20
ns.add(25, 30, 36, 49)

print("\nPerfect squares:", ns.get_perfect_squares())
print("Fibonacci numbers:", ns.get_fibonacci())
print("Multiples of 5:", ns.get_multiples_of(5))
```

### Working with Words

```python
from pyset import WordSet

ws = WordSet()
ws.add(
    "apple", "banana", "orange", "grape",
    "level", "radar", "madam", "refer",
    "python", "java", "rust", "c"
)

# word classification
print("Palindromes:", ws.get_palindrome())
print("Start with vowel:", ws.get_vowel_start())
print("Start with consonant:", ws.get_consonant_start())

# filtering by length
print("Words length 5-6:", ws.get_words_by_length(5, 6))

# advanced word operations
print("Words with 3 vowels:", ws.get_by_vowel_count(3))
print("Sorted by length:", ws.sort_by_length())
print("Sorted alphabetically:", ws.sort_alphabetically())

# find anagrams
ws.add("race", "care", "acre")
print("Anagrams of 'race':", ws.get_anagrams("race"))
```

### Set Operations

```python
from pyset import PySet

ps = PySet()
ps.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even = ps.get_even()      # {2, 4, 6, 8, 10}
odd = ps.get_odd()        # {1, 3, 5, 7, 9}
primes = ps.get_primes()  # {2, 3, 5, 7}

# basic set operations
print("Union (even ∪ primes):", ps.union(even, primes))
print("Intersection (even ∩ primes):", ps.intersection(even, primes))
print("Difference (odd - primes):", ps.difference(odd, primes))
print("Symmetric diff (odd ^ primes):", ps.symmetric_difference(odd, primes))

# set comparisons
print("Is even subset of numbers?", ps.is_subset(even, ps.get_all_numbers()))
print("Are odd and primes disjoint?", ps.is_disjoint(odd, primes))
```

### Custom Filtering

```python
from pyset import PySet

ps = PySet()
ps.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ps.add("cat", "dog", "elephant", "bee", "butterfly")

# custom number filter
greater_than_5 = ps.filter_numbers(lambda x: x > 5)
print("Numbers > 5:", greater_than_5)

# custom word filter
contains_e = ps.filter_words(lambda w: 'e' in w)
print("Words containing 'e':", contains_e)

# create custom named sets
ps.create_custom_set("small_numbers", [1, 2, 3])
ps.create_custom_set("large_numbers", [100, 200, 300])
print("Custom set 'small_numbers':", ps.get_custom_set("small_numbers"))
```

### Statistics

```python
from pyset import PySet

ps = PySet()
ps.add(10, -5, 3, -8, 0, 2.5, -1.3, 42)
ps.add("hello", "world", "level", "python", "radar", "code")

stats = ps.get_stats()
print("\n=== STATISTICS ===")
for key, value in stats.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
```

### Command Line Interface

After installation, you can use the interactive CLI:

```bash
# start interactive shell
pyset
```

Available commands:

| Command | Description |
|---------|-------------|
| `help` | Show help menu |
| `stats` | Show statistics |
| `positive` | Show positive numbers |
| `negative` | Show negative numbers |
| `even` | Show even numbers |
| `odd` | Show odd numbers |
| `decimal` | Show decimal numbers |
| `primes` | Show prime numbers |
| `palindromes` | Show palindrome words |
| `words [min] [max]` | Filter words by length |
| `range [start] [end]` | Numbers in range |
| `vowels` | Words starting with vowel |
| `consonants` | Words starting with consonant |
| `add [items]` | Add new items |
| `compare [set1] [set2]` | Compare two sets |
| `clear` | Clear all data |
| `exit` | Exit program |

Example CLI session:
```bash
$ pyset

pyset> add 1,2,3,4,5,-1,-2,hello,world,level
items added

pyset> stats
total_items: 10
total_numbers: 7
total_words: 3
positive: 5
negative: 2
even: 3
odd: 4

pyset> positive
positive: {1, 2, 3, 4, 5}

pyset> palindromes
palindromes: {'level'}
