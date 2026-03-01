"""
core classes for pyset library
"""

class PySet:
    """main class for sorting and managing objects in sets"""
    
    def __init__(self):
        """initialize empty sets"""
        self.numbers = []
        self.words = []
        self.mixed = []
        
        # number sets
        self.positive = set()
        self.negative = set()
        self.zero = set()
        self.even = set()
        self.odd = set()
        self.decimal = set()
        self.integer = set()
        
        # word sets
        self.word_length = {}
        self.palindrome = set()
        self.vowel_start = set()
        self.consonant_start = set()
        
        # custom sets
        self.custom_sets = {}
    
    def add(self, *items):
        """add items to library"""
        for item in items:
            self.mixed.append(item)
            
            if isinstance(item, (int, float)):
                self.numbers.append(item)
                self._classify_number(item)
            
            elif isinstance(item, str):
                self.words.append(item)
                self._classify_word(item)
        
        return self
    
    def _classify_number(self, num):
        """classify number by properties"""
        # sign classification
        if num > 0:
            self.positive.add(num)
        elif num < 0:
            self.negative.add(num)
        else:
            self.zero.add(num)
        
        # parity classification
        if num % 2 == 0:
            self.even.add(num)
        else:
            self.odd.add(num)
        
        # type classification
        if isinstance(num, float):
            self.decimal.add(num)
        else:
            self.integer.add(num)
    
    def _classify_word(self, word):
        """classify word by properties"""
        # length classification
        length = len(word)
        if length not in self.word_length:
            self.word_length[length] = set()
        self.word_length[length].add(word)
        
        # palindrome check
        if word == word[::-1]:
            self.palindrome.add(word)
        
        # first letter classification
        if word and word[0].lower() in 'aeiou':
            self.vowel_start.add(word)
        else:
            self.consonant_start.add(word)
    
    # getter methods
    def get_positive(self):
        """return positive numbers"""
        return self.positive
    
    def get_negative(self):
        """return negative numbers"""
        return self.negative
    
    def get_zero(self):
        """return zero"""
        return self.zero
    
    def get_even(self):
        """return even numbers"""
        return self.even
    
    def get_odd(self):
        """return odd numbers"""
        return self.odd
    
    def get_decimal(self):
        """return decimal numbers (float)"""
        return self.decimal
    
    def get_integer(self):
        """return integer numbers"""
        return self.integer
    
    def get_palindrome(self):
        """return palindrome words"""
        return self.palindrome
    
    def get_vowel_start(self):
        """return words starting with vowel"""
        return self.vowel_start
    
    def get_consonant_start(self):
        """return words starting with consonant"""
        return self.consonant_start
    
    def get_all_numbers(self):
        """return all numbers"""
        return set(self.numbers)
    
    def get_all_words(self):
        """return all words"""
        return set(self.words)
    
    # filter methods
    def filter_numbers(self, condition):
        """filter numbers by custom condition"""
        return {n for n in self.numbers if condition(n)}
    
    def filter_words(self, condition):
        """filter words by custom condition"""
        return {w for w in self.words if condition(w)}
    
    def get_words_by_length(self, min_len, max_len=None):
        """get words within length range"""
        if max_len is None:
            max_len = min_len
        
        result = set()
        for length, words in self.word_length.items():
            if min_len <= length <= max_len:
                result.update(words)
        return result
    
    def get_words_starting_with(self, letter):
        """get words starting with specific letter"""
        letter = letter.lower()
        return {w for w in self.words if w.lower().startswith(letter)}
    
    def get_words_ending_with(self, letter):
        """get words ending with specific letter"""
        letter = letter.lower()
        return {w for w in self.words if w.lower().endswith(letter)}
    
    def get_numbers_in_range(self, start, end):
        """get numbers within range [start, end]"""
        return {n for n in self.numbers if start <= n <= end}
    
    def get_primes(self):
        """get prime numbers"""
        def is_prime(n):
            if n < 2 or not isinstance(n, int):
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        return {n for n in self.integer if n > 0 and is_prime(n)}
    
    def get_multiples_of(self, n):
        """get numbers that are multiples of n"""
        if n == 0:
            return set()
        return {num for num in self.numbers if num % n == 0}
    
    # set operations
    def union(self, *sets):
        """union of multiple sets"""
        result = set()
        for s in sets:
            result |= s
        return result
    
    def intersection(self, *sets):
        """intersection of multiple sets"""
        if not sets:
            return set()
        result = sets[0].copy()
        for s in sets[1:]:
            result &= s
        return result
    
    def difference(self, a, b):
        """difference between sets (a - b)"""
        return a - b
    
    def symmetric_difference(self, a, b):
        """symmetric difference (a ^ b)"""
        return a ^ b
    
    # comparison
    def is_subset(self, a, b):
        """check if a is subset of b"""
        return a.issubset(b)
    
    def is_superset(self, a, b):
        """check if a is superset of b"""
        return a.issuperset(b)
    
    def is_disjoint(self, a, b):
        """check if sets are disjoint"""
        return a.isdisjoint(b)
    
    # custom sets
    def create_custom_set(self, name, items):
        """create named custom set"""
        self.custom_sets[name] = set(items)
        return self
    
    def get_custom_set(self, name):
        """get custom set by name"""
        return self.custom_sets.get(name, set())
    
    # statistics
    def get_stats(self):
        """get statistics about all data"""
        return {
            'total_items': len(self.mixed),
            'total_numbers': len(self.numbers),
            'total_words': len(self.words),
            'positive': len(self.positive),
            'negative': len(self.negative),
            'zero': len(self.zero),
            'even': len(self.even),
            'odd': len(self.odd),
            'decimal': len(self.decimal),
            'integer': len(self.integer),
            'palindrome': len(self.palindrome),
            'vowel_start': len(self.vowel_start),
            'consonant_start': len(self.consonant_start),
            'unique_lengths': len(self.word_length)
        }
    
    def clear(self):
        """clear all data"""
        self.__init__()
        return self


class NumberSet(PySet):
    """specialized class for numbers only"""
    
    def __init__(self):
        super().__init__()
    
    def add_range(self, start, end, step=1):
        """add range of numbers"""
        for i in range(start, end + 1, step):
            self.add(i)
        return self
    
    def get_factors(self, n):
        """get factors of n"""
        if n <= 0:
            return set()
        return {i for i in self.integer if i > 0 and n % i == 0}
    
    def get_perfect_squares(self):
        """get perfect squares"""
        return {n for n in self.integer if n > 0 and 
                int(n ** 0.5) ** 2 == n}
    
    def get_perfect_cubes(self):
        """get perfect cubes"""
        return {n for n in self.integer if n > 0 and 
                round(n ** (1/3)) ** 3 == n}
    
    def get_fibonacci(self):
        """get fibonacci numbers"""
        if not self.integer:
            return set()
        
        max_num = max(self.integer)
        a, b = 0, 1
        fib = {0, 1}
        
        while b <= max_num:
            a, b = b, a + b
            fib.add(b)
        
        return {n for n in self.integer if n in fib}


class WordSet(PySet):
    """specialized class for words only"""
    
    def __init__(self):
        super().__init__()
        self.vowels = set('aeiouAEIOU')
    
    def count_vowels(self, word):
        """count vowels in word"""
        return sum(1 for c in word if c in self.vowels)
    
    def count_consonants(self, word):
        """count consonants in word"""
        return sum(1 for c in word if c.isalpha() and c not in self.vowels)
    
    def get_by_vowel_count(self, count):
        """get words with specific vowel count"""
        return {w for w in self.words if self.count_vowels(w) == count}
    
    def get_by_consonant_count(self, count):
        """get words with specific consonant count"""
        return {w for w in self.words if self.count_consonants(w) == count}
    
    def sort_by_length(self):
        """sort words by length"""
        return sorted(self.words, key=len)
    
    def sort_alphabetically(self):
        """sort words alphabetically"""
        return sorted(self.words, key=str.lower)
    
    def get_anagrams(self, word):
        """find anagrams of word"""
        sorted_word = ''.join(sorted(word.lower()))
        return {w for w in self.words 
                if ''.join(sorted(w.lower())) == sorted_word 
                and w.lower() != word.lower()}
    
    def get_common_words(self, other_set):
        """get words common with another set"""
        return set(self.words) & set(other_set.words)
    
    def get_unique_words(self, other_set):
        """get words unique to this set"""
        return set(self.words) - set(other_set.words)
