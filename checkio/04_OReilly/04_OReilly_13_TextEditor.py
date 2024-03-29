import copy

class Text:
    def __init__(self):
        self.text = ""
        self.font = ""
        
    def write(self, atext):
        self.text += atext

    def set_font(self, afont):
        self.font = afont

    def show(self):
        if self.font:
            return f"[{self.font}]{self.text}[{self.font}]"
        else:
            return f"{self.text}"

    def restore(self, text):
        self.text = text.text
        self.font = text.font

class SavedText:
    def __init__(self):
        self.num = 0
        self.versions = []

    def save_text(self, text):
        self.versions.append(copy.copy(text)) # check on copy
        self.num += 1

    def get_version(self, number):
        return copy.copy(self.versions[number]) # check on copy


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
