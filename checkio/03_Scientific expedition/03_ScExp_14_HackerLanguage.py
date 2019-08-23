class HackerLanguage:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def delete(self, N):
        self.text = self.text[0:len(self.text)-N]

    def send(self):
        rtext = ""
        for c in self.text:
            if c.isdigit() or c in ".:!?@$%":
                rtext += c
            elif c == " ":
                rtext += '1000000'
            else:
                rtext += self.to_bin(ord(c))
        print("text: ", self.text)
        print("send text: ", rtext)
        return rtext

    def read(self, text):
        print("enc_text: ", text)
        dec_text = ""
        encr_letter = ""
        for c in text:
            if c not in "01":
                dec_text += encr_letter + c
                encr_letter = ""
            elif len(encr_letter) < 6:
                encr_letter += c
            else:
                encr_letter += c
                print("part: ", encr_letter)
                if encr_letter == '1000000':
                    dec_text += ' '
                else:
                    dec_text += chr(self.from_bin(encr_letter))
                encr_letter = ""
        print("dec_text: ", dec_text)
        return dec_text
            

    @staticmethod
    def to_bin(num):
        if num:
            res = ""
        else:
            return "0"
        while num:
            resid = num % 2
            res = str(resid) + res
            num -= resid
            num //= 2
        return res

    @staticmethod
    def from_bin(bin_num):
        res = 0
        for d,i in enumerate(bin_num):
            res += int(i) * 2**(len(bin_num)-1-d)
        return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()
    message_3 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    assert message_2.read("1001001100000011000011101101100000011101001101001111001011001011100100...") == "I am tired..."
    print("Coding complete? Let's try tests!")
