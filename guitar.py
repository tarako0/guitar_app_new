# 指板情報を数値として取得し、コード、スケールの構成音を与えられたら指板のどの位置にあるかを返す。
class Guitar: # 1'f'平均律、7弦、ドロップDチューニング可能！！
    def __init__(self, root = 0, tuning_type = 'regular', scale_type = 'major_scale', n_onkai = 12, number_of_gen = 6):
        self.root = root # root:0はCを表す。
        self.tuning_type = tuning_type
        self.tuning_dic = {'regular':[4,11,7,2,9,4],'drop_D':[4,11,7,2,9,2]} # tuning:1弦から,ebgdae。0はCを表す。
        self.scale_type = scale_type
        self.scale_dic = {'major_scale':[0,2,4,5,7,9,11],'minor_scale1':[0,2,3,5,7,8,10]} # scaleはメジャースケールであれば、[0,2,4,5,7,9,11]で、ルートを0とし、スケール音がルートから半音刻みでいくつずれているかを書いた辞書。
        self.n_onkai = n_onkai # n_onkai:12音階。
        self.number_of_gen = number_of_gen # number_of_gen:弦の数が6。

    def guitar_scale(self):
        scale_=self.scale_dic[self.scale_type]
        scale_list=[]
        for i in scale_:
            if self.root + i < self.n_onkai:
                scale_list.append(self.root + i)
            else:
                scale_list.append(self.root + i - self.n_onkai)
        return scale_list

    def display_scale(self):
        dosu={0:'Root',1:'9th',2:'M3',3:'P4',4:'P5',5:'6th',6:'M7'}
        tuning = self.tuning_dic[self.tuning_type]
        guitar_scale=self.guitar_scale()
        shiban = [[] for i in range(self.number_of_gen)] # 6
        insert_picture = {}
        for n,i1 in enumerate(tuning): # eadgbe
            for i2 in range(17): # 指板の一番高い音が17フレットまで。
                if i1 + i2 < self.n_onkai: #12
                    if i1 + i2 in guitar_scale: # guitar_scale()のscale_listにある数値のみ取り出せばいい。それ以外は'f'。
                        shiban[n].append(dosu[guitar_scale.index(i1 + i2)])
                        insert_picture[(n + 1, i2)] = guitar_scale.index(i1 + i2) # (n+1弦, i2フレット):度数の識別番号
                    else:
                        shiban[n].append('f')
                elif i1 + i2 < self.n_onkai * 2:
                    if i1 + i2 - self.n_onkai in guitar_scale:
                        shiban[n].append(dosu[guitar_scale.index(i1 + i2 - self.n_onkai)])
                        insert_picture[(n + 1, i2)] = guitar_scale.index(i1 + i2 - self.n_onkai)
                    else:
                        shiban[n].append('f')
                else:
                    if i1 + i2 - self.n_onkai * 2 in guitar_scale:
                        shiban[n].append(dosu[guitar_scale.index(i1 + i2 - self.n_onkai * 2)])
                        insert_picture[(n + 1, i2)] = guitar_scale.index(i1 + i2 - self.n_onkai * 2)
                    else:
                        shiban[n].append('f')
        return shiban, insert_picture