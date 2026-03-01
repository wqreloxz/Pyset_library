#!/usr/bin/env python3
"""
command line interface for pyset
"""

import sys
from .core import PySet, NumberSet, WordSet
from .utils import compare_sets


def main():
    """main cli function"""
    ps = PySet()
    
    # add example data
    ps.add(5, -3, 10, -8, 0, 3.14, 2.5, -1.7, 42, -15, 7, 11)
    ps.add("python", "java", "rust", "c", "javascript", "kotlin")
    ps.add("level", "radar", "world", "hello", "madam", "refer")
    
    print("\n" + "=" * 60)
    print("pyset - interactive shell")
    print("=" * 60)
    print("type 'help' for commands, 'exit' to quit")
    
    while True:
        try:
            cmd = input("\npyset> ").strip().split()
            
            if not cmd:
                continue
            
            cmd = cmd[0].lower()
            
            if cmd == "exit":
                print("goodbye!")
                sys.exit(0)
            
            elif cmd == "help":
                print("\navailable commands:")
                print("  help                 - show this help")
                print("  stats                - show statistics")
                print("  positive             - show positive numbers")
                print("  negative             - show negative numbers")
                print("  even                 - show even numbers")
                print("  odd                  - show odd numbers")
                print("  decimal              - show decimal numbers")
                print("  primes               - show prime numbers")
                print("  palindromes          - show palindrome words")
                print("  words [min] [max]    - words by length")
                print("  range [start] [end]  - numbers in range")
                print("  vowels               - words starting with vowel")
                print("  consonants           - words starting with consonant")
                print("  add [items...]       - add items (comma separated)")
                print("  compare [a] [b]      - compare two sets")
                print("  clear                - clear all data")
                print("  exit                 - exit program")
            
            elif cmd == "stats":
                stats = ps.get_stats()
                for k, v in stats.items():
                    print(f"  {k}: {v}")
            
            elif cmd == "positive":
                print("positive:", ps.get_positive())
            
            elif cmd == "negative":
                print("negative:", ps.get_negative())
            
            elif cmd == "even":
                print("even:", ps.get_even())
            
            elif cmd == "odd":
                print("odd:", ps.get_odd())
            
            elif cmd == "decimal":
                print("decimal:", ps.get_decimal())
            
            elif cmd == "primes":
                print("primes:", ps.get_primes())
            
            elif cmd == "palindromes":
                print("palindromes:", ps.get_palindrome())
            
            elif cmd == "vowels":
                print("vowel start:", ps.get_vowel_start())
            
            elif cmd == "consonants":
                print("consonant start:", ps.get_consonant_start())
            
            elif cmd == "multiples":
                n = int(input("enter number: "))
                print(f"multiples of {n}:", ps.get_multiples_of(n))
            
            elif cmd == "range":
                start = float(input("start: "))
                end = float(input("end: "))
                print(f"numbers in range [{start}, {end}]:", 
                      ps.get_numbers_in_range(start, end))
            
            elif cmd == "words":
                min_len = int(input("min length: "))
                max_len = input("max length (enter for same): ")
                if max_len:
                    max_len = int(max_len)
                else:
                    max_len = min_len
                print(ps.get_words_by_length(min_len, max_len))
            
            elif cmd == "add":
                items = input("enter items (comma separated): ").split(',')
                for item in items:
                    item = item.strip()
                    try:
                        if '.' in item:
                            ps.add(float(item))
                        else:
                            ps.add(int(item))
                    except ValueError:
                        ps.add(item)
                print("items added")
            
            elif cmd == "compare":
                print("compare two sets")
                print("available: positive, negative, even, odd, decimal")
                a_name = input("first set: ")
                b_name = input("second set: ")
                
                sets = {
                    'positive': ps.positive,
                    'negative': ps.negative,
                    'even': ps.even,
                    'odd': ps.odd,
                    'decimal': ps.decimal,
                    'integer': ps.integer,
                    'palindrome': ps.palindrome
                }
                
                if a_name in sets and b_name in sets:
                    result = compare_sets(sets[a_name], sets[b_name])
                    for k, v in result.items():
                        print(f"  {k}: {v}")
                else:
                    print("invalid set names")
            
            elif cmd == "clear":
                ps.clear()
                print("all data cleared")
            
            else:
                print(f"unknown command: {cmd}")
        
        except KeyboardInterrupt:
            print("\ngoodbye!")
            sys.exit(0)
        
        except Exception as e:
            print(f"error: {e}")


if __name__ == "__main__":
    main()
