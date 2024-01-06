class Signature:
    def __init__(self, r, s):
        self.r = r
        self.s = s
        
    def __repr__(self):
        return 'Signature : {}'.format(hex(self.s))