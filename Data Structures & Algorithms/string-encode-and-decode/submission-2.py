class Solution:
    # ["Hello","World"]
    def encode(self, strings: list[str]) -> str:
        return "".join(f"{len(string)}#{string}" for string in strings)

    # "5#Hello5#World11#like12#word"
    def decode(self, encoded: str) -> list[str]:
        result: list[str] = []
        pointer = 0

        while pointer < len(encoded):
            delimiter = encoded.index("#", pointer)
            length = int(encoded[pointer:delimiter])

            pointer = delimiter + 1
            result.append(encoded[pointer : pointer + length])
            pointer += length

        return result
