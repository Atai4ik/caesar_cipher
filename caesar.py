class CaesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        result = ""
        for i in plainText:
            if i in self._alphabet:
                result += self._alphabet[(self._alphabet.index(i) + self._shift) % (len(self._alphabet))]
            else:
                result += i
        return result

caesar = CaesarCipher()
caesar.set_alphabet('abcdefghijklmnopqrstuvwxyz')
caesar.set_shift(3)
print caesar.encode('The quick brown fox jumps over the lazy dog')
