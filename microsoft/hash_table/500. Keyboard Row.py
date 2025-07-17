class key_row:

    def func(self,words):
        row1='qwertyuiop'
        row2='asdfghjkl'
        row3='zxcvbnm'

        res = []
        for word in words:
            temp_chr = []
            for chr in word:
                if chr.lower() in row1:
                    temp_chr.append(1)
                elif chr.lower() in row2:
                    temp_chr.append(2)
                elif chr.lower() in row3:
                    temp_chr.append(3)
                else:
                    pass

            if len(set(temp_chr)) == 1:
                res.append(word)

        return res 



cl = key_row()
print(cl.func(words = ["Hello","Alaska","Dad","Peace"]))