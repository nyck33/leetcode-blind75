'''
937. Reorder Data in Log Files
Attempted
Medium
Topics
Companies
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Constraints:

1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.
'''
class Solution:
    def sort_by_first_then_second(self, item):
        return item[0], item[1]

    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        '''
        1. iterate logs, first 4 letters are identifier,
        put them in dicts one for letters, a list for digits
        2 dicts {content_as_str: identifier} for letters
        {identifier: original str}
        2.  sort the letters dict with key contentStr then index into identifier dict to get the original str, construct the original string and place in an empty list of len(logs)
        extend list by digits list 
        '''
        # list of digit logs, list of compacted letter logs for sorting, {key:log} dict
        digit_logs, letter_log_contents, str_key_dict = self.make_letters_dicts(logs)

        #sort letter_log_contents (squished content key, id)
        #letter_log_contents.sort()
        #sorted_letter_log_contents = sorted(letter_log_contents, key=self.sort_by_first_then_second)
        letter_log_contents = sorted(letter_log_contents, key=lambda tup: (tup[0], tup[1]))

        print(f'letter_log_contents: {letter_log_contents}')

        # use the sorted list to index into str_key_dict, get the letter logs and make a final list
        final_list = ['' for x in range(len(logs))]
        count = 0

        for i in range(len(letter_log_contents)):
            curr_key_tup = letter_log_contents[i]
            str_key, id = curr_key_tup
            curr_log = str_key_dict[curr_key_tup]
            final_list[count] = curr_log
            count +=1
        
        # append the digits logs
        final_list = final_list[:count]
        return final_list + digit_logs
    
    def make_letters_dicts(self,logs):
        # init data structures
        digit_logs = ["" for x in range(len(logs))]
        dig_logs_count = 0

        #{stripped str lowered key: entire log}
        # can be indexed with sorted keys
        str_key_dict = {} 
        #{stripped id only: entire log}
        #orig_str_dict = {}

        # a list to hold all letter logs lowered and stripped strings for 
        # sorting and the identifier as tuple (identifier, content_as_key)
        letter_log_contents = ["" for x in range(len(logs))]
        letter_log_count = 0
        
        for i in range(len(logs)):
            curr_log = logs[i]
            id, content_type, content = self.determine_log_type(curr_log)
            if content_type == "digit":
                # store digit logs in array to be appended after letter logs
                digit_logs[dig_logs_count] = curr_log
                dig_logs_count += 1
            else:
                # get the string
                #s_key = curr_log[4:].strip().lower()
                #s_key = content.replace(" ", "").lower()
                s_key = content.lower()
                # sort by content squished by for same content then sort by identifier so store tuple
                sorting_tup = (s_key, id)
                letter_log_contents[letter_log_count] = sorting_tup
                letter_log_count += 1
                # insert into dicts
                str_key_dict[sorting_tup] = curr_log
                #orig_str_dict[id] = curr_log

        
        # return all the data structures but chop the lists first
        digit_logs = digit_logs[:dig_logs_count]
        letter_log_contents = letter_log_contents[:letter_log_count]

        return digit_logs, letter_log_contents, str_key_dict # , orig_str_dict
    
    def determine_log_type(self, log):
        '''
        take one log, find identifier and if alpha or digit log
        '''
        id_content_arr = log.split(" ", 1)
        id = id_content_arr[0]
        content = id_content_arr[1]
        content_type = "" # letter or digit
        if(content.replace(" ", "").isalpha()):
            content_type = "letter"
        else: #content.isnumeric()
            content_type = "digit"
        
        return id, content_type, content

            
'''
Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Constraints:

1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.
'''

class Solution_notmine:
    '''
    Approach
    We will divide the problem in two lists. One for letter logs and another for digits. By using .split(maxsplit=1) we obtain [id, words]. We will use this to determine if the log is digit or letter, and also to sort the letter logs (first by words and if tie by id).
    '''
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digit_logs, letter_logs = [], []
        
        for log in logs:
            # split each log into id and words
            id, words = log.split(maxsplit=1)
            # if the first character of words is numeric, it's a digit log
            if words[0].isnumeric():
                digit_logs += [log]    
            else:
                letter_logs += [log]

        for i in range(len(letter_logs)):
            check_split_words = letter_logs[i].split(maxsplit=1)[1]
            print(f'check_split_words: {check_split_words}')
            check_split_ids = letter_logs[i].split(maxsplit=1)[0]
            print(f'check_split_ids: {check_split_ids}')    
        # sort the letter logs by words and if tie by id 
        letter_logs.sort(key=lambda log: (log.split(maxsplit=1)[1], log.split(maxsplit=1)[0]))

        return letter_logs + digit_logs   




# write driver based on above comments
if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]  # Example input
    solution = Solution()
    result = solution.reorderLogFiles(logs)
    expected = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    assert result == expected, f"Expected output: {expected}, but returned: {result}"

    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]  # Example input
    solution = Solution()
    result = solution.reorderLogFiles(logs)
    expected = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    assert result == expected, f"Expected output: {expected}, but returned: {result}"

    logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
    solution = Solution()
    result = solution.reorderLogFiles(logs)
    expected = ["5 m w","j mo","t q h","g 07","o 2 0"]
    assert result == expected, f"Expected output: {expected}, but returned: {result}"
    
    
    # command to run this file
    # python3 937_reorderLogs.py