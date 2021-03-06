

class 功能:

    def 做(self, 模組, 函式名, *參數陣列, **參數物件):
        參數物件['物件'] = self
        return getattr(模組, 函式名)(*參數陣列, **參數物件)

    def 揀(self, 揀集內組方法, *參數陣列, **參數物件):
        參數物件['物件'] = self
        return 揀集內組方法.揀(*參數陣列, **參數物件)

    def 揣詞(self, 揣詞方法, *參數陣列, **參數物件):
        參數物件['物件'] = self
        return 揣詞方法.揣詞(*參數陣列, **參數物件)

    def 斷詞(self, 斷詞方法, *參數陣列, **參數物件):
        參數物件['物件'] = self
        return 斷詞方法.斷詞(*參數陣列, **參數物件)

    def 翻譯(self, 翻譯方法, *參數陣列, **參數物件):
        參數物件['物件'] = self
        return 翻譯方法.翻譯(*參數陣列, **參數物件)
