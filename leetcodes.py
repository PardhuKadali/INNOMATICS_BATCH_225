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
    
    #1742: Maximum Number of Balls in a Box
    @staticmethod
    def sum_of_digits(digit,sum=0):
        sum=0
        while digit:
            sum+=digit%10
            digit=digit//10
        return sum
    def lc_1742(self,lowerLimit,highLimit):
        
        '''
        You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive 
        (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
        Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. 
        For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 
        10 will be put in the box number 1 + 0 = 1.
        Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

        Example 1:
        Input: lowLimit = 1, highLimit = 10
        Output: 2
        Explanation:
        Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
        Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
        Box 1 has the most number of balls with 2 balls.
             --------------------------------------------------- Swetha
        '''
        my_dict={}
        for i in range(lowerLimit,highLimit+1):
            sum=sum_of_digits(i)
            if sum in my_dict:
                my_dict[sum]+=1
            else:
                my_dict[sum]=1
        return max(my_dict.values())
    
    #1929: Concatenation of Array
    def lc_1929(self,nums:list[int]):

        '''
        Given an integer array nums of length n, you want to create an array ans of length 2n 
        where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
        Specifically, ans is the concatenation of two nums arrays.
        Return the array ans.

        Example 1:

        Input: nums = [1,2,1]
        Output: [1,2,1,1,2,1]
        Explanation: The array ans is formed as follows:
        - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
        - ans = [1,2,1,1,2,1]
          ------------------------------------------------------------Swetha
        '''

        return nums*2

    
    #762: Prime Number of Set Bits in Binary Representation
    @staticmethod
    def is_prime(n):

        if n<2:
            return False
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        return True

    #left=int(input())
    #right=int(input())

    def lc_762(self):
        
        '''
        Given two integers left and right, return the count of numbers in the inclusive range [left, right] 
        having a prime number of set bits in their binary representation.
        Recall that the number of set bits an integer has is the number of 1's present when written in binary.
        For example, 21 written in binary is 10101, which has 3 set bits. 

        Example 1:
        Input: left = 6, right = 10
        Output: 4
        Explanation:
        6  -> 110 (2 set bits, 2 is prime)
        7  -> 111 (3 set bits, 3 is prime)
        8  -> 1000 (1 set bit, 1 is not prime)
        9  -> 1001 (2 set bits, 2 is prime)
        10 -> 1010 (2 set bits, 2 is prime)
        4 numbers have a prime number of set bits.
                        ----------------------------------Swetha
        '''
        count=0
        for i in range(6,10+1):
            x=(str(bin(i))[2:])
            if is_prime(x.count('1')):
                count+=1
        return count
    
    #1470: Shuffle the Array
    def lc_1470(self, nums:list[int], n):
        
        '''
        Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
        Return the array in the form [x1,y1,x2,y2,...,xn,yn]. 
        Example 1:
        Input: nums = [2,5,1,3,4,7], n = 3
        Output: [2,3,5,4,1,7] 
        Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
          ----------------------------------------------- Swetha
        '''
        
        x=nums[0:n]
        y=nums[n:]
        new_arr=[]
        for i in range(n):
            new_arr.append(x[i])
            new_arr.append(y[i])
        return new_arr
    
    #509: Fibonacci Number    
    def lc_509(self, n: int) -> int:
                
        '''
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
        such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
        Given n, calculate F(n).
        Example 1:
        Input: n = 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
          -------------------------------------------------- Swetha
        '''
        
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            
            return self.lc_509(n-1)+self.lc_509(n-2)
        

    #2235: Add Two Integers
    def lc_2235(self, num1: int, num2: int):
            
        '''
        Given two integers num1 and num2, return the sum of the two integers.
        Example 1:
        Input: num1 = 12, num2 = 5
        Output: 17
        Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
        --------------------------------------------------- Sai
        '''
        c=num1+num2
        return c
    
    
    #1603: Design Parking System
    @staticmethod
    def addCar(carType:int,ParkingSystem)->bool:
        mapping = {1: "big",2:"medium",3: "small"}
        
        if ParkingSystem[mapping[carType]]!=0:
            ParkingSystem[mapping[carType]]-=1
            return True
        return False
    def lc_1603(self,big:int,medium:int,small:int):
        '''
        Design a parking system for a parking lot. 
        The parking lot has three kinds of parking spaces: big, medium, and small, 
        with a fixed number of slots for each size.

        Implement the ParkingSystem class:

        ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
        The number of slots for each parking space are given as part of the constructor.
        bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get 
        into the parking lot. 
        carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. 
        A car can only park in a parking space of its carType. 
        If there is no space available, return false, else park the car in that size space and return true.
 

        Example 1:

        Input
        ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
        [[1, 1, 0], [1], [2], [3], [1]]
        Output
        [null, true, true, false, false]

        Explanation
        ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
        parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
        parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
        parkingSystem.addCar(3); // return false because there is no available slot for a small car
        parkingSystem.addCar(1); // return false because there is no available slot for a big car. 
        It is already occupied.
        --------------------------------------------------- Sai
        '''
        l=[]
        ParkingSystem={'big':big,'medium':medium,'small':small}
        ac=self.addCar(1,ParkingSystem) 
        l.append(ac)
        ac=self.addCar(2,ParkingSystem) 
        l.append(ac)
        ac=self.addCar(3,ParkingSystem) 
        l.append(ac)
        ac=self.addCar(1,ParkingSystem) 
        l.append(ac)
        return l
    

    #1025: Divisor Game
    def lc_1025(self, n: int) -> bool:
        
        '''
        Alice and Bob take turns playing a game, with Alice starting first.
        Initially, there is a number n on the chalkboard. 
        On each player's turn, that player makes a move consisting of:
        Choosing any x with 0 < x < n and n % x == 0.
        Replacing the number n on the chalkboard with n - x.
        Also, if a player cannot make a move, they lose the game.
        Return true if and only if Alice wins the game, assuming both players play optimally.

        Example 1:
        Input: n = 2
        Output: true
        Explanation: Alice chooses 1, and Bob has no more moves.
        --------------------------------------------------- Sai
        '''
        if (n%2==0):
            return True
        else:
            return False

    
    #1678:  Goal Parser Interpretation
    def lc_1678(self,command):

        '''
        You own a Goal Parser that can interpret a string command. 
        The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
        The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
        The interpreted strings are then concatenated in the original order.
        Given the string command, return the Goal Parser's interpretation of command.

        Example 1:
        Input: command = "G()(al)"
        Output: "Goal"
        Explanation: The Goal Parser interprets the command as follows:
        G -> G
        () -> o
        (al) -> al
        The final concatenated result is "Goal".
        --------------------------------------------------- Sai
        '''

        interp = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                interp += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                interp += 'o'
                i += 2
            elif command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                interp += 'al'
                i += 4
            else:
                # Invalid command, handle error or raise exception
                return "Invalid command"
        return interp 
    

    #2648: Generate Fibonacci Sequence
    @staticmethod
    def Fib(n):
        if n <= 1:
            return n
        else:
            return (Fib(n - 1) + Fib(n - 2)) # function calling itself(recursion)

    def lc_2648(self,n):
   
        '''
        Write a generator function that returns a generator object which yields the fibonacci sequence.
        The fibonacci sequence is defined by the relation Xn = Xn-1 + Xn-2.
        The first few numbers of the series are 0, 1, 1, 2, 3, 5, 8, 13. 

        Example 1:

        Input: callCount = 5
        Output: [0,1,1,2,3]
        Explanation:
        const gen = fibGenerator();
        gen.next().value; // 0
        gen.next().value; // 1
        gen.next().value; // 1
        gen.next().value; // 2
        gen.next().value; // 3
        --------------------------------------------------- Sai
        '''
    
        l=[]
        for i in range(n):
            l.append(Fib(i))
        return l

    #1374:Generate a String With Characters That Have Odd Counts
    def lc_1374(self,n):

        '''
        Given an integer n, return a string with n characters 
        such that each character in such string occurs an odd number of times.
        The returned string must contain only lowercase English letters. 
        If there are multiples valid strings, return any of them.  

        Example 1:

        Input: n = 4
        Output: "pppz"
        Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. 
        Note that there are many other valid strings such as "ohhh" and "love".
        --------------------------------------------------- Manoj
        '''

        if n % 2 == 0:
            return 'a' * (n-1) + 'b'
        else:
            return 'a' * n


    #1313: Decompress Run-Length Encoded List
    def lc_1313(self,n):

        '''
        We are given a list nums of integers representing a list compressed with run-length encoding.
        Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
        For each such pair, there are freq elements with value val concatenated in a sublist. 
        Concatenate all the sublists from left to right to generate the decompressed list.
        Return the decompressed list.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [2,4,4,4]
        Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
        The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
        At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
        --------------------------------------------------- Manoj
        '''

        x=[]
        for i in range(0,len(n),2):
            x=x+[n[i+1]]*n[i]
        return x


    #2652: Sum Multiples
    def lc_2652(self,a,n):

        '''
        Given a positive integer n, 
        find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
        Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

        Example 1:
        Input: n = 7
        Output: 21
        Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. 
        The sum of these numbers is 21.
        --------------------------------------------------- Manoj
        '''

        sum=0
        for num in range(a,n+1):
            if num%3==0 or num%5==0 or num%7==0:
                sum+=num
        return sum

    
    
    #1656: Design an Ordered Stream
    
    '''
    There is a stream of n (idKey, value) pairs arriving in an arbitrary order, 
    where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

    Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values 
    after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

    Implement the OrderedStream class:
    OrderedStream(int n) Constructs the stream to take n values.
    String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, 
    then returns the largest possible chunk of currently inserted values that appear next in the order.
    Input
    ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
    Output
    [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

    Explanation
    // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
    OrderedStream os = new OrderedStream(5);
    os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
    os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
    os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
    os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
    // Concatentating all the chunks returned:
    // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
    // The resulting order is the same as the order above.
    --------------------------------------------------------------- Manoj
    '''
    @staticmethod
    def insert(idKey: int, value: str,stream,ptr) :
        #print(idKey)
        #print(value)
        idKey -= 1  # Adjust the ID to match the array index
        #print('changed id : ',idKey)
        #print(value)
        stream[idKey] = value  # Store the value in the array

        if idKey == ptr:
            # If the inserted ID is the next expected ID, find the largest possible chunk
            chunk = []
            while ptr < len(stream) and stream[ptr]:
                chunk.append(stream[ptr])
                ptr += 1
                #print(chunk)
            return chunk,ptr
        else:
            return []

    def lc_1656(self,z):
        stream = [None] * z[0][0]  # Initialize an array to store the values
        ptr = 0  # Pointer to keep track of the next expected ID
        l=[]
        for y in range(1,len(z)):
            i=self.insert(z[y][0],z[y][1],stream,ptr)
            if len(i)==0:
                l.append(i)
            else:
                ptr=i[1]
                l.append(i[0])
        return l
    
    
    
    #2418: Sort the People
    def lc_2418(self,names,heights):
        '''
        You are given an array of strings names, and an array heights that consists of distinct positive integers. 
        Both arrays are of length n.
        For each index i, names[i] and heights[i] denote the name and height of the ith person.
        Return names sorted in descending order by the people's heights.

        Example 1:

        Input: names = ["Mary","John","Emma"], heights = [180,165,170]
        Output: ["Mary","Emma","John"]
        Explanation: Mary is the tallest, followed by Emma and John.
        --------------------------------------------------- Manoj
        '''
        final_list=[]
        sorted_heights=sorted(heights,reverse=True)
        for i in sorted_heights:
            pos=heights.index(i)
            k=names[pos]
            final_list.append(k)
        return final_list
    
    
    
    #2194: Cells in a Range on an Excel Sheet
    def lc_2194(self,s):

        '''
        A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:

        <col> denotes the column number c of the cell. It is represented by alphabetical letters.
        For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
        <row> is the row number r of the cell. The rth row is represented by the integer r.
        You are given a string s in the format "<col1><row1>:<col2><row2>", 
        where <col1> represents the column c1, <row1> represents the row r1, 
        <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

        Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. 
        The cells should be represented as strings in the format mentioned above and 
        be sorted in non-decreasing order first by columns and then by rows.
        
        Example 1:
        Input: s = "K1:L2"
        Output: ["K1","K2","L1","L2"]
        Explanation:
        The above diagram shows the cells which should be present in the list.
        The red arrows denote the order in which the cells should be presented.
        --------------------------------------------------- Mouni
        '''

        colon_idx = s.index(':')
        col1 = s[0]
        col2 = s[colon_idx + 1]

        row1 = int(s[1:colon_idx])
        row2 = int(s[colon_idx + 2:])

        cells = []
        for col in range(ord(col1), ord(col2) + 1):
            for row in range(row1, row2 + 1):
                cell = chr(col) + str(row)
                cells.append(cell)

        return sorted(cells)

    
    #1859:  Sorting the Sentence
    def lc_1859(self,l):
        '''
        A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
        Each word consists of lowercase and uppercase English letters.
        A sentence can be shuffled by appending the 1-indexed word position to each word 
        then rearranging the words in the sentence.
        For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
        Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

        Example 1:

        Input: s = "is2 sentence4 This1 a3"
        Output: "This is a sentence"
        Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
        --------------------------------------------------- Mouni
        '''

        s = l.split()
        n = len(s)
        res = [""] * n

        for i in s:
            k= int(i[-1])
            res[k - 1] = i[:-1]
        return " ".join(res)
    

    #1021: Remove Outermost Parenthesis
    def lc_1021(self,s):

        '''
        A valid parentheses string is either empty "", "(" + A + ")", or A + B, 
        where A and B are valid parentheses strings, 
        and + represents string concatenation.

        For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
        A valid parentheses string s is primitive if it is nonempty, and 
        there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

        Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, 
        where Pi are primitive valid parentheses strings.

        Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

        Example 1:

        Input: s = "(()())(())"
        Output: "()()()"
        Explanation: 
        The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
        After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
        --------------------------------------------------- Mouni
        '''

        result = []
        bal = 0

        for char in s:
            if char == '(':
                if bal > 0:
                    result.append(char)
                bal += 1
            elif char == ')':
                bal -= 1
                if bal > 0:
                    result.append(char)                                                                              

        return ''.join(result)
    

    #760: Find Anagram Mappings
    def lc_760(self,num1,num2):
        '''
        Given two lists Aand B, and B is an anagram of A. 
        B is an anagram of A means B is made by randomizing the order of the elements in A.

        We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

        These lists A and B may contain duplicates. If there are multiple answers, output any of them.

        For example, given

        A = [12, 28, 46, 32, 50]
        B = [50, 12, 32, 46, 28]
        We should return
        [1, 4, 3, 2, 0]
        as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 
        because the 1st element of A appears at B[4], and so on.
        --------------------------------------------------- Mouni
        '''
        lst=[]
        for i in num1:
            x=num2.index(i)
            lst.append(x)
        return lst


    #1688: Count of Matches in Tournament
    def lc_1688(self, n: int) -> int:
        '''
        You are given an integer n, the number of teams in a tournament that has strange rules:
        If the current number of teams is even, each team gets paired with another team. 
        A total of n / 2 matches are played, and n / 2 teams advance to the next round.
        If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. 
        A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
        Return the number of matches played in the tournament until a winner is decided.

        Example 1:

        Input: n = 7
        Output: 6
        Explanation: Details of the tournament: 
        - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
        - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
        - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
        Total number of matches = 3 + 2 + 1 = 6.
        --------------------------------------------------- Mouni
        '''
        
        i=n
        c=0
        while i!=1:
            if(i%2==0):
                c+=i//2
                i=i//2
            else:
                c+=(i-1)//2
                i=(i-1)//2 +1
        return c


    #2006: Count Number of Pairs With Absolute Difference K
    def lc_2006(self,arr, k):

        '''
        Given an integer array nums and an integer k, 
        return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
        The value of |x| is defined as:
        x if x >= 0.
        -x if x < 0.

        Example 1:
        Input: nums = [1,2,2,1], k = 1
        Output: 4
        Explanation: The pairs with an absolute difference of 1 are:
        - [1,2,2,1]
        - [1,2,2,1]
        - [1,2,2,1]
        - [1,2,2,1]
        --------------------------------------------------- Sonu
        '''
        n=len(arr)
        count = 0

        # Pick all elements one by one
        for i in range(0, n):

            # See if there is a pair of this picked element
            for j in range(i+1, n) :

                if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
                    count += 1

        return count


    
    #709: To Lower Case
    def lc_709(self,s):

        '''
        Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
        Example 1:
        Input: s = "Hello"
        Output: "hello"
        --------------------------------------------------- Sonu
        '''

        ns=''

        for i in range(len(s)):



            if(s[i] >= 'A' and s[i] <= 'Z'):

                ns= ns+chr((ord(s[i]) + 32))
            else:

                ns= ns + s[i]
        return(ns)
    
    
    #2283: Check if Number Has Equal Digit Count and Digit Value
    def lc_2283(self,num):

        '''
        You are given a 0-indexed string num of length n consisting of digits.
        Return true if for every index i in the range 0 <= i < n, 
        the digit i occurs num[i] times in num, otherwise return false.

        Example 1:
        Input: num = "1210"
        Output: true
        Explanation:
        num[0] = '1'. The digit 0 occurs once in num.
        num[1] = '2'. The digit 1 occurs twice in num.
        num[2] = '1'. The digit 2 occurs once in num.
        num[3] = '0'. The digit 3 occurs zero times in num.
        The condition holds true for every index in "1210", so return true.
        --------------------------------------------------- Sonu
        '''

        n = len(num)

        for i in range(n):
            digit_count = num.count(str(i))
            if digit_count != int(num[i]):
                return False

        return True
    

    #2315: Count Asterisks
    def lc_2315(self,s):

        '''
        You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. 
        In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
        Return the number of '*' in s, excluding the '*' between each pair of '|'.
        Note that each '|' will belong to exactly one pair.

        Example 1:
        Input: s = "l|*e*et|c**o|*de|"
        Output: 2
        Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
        The characters between the first and second '|' are excluded from the answer.
        Also, the characters between the third and fourth '|' are excluded from the answer.
        There are 2 asterisks considered. Therefore, we return 2.
        --------------------------------------------------- Sonu
        '''

        res=''
        j=s.split('|')
        data=j[::2]
        res=str(data)
        return res.count('*')
    
    #1160:  Find Words That Can Be Formed by Characters
    def lc_1160(self,words,chars):

        '''
        You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars (each character can only be used once).
        Return the sum of lengths of all good strings in words.

        Example 1:
        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
        --------------------------------------------------- Sonu
        '''
        result=0

        for i in words:
            count=0
            for j in i:
                if (i.count(j)>chars.count(j)):
                    count=1


            if count==0:

                result+=len(i)
        return result

    
