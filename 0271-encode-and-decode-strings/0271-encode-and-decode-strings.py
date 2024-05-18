class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        print("(*)_@)".join(strs))
        return "(*)_@)".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        print(s.split("(*)_@)"))
        return s.split("(*)_@)")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
