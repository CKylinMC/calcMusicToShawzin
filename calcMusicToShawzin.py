class calcMusicToShawzin:
    import string
    __letters = {
        '1':'B',
        '2':'C',
        '3':'E',
        '4':'J',
        '5':'K',
        '6':'M',
        '7':'R',
        '8':'S',
        '9':'U',
        '+':'h',
        '-':'i',
        '*':'k',
        '/':'B',
        '=':'C',
    }
    cur = '5'
    __spaceMarks = list(string.ascii_uppercase + string.ascii_lowercase)
    __spaceMarks += [str(i) for i in range(0, 10)]
    __spaceMarks += ['+','/']
    space = 3

    def resetData(self):
        self.slot = 0
        self.rounds = 0
        self.songStr = self.cur

    def convert(self, txtCalcMusic):
        self.resetData()
        tmpjump = 1
        nospace = False
        for w in txtCalcMusic:
            if w == ' ':
                if nospace:
                    tmpjump += 1
                else:
                    tmpjump += self.space
                continue
            if w == '[':
                nospace = True
                continue
            if w == ']':
                nospace = False
                continue
            if not w in self.__letters:
                print("Unknow word: '{}'".format(w))
                return False
            self.songStr += self.__letters[w]
            self.songStr += self.jump(tmpjump)
            if nospace:
                tmpjump = 1
            else:
                tmpjump = self.space
        return True

    def jump(self, ts=1):
        countMarks = len(self.__spaceMarks)
        self.slot += ts
        if self.slot >= countMarks:
            self.rounds += 1
            if self.rounds >= countMarks:
                self.rounds -= self.rounds % countMarks
            self.slot = self.slot % countMarks
        return self.__spaceMarks[self.rounds] + self.__spaceMarks[self.slot]
        
    def convertFromFile(self, txtFilePath):
        scores = None
        with open(txtFilePath,mode = 'r', encoding='utf-8') as f:
            scores = f.read()
            f.close()
        if scores == None:
            print("File has no content")
            return False
        scores = scores.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
        scores = scores.replace("＋", "+")
        scores = scores.replace("－", "-").replace("—", "-")
        scores = scores.replace("x", "*").replace("×", "*")
        scores = scores.replace("÷", "/")
        return self.convert(scores)
        
    def getShawzinScores(self):
        return self.songStr

    def __init__(self, space=3):
        self.space = space
        self.resetData()

if __name__ == '__main__':
    import optparse
    Parser = optparse.OptionParser(
        description='Calculator Music To Shawzin Scores Converter 1.0 by CKylin')
    Parser.add_option('-f', '--file', dest='file',
                      help='Load calculator scores from file',default=None)
    Parser.add_option('-o', '--output', dest='output',
                      help='Output shawzin scores to a file',default=None)
    Parser.add_option('-s', '--space', dest='space',
                      help='Set the space between letters',default=3,type=int)
    opts, args = Parser.parse_args()
    CMS = calcMusicToShawzin(opts.space)
    if opts.file == None:
        try:
            stat = CMS.convert(input())
        except KeyboardInterrupt:
            print('Input cancelled')
            stat = False
    else:
        stat = CMS.convertFromFile(opts.file)
    if stat:
        if opts.output == None:
            print(CMS.getShawzinScores())
        else:
            with open(opts.output, mode='a', encoding='utf-8') as f:
                print(CMS.getShawzinScores(), file=f)
                f.close()
    else:
        print("Errored while converting")
