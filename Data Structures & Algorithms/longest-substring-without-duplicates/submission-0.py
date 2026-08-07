class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Tracks {character: last_seen_index}
        max_length = 0
        left = 0

        for right in range(len(s)):
            current_char = s[right]
            
            # If character is seen inside the current window, slide left pointer
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
                
            # Update or add the character's newest position
            char_map[current_char] = right
            
            # Calculate window size and update max length
            current_window_len = right - left + 1
            max_length = max(max_length, current_window_len)
            
        return max_length