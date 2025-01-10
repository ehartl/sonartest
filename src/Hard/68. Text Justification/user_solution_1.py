class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        cur_line = []
        cur_len = 0
        
        for word in words:
            if cur_len + len(word) + len(cur_line) > maxWidth:
                # Justify the current line
                num_spaces = maxWidth - cur_len
                if len(cur_line) == 1:
                    result.append(cur_line[0] + ' ' * num_spaces)
                else:
                    space_between_words = num_spaces // (len(cur_line) - 1)
                    extra_spaces = num_spaces % (len(cur_line) - 1)
                    justified_line = ''
                    for i in range(len(cur_line) - 1):
                        justified_line += cur_line[i] + ' ' * (space_between_words + (i < extra_spaces))
                    justified_line += cur_line[-1]
                    result.append(justified_line)
                
                # Reset current line
                cur_line = []
                cur_len = 0
                
            cur_line.append(word)
            cur_len += len(word)
        
        # Last line: left justify
        last_line = ' '.join(cur_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
