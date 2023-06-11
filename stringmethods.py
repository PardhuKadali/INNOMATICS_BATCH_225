#Prepared by ASSAN,PARDHU,RUTHVI & SWETHA TEAMS
class stringm:
    def __init__(self):
        pass
    #upper
    def Upper(self,word):
        result = ""
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)
            else:
                result += char
        return result
    
    #lower
    def Lower(self,word):
        result = ""
        for char in word:
            if ord('A') <= ord(char) <= ord('Z'):
                result += chr(ord(char) + 32)
            else:
                result += char
        return result
    
    #swapcase
    def Swapcase(self,word):
        result = ""
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)
            elif ord('A') <= ord(char) <= ord('Z'):
                result += chr(ord(char) + 32)
            else:
                result += char
        return result
    
    #capitalize
    def Capitaliz(self,word):
        first_letter = word[0]
        second_letter =word[1::]
        if 'a' <= first_letter <= 'z':
            first_letter = chr(ord(first_letter) - 32)
        return first_letter + second_letter
    
    #Title
    def Title(self,word):
        result = ""
        text = True
        for char in word:
            if text and ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)
                text = False
            elif char in [' ', '\t', '\n']:
                result += char
                text = True
            else:
                result += char.lower()
        return result
 
    #count
    def s_count(self,word,find_to):
        count = 0
        sub_len = len(find_to)
        str_len = len(word)
        for i in range(str_len - sub_len + 1):
            if word[i:i+sub_len] == find_to:
                count += 1
        return count
    
    #casefold
    def Casefold(self,word):
        casefolded_string = ''
        for char in word:
            if 'A' <= char <= 'Z':
                 # Convert uppercase letter to lowercase
                char = chr(ord(char) + 32)
            casefolded_string += char
        return casefolded_string
    
    #center
    def Center(self,word,wdt,fillin):
        if wdt <= len(word):
            return word
        pad = wdt - len(word)
        lp = pad// 2
        rp = pad - lp
        return fillin * lp + word + fillin * rp
    
    
    #startswith
    def Startw(self,word,pf):
        pfl = len(pf)
        sl = len(word)
        if pfl > sl:
            return False
        return word[:pfl] == pf
    
    #endswith
    def Endsw(self,word,sf):
        slen = len(sf)
        len_wrd = len(word)
        if slen > len_wrd:
            return False
        return word[len_wrd - slen:] == sf
    
    #expandtab
    def Exptab(self,word,tab_size):
        expanded_string = ''

        for char in word:
            if char == '\t':
                spaces_to_insert = tab_size - (len(expanded_string) % tab_size)
                expanded_string += ' ' * spaces_to_insert
            else:
                expanded_string += char

        return expanded_string
    
    #find
    def s_find(self,word,s_string):
        main_len = len(word)
        sub_len = len(s_string)

        for i in range(main_len - sub_len + 1):
            found = True
            for j in range(sub_len):
                if word[i+j] != s_string[j]:
                    found = False
                    break
            if found:
                return i
        return -1
    
    #index
    def Index(self,word,subs:int):
        for i in range(len(word) - len(subs) + 1):
            if word[i:i+len(subs)] == subs:
                return i
        raise ValueError('substring not found')
        
        
    #isalnum
    def Isaln(self,word):
        for ele in word:        
            if not (65 <= ord(ele) <= 90 or 97 <= ord(ele) <= 122 or 48 <= ord(ele) <= 57):
                return False
        return True
    
    # isascii
    def Isascii(self,word):
        for ele in word:
            if ord(ele) > 127:
                return False
        return True
    
    #isalpha
    def Isalpha(self,word):
        for ele in word:
            if not (65 <= ord(ele) <= 90 or 97 <= ord(ele) <= 122):
                return False
        return True

    #isdigit
    def s_isdigit(self,word):
        for ele in word:
            if not (48 <= ord(ele) <= 57):
                return False
        return True
    
    
    #islower
    def s_islower(self,word):
        for ele in word:
            if not (97 <= ord(ele) <= 122):
                return False
        return True
    
    #isupper
    def s_isupper(self,word):
        for ele in word:
            if not (65 <= ord(ele) <= 90):
                return False
        return True
    
    # isnumeric
    def s_isnumaric(self,word):
        for ele in word:
            if not (48 <= ord(ele) <= 57):
                return False
        return True
    
    #join
    def Join(self,word,sep):
        result = ""
        for i in range(len(word)):
            result += word[i]
            if i != len(word) - 1:
                result += sep
        return result
    
    #lstrip
    def Lstrip(self,word):
        index = 0
        while index < len(word) and word[index].isspace():
            index += 1
        return word[index:]
    
    #partition
    def Partition(self,word,sep):
        first = ""
        middle = ""
        last = ""
        index = 0
        while index < len(word):
            if word[index:index+len(sep)] == sep:
                middle = sep
                last = word[index+len(sep):]
                break
            else:
                first += word[index]
                index += 1
        if middle == "":
            return (word, "", "")
        else:
            return (first, middle, last)
        
        
    #istitle
    def Istitle(self,word):
        previous_char_is_space = True
        is_title = False

        for char in word:
            if char != ' ':
                if previous_char_is_space:
                    if 'A' <= char <= 'Z':
                        is_title = True
                    else:
                        is_title = False
                        break
                    previous_char_is_space = False
            else:
                previous_char_is_space = True
        return is_title
    
    #removeprefix
    def Removepref(self,word,prefix):
        if word[:len(prefix)] == prefix:
            return word[len(prefix):]
        else:
            return word
    
    #removesufex
    def Removesuf(self,word,suffix):
        if word.endswith(suffix):
            return word[:-len(suffix)]
        else:
            return word
        
    #replace
    def Replace(self,word,old,new):
        index = 0
        while index < len(word):
            if word[index:index+len(old)] == old:
                word = word[:index] + new + word[index+len(old):]
                index += len(new)
            else:
                index += 1
        return word
    
    #rfind
    def Rfind(self,word,sub):
        start=None
        end=None
        if start is None:
            start = len(word) - 1
        if end is None:
            end = -1
        index = start
        while index >= end:
            if word[index:index+len(sub)] == sub:
                return index
            index -= 1
        return -1
    
    
    #rindex
    def Rindex(self,word,sub):
        main_len = len(word)
        sub_len = len(sub)

        for i in range(main_len - sub_len, -1, -1):
            found = True
            for j in range(sub_len):
                if word[i+j] != sub[j]:
                    found = False
                    break
            if found:
                return i

        return -1
    
    #rjust
    def Rjust(self,word,width):
        fillchar=' '
        if len(word) >= width:
            return word
        fill = fillchar * (width - len(word))
        return fill + word
    
    #rpartition
    def Rpartition(self,word,sep):
        separator_index = -1

        for i in range(len(word) - 1, -1, -1):
            if word[i] == sep:
                separator_index = i
                break

        if separator_index == -1:
            return ('', '', word)
        else:
            prefix = word[:separator_index]
            suffix = word[separator_index + 1:]
            return (prefix, sep, suffix)
        
        
    #rsplit
    def Rsplit(self,word, sep, maxsplit=-1):
        words = []
        count = 0

        for i in range(len(word)  -1, -1, 1):
            if word[i] == sep:
                words.append(word[i+1:][::1])
                count += 1
                if maxsplit != -1 and count >= maxsplit:
                    break

        if count == 0:
            words.append(word[::1])

        return words[::1]
    
    #rstrip
    def Rstrip(self,word):
        chars=None
        if chars is None:
            chars = ' \t\n\r\f\v'
        index = len(word) - 1
        while index >= 0:
            if word[index] not in chars:
                break
            index -= 1
        return word[:index+1]
    
    #split
    def Split(self,word,sep,maxsplit):
        words = []
        count = 0
        scn = ''

        for char in word:
            if char == sep:
                words.append(scn)
                scn = ''
                count += 1
                if maxsplit != -1 and count >= maxsplit:
                    break
            else:
                scn += char

        if scn:
            words.append(scn)

        return words
    
    
    #splitlines
    def Splitlines(self,word):
        keepends=False
        lines = []
        start = 0
        for i in range(len(word)):
            if word[i] in ('\n', '\r'):
                lines.append(word[start:i])
                if keepends:
                    lines[-1] += word[i]
                if i+1 < len(word) and word[i] != word[i+1] and word[i+1] in ('\n', '\r'):
                    i += 1
                start = i + 1
        lines.append(word[start:])
        return lines
    
    
    #strip
    def Strip(self,word,charac):
        if charac is None:
            characters = ' \t\n\r'

        start = 0
        end = len(word) - 1

        while start <= end and word[start] in charac:
            start += 1

        while end >= start and word[end] in charac:
            end -= 1

        return word[start:end+1]
    
    
    #lstrip
    def Lstrip(self,word,ch):
        if ch is None:
            ch = ' \t\n\r'

        start = 0

        while start < len(word) and word[start] in ch:
            start += 1

        return word[start:]

        
            

    
    
    
    
my_str = stringm()
my_str.Upper('Ruthvi')
