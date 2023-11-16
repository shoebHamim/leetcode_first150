class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):

        return ":;".join(strs)
        # write your code here

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        return str.split(":;")
        # write your code here