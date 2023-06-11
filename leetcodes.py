class Leetcode:
    def __init__(self):
        pass
    
    # 1456. Maximum Number of Vowels in a Substring of Given Length
    def lc_1456(self, s: str, k: int):
        """
        Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
        Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
        Example 1:
        Input: s = "abciiidef", k = 3
        Output: 3
        Explanation: The substring "iii" contains 3 vowel letters.
        -------------------------> Ruthvi Gurram
        """
        
        vowels = set('aeiou')
        max_count = 0
        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1

        max_count = current_count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            max_count = max(max_count, current_count)

        return max_count
    
    
    
    
    
    
    # 2103. Rings and Rods
    def lc_2103(self, rnr: str):
        """
        There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

        You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

        The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
        The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
        For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

        Return the number of rods that have all three colors of rings on them.

        Example 1:


        Input: rings = "B0B6G0R6R0R6G9"
        Output: 1
        Explanation:
        - The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
        - The rod labeled 6 holds 3 rings, but it only has red and blue.
        - The rod labeled 9 holds only a green ring.
        Thus, the number of rods with all three colors is 1.
        ------------------------>  Ruthvi Gurram
        """
        n = len(rnr) // 2
        rod_colors = {i: {'R': 0, 'G': 0, 'B': 0} for i in range(10)}
        for i in range(n):
            color = rnr[2 * i]
            rod = int(rnr[2 * i + 1])
            rod_colors[rod][color] += 1
        count = 0
        for i in range(10):
            if all(rod_colors[i][color] > 0 for color in ['R', 'G', 'B']):
                count += 1
        return count
    
    
    
    
    # 1920.Build Array from Permutation
    def lc_1920(self, nums: list):
        """
        Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

         A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
         Example 1:

         Input: nums = [0,2,1,5,3,4]
         Output: [0,1,2,4,5,3]
        Explanation: The array ans is built as follows:
         ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
         = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
        = [0,1,2,4,5,3]
        ---------------------> Ruthvi Gurram
        """
        n = len(nums)
        arr_lst = [0] * n
        for i in range(n):
            arr_lst[i] = nums[nums[i]]
        return arr_lst
    
    
    
    
    
    # 2496. Maximum Value of a String in an Array
    def lc_2496(self, strn):
        """
        The value of an alphanumeric string can be defined as:

        The numeric representation of the string in base 10, if it comprises of digits only.
        The length of the string, otherwise.
        Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

        Example 1:

         Input: strs = ["alic3","bob","3","4","00000"]
         Output: 5
         Explanation:
           - "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
        - "bob" consists only of letters, so its value is also its length, i.e. 3.
        - "3" consists only of digits, so its value is its numeric equivalent,  .e. 3.
         - "4" also consists only of digits, so its value is 4.
         - "00000" consists only of digits, so its value is 0.
           Hence, the maximum value is 5, of "alic3".
            ---------------------> Ruthvi Gurram
        """

        strs = list(strn)
        values = []
        for s in strs:
            if s.isdigit():
                values.append(int(s))
            else:
                values.append(len(s))
        return max(values)
    
    
    
    
    
    # 1844. Replace All Digits with Characters
    def lc_1844(self, s):
        """
        You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

        There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

         For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
         For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

         Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

        Example 1:

        Input: s = "a1c1e1"
        Output: "abcdef"
        Explanation: The digits are replaced as follows:
        - s[1] -> shift('a',1) = 'b'
        - s[3] -> shift('c',1) = 'd'
        - s[5] -> shift('e',1) = 'f'
        ----------------------------->  Ruthvi Gurram

        """
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)

        s = list(s)
        n = len(s)
        for i in range(1, n, 2):
            s[i] = shift(s[i - 1], int(s[i]))
        return ''.join(s)
    
    
    
    
    # 2574. Left and Right Sum Differences
    def lc_2574(self, nums):
        """
        Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

        answer.length == nums.length.
        answer[i] = |leftSum[i] - rightSum[i]|.
        Where:

        leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
         rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
         Return the array answer.

         Example 1:

        Input: nums = [10,4,8,3]
        Output: [15,1,11,22]
        Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
        The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
        ----------------------> Akash Viswas

        """
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]
        answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
        return answer
    
    
    
    
    # 2000. Reverse Prefix of Word
    def lc_2000(self, word, ch):
        """
        Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

        For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
        Return the resulting string.

        Example 1:

        Input: word = "abcdefd", ch = "d"
        Output: "dcbaefd"
         Explanation: The first occurrence of "d" is at index 3.
         Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
        ---------------------------------> Ruthvi Gurram
        """
        if ch not in word:
            return word

        ch_index = word.index(ch)
        segment = word[:ch_index + 1]
        reversed_segment = segment[::-1]
        rest_of_word = word[ch_index + 1:]

        return reversed_segment + rest_of_word
    
    
    
    
    
    # 1672. Richest Customer Wealth
    def lc_1672(self,acc):

        """
        You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

        A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


        Example 1:

        Input: accounts = [[1,2,3],[3,2,1]]
        Output: 6
        Explanation:
        1st customer has wealth = 1 + 2 + 3 = 6
        2nd customer has wealth = 3 + 2 + 1 = 6
        Both customers are considered the richest with a wealth of 6 each, so return 6.
      
        ------------------------> Akash Viswas
        """
        max_wealth = 0
        for row in acc:
            current_wealth = 0
            for amount in row:
                current_wealth += amount
                if current_wealth > max_wealth:
                    max_wealth = current_wealth
        return max_wealth
    
    
    
    
    def lc_2114(self, sentences):
        """
        A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

        You are given an array of strings sentences, where each sentences[i] represents a single sentence.

        Return the maximum number of words that appear in a single sentence.

        Example 1:

        Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
        Output: 6
        Explanation:
        - The first sentence, "alice and bob love leetcode", has 5 words in total.
        - The second sentence, "i think so too", has 4 words in total.
        - The third sentence, "this is great thanks very much", has 6 words in total.
        Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
        -------------------->  Akash Viswas
        """

        max_words = 0
        for sentence in sentences:
            words = sentence.split()
            num_words = len(words)
            if num_words > max_words:
                max_words = num_words

        return max_words
    
    
    
    
    # 1614.Maximum Nesting Depth of the Parentheses
    def lc_1614(self, s):

        """
        A string is a valid parentheses string (denoted VPS) if it meets one of the following:

        It is an empty string "", or a single character not equal to "(" or ")",
        It can be written as AB (A concatenated with B), where A and B are VPS's, or
        It can be written as (A), where A is a VPS.
        We can similarly define the nesting depth depth(S) of any VPS S as follows:

        depth("") = 0
        depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
        depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
        depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
        For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

        Given a VPS represented as string s, return the nesting depth of s.
        ---------------------------> Sarath


        Example 1:

        Input: s = "(1+(2*3)+((8)/4))+1"
        Output: 3
        Explanation: Digit 8 is inside of 3 nested parentheses in the string.

        """

        max_depth = 0
        current_depth = 0
        for c in s:
            if c == "(":
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif c == ")":
                current_depth -= 1
        return max_depth
    #2651 Calculate Delayed Arrival Time for a train
    def lc_2651(self, arrivalTime: int, delayedTime: int) -> str:

        """
        You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.

         Return the time when the train will arrive at the station.

        Note that the time in this problem is in 24-hours format.



        Example 1:

        Input: arrivalTime = 15, delayedTime = 5
        Output: 20
        Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
        -------------------------------- > Ruthvi Gurram

        """

        # convert arrival time and delay time to minutes
        arrival_minutes = arrivalTime // 100 * 60 + arrivalTime % 100
        delay_minutes = delayedTime * 60

        # calculate the new arrival time in minutes
        new_arrival_minutes = (arrival_minutes + delay_minutes) % (24 * 60)

        # convert the new arrival time to hours and minutes
        new_arrival_hours = new_arrival_minutes // 60
        new_arrival_minutes = new_arrival_minutes % 60
        return '{:02d}:{:02d}'.format(new_arrival_hours, new_arrival_minutes)
    
    
    
    
    
    # 1281. Subtract the Product and Sum of Digits of an Integer
    def lc_1281(self, n):
        """
        Given an integer number n, return the difference between the product of its digits and the sum of its digits.


        Example 1:

        Input: n = 234
        Output: 15
        Explanation:
        Product of digits = 2 * 3 * 4 = 24
        Sum of digits = 2 + 3 + 4 = 9
        Result = 24 - 9 = 15
        ---------------------> Sarath

        """
        product = 1
        sum = 0
        while n > 0:
            digit = n % 10
            product *= digit
            sum += digit
            n //= 10

        return (product - sum)
    
    #1967. Number of Strings That Appear as Substrings in Word
    def lc_1967(self,patterns:str , words:str):
        """
        Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

        A substring is a contiguous sequence of characters within a string.

        Example 1:

        Input: patterns = ["a","abc","bc","d"], word = "abc"
        Output: 3
        Explanation:
        - "a" appears as a substring in "abc".
        - "abc" appears as a substring in "abc".
        - "bc" appears as a substring in "abc".
        - "d" does not appear as a substring in "abc".
        3 of the strings in patterns appear as a substring in word.
        --------------------> Sarath 
        """
        count = 0
        for pattern in patterns:
            if pattern in words:
                count += 1
        return count
    
    
    
    
    #1389. Create Target Array in the Given Order
    def lc_1389(self,nums, index):
        """
        Given two arrays of integers nums and index. Your task is to create target array under the following rules:

         Initially target array is empty.
         From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
         Repeat the previous step until there are no elements to read in nums and index.
         Return the target array.

         It is guaranteed that the insertion operations will be valid.

         Example 1:

         Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
         Output: [0,4,1,3,2]
         Explanation:
         nums       index     target
         0            0        [0]
         1            1        [0,1]
         2            2        [0,1,2]
         3            2        [0,1,3,2]
         4            1        [0,4,1,3,2]

        ----------------------------> Sarath
        """
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
    
    
    #1880. Check if Word Equals Summation of Two Words
    @staticmethod
    def get_num_value(word):
        
        
        """
        The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

        The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.

         For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
         You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

         Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

         Example 1:

         Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
         Output: true
         Explanation:
         The numerical value of firstWord is "acb" -> "021" -> 21.
         The numerical value of secondWord is "cba" -> "210" -> 210.
         The numerical value of targetWord is "cdb" -> "231" -> 231.
         We return true because 21 + 210 == 231.

        ---------------------------> Sirisha
        """
        
        numerical_value = ""
        for letter in word:
            numerical_value += str(ord(letter) - 97)
        return int(numerical_value)

    def lc_1880(self, firstWord, secondWord, targetWord):
        first_word_num_value = Leetcode.get_num_value(firstWord)
        second_word_num_value = Leetcode.get_num_value(secondWord)
        target_word_num_value = Leetcode.get_num_value(targetWord)

        return first_word_num_value + second_word_num_value == target_word_num_value
    
    
    
    
    #1342.Number of Steps to Reduce a Number to Zero
    def lc_1342(self,num: int):
        """
        Given an integer num, return the number of steps to reduce it to zero.

        In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

        Example 1:

        Input: num = 14
        Output: 6
        Explanation: 
        Step 1) 14 is even; divide by 2 and obtain 7. 
        Step 2) 7 is odd; subtract 1 and obtain 6.
        Step 3) 6 is even; divide by 2 and obtain 3. 
        Step 4) 3 is odd; subtract 1 and obtain 2. 
         Step 5) 2 is even; divide by 2 and obtain 1. 
        Step 6) 1 is odd; subtract 1 and obtain 0.

        ------------------------> Sirisha
        """
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            steps += 1
        return steps
      
    
    
    #728. Self Dividing Numbers
    @staticmethod
    def is_self_dividing(num):
        """
        A self-dividing number is a number that is divisible by every digit it contains.
        For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
        A self-dividing number is not allowed to contain the digit zero.
        Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
        --------------------> Sirisha
        """
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True

    def lc_728(self, left, right):
        result = []
        for num in range(left, right + 1):
            if Leetcode.is_self_dividing(num):
                result.append(num)
        return result
    
    
    
    
    
    #2520.Count the Digits That Divide a Number
    def lc_2520(self,num):
        """
        Given an integer num, return the number of digits in num that divide num.

        An integer val divides nums if nums % val == 0.

        Example 1:

        Input: num = 7
        Output: 1
        Explanation: 7 divides itself, hence the answer is 1.
        -------------------------> Akash Viswas
        """
        num_str = str(num)
        count = 0
    
        # Iterate through each digit in num
        for digit in num_str:
            
        # Convert digit back to an integer and check if it divides num
            if int(digit) != 0 and num % int(digit) == 0:
                count += 1
    
        return count
    
    
    
    #1304 Find N Unique Integers Sum up to Zero
    def lc_1304(self,n):
        """
        Given an integer n, return any array containing n unique integers such that they add up to 0.

        Example 1:

        Input: n = 5
        Output: [-7,-1,1,3,4]
        Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

        ----------------------> Akash Viswas
        """
    
        if n % 2 == 1:
            arr = [i for i in range(-(n-1)//2, (n-1)//2 + 1)]
            arr.append(0)
            return arr
        else:
            return [i for i in range(-n//2, 0)] + [i for i in range(1, n//2 + 1)]
        
           
    #1876. Substrings of Size Three with Distinct Characters
    @staticmethod
    def is_good_substring(substr):
        return len(set(substr)) == len(substr)

    def lc_1876(self, s):
        
        """  
        A string is good if there are no repeated characters.

        Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

        Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
 
        A substring is a contiguous sequence of characters in a string.

        Example 1:

        Input: s = "xyzzaz"
        Output: 1
        Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
         The only good substring of length 3 is "xyz".
         --------------------> Akash Viswas
          
        """
    
        count = 0
        for i in range(len(s) - 2):
            substr = s[i:i+3]
            if Leetcode.is_good_substring(substr):
                count += 1
        return count
    
  
    
    
    #1588. Sum of All Odd Length Subarrays
    def lc_1588(self,arr):
        """
        Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

        A subarray is a contiguous subsequence of the array.

        Example 1:

        Input: arr = [1,4,2,5,3]
        Output: 58 
        Explanation: The odd-length subarrays of arr and their sums are:
        [1] = 1
        [4] = 4
        [2] = 2
        [5] = 5
        [3] = 3
        [1,4,2] = 7
        [4,2,5] = 11
        [2,5,3] = 10
        [1,4,2,5,3] = 15
        If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
        ------------------------> Akash Viswas
    
        """
        total_sum = 0
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                if (j-i+1) % 2 != 0:
                    total_sum += sum(arr[i:j+1])
        return total_sum
    
    
    #1085 Sum of Digits in the Minimum Number
    def lc_1085(self,lst):
    
        """
        Question
        Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
        Return 0 if S is odd, otherwise return 1.

        Example 1:
        Input: [34,23,1,24,75,33,54,8]
        Output: 0
        Explanation: The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
        -------------------------> Akash Viswas
    
        """
        # Find the minimum number in the list
        min_num = min(lst)
    
        # Convert the minimum number to a string and sum the digits
        sum_digits = sum([int(digit) for digit in str(min_num)])
    
        return sum_digits
    
    
    
    #1684 Count the Number of Consistent Strings
    def lc_1684(self,allowed, words):
        """
        You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

        Return the number of consistent strings in the array words.

 

        Example 1:

        Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
        Output: 2
        Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

        ----------------------> Ruthvi Gurram
        """
    
        allowedchars = set(allowed)
        consistentcount = 0

        for ele in words:
            if all(char in allowedchars for char in ele):
                consistentcount += 1
        return consistentcount 
    
    # 557. Reverse Words in a String III
    def lc_557(self,s):
        """
        Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

        Example 1:

        Input: s = "Let's take LeetCode contest"
         Output: "s'teL ekat edoCteeL tsetnoc"
        """
        words = s.split(" ")
        reversed_words = []
        for ele in words:
            reversed_words.append(ele[::-1])
        return " ".join(reversed_words)
