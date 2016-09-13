
#coding=utf8
#                       东西南北
#EAST,WEST,SOUTH,NORTH: 右左下上  WEST, NORTH, EAST, SOUTH：

#SOUTH, EAST, NORTH, WEST：下右上左
#l变更  左上右下

text=['###############', '#      IXXXXX #', '#  @          #', '#E S          #', '#             #', '#  I          #', '#  B          #', '#  B   S     W#', '#  B   T      #', '#             #', '#         T   #', '#         B   #', '#N          W$#', '#        XXXX #', '###############']


class main():

    def __init__(self,text):
        self.superB=False#碰到B变成True
        self.nextdirection='SOUTH'#方向
        self.loop=True#到达
        self.status='C'#C顺时针，L逆时针
        self.statusC=['SOUTH','EAST','NORTH','WEST']#顺时针
        self.statusI=['WEST','NORTH','EAST','SOUTH']#逆时针
        self.listT=[]
        self.text=text
        self.crashX=0#碰撞次数
        for i in range(len(text)):
            if text[i].find('@')>0:
                self.start=i,text[i].find('@')
            if text[i].find('$')>0:
                self.end=i,text[i].find('$')
            if text[i].find('T')>0:
                T=i,text[i].find('T')
                self.listT.append(T)
        self.move=self.start#运动坐标

    def direction(self,str):
        '''
        :param str: 碰到的字符串
        :return: 返回下一次运动方向
        '''
        if str=='X' or str=='#':
            if self.superB==True and str=='X':
                self.text[self.next_move[0]]=self.text[self.next_move[0]][:self.next_move[1]]+' '+self.text[self.next_move[0]][self.next_move[1]+1:]
                return self.nextdirection
            else:
                if self.crashX>1:
                    if self.status=='C':
                        self.nextdirection=self.statusC[0] if self.statusC.index(self.nextdirection)==3 else self.statusC[self.statusC.index(self.nextdirection)+1]
                    else:
                        self.nextdirection=self.statusI[0] if self.statusI.index(self.nextdirection)==3 else self.statusI[self.statusI.index(self.nextdirection)+1]
                else:
                    if self.status=='C':
                        self.nextdirection=self.statusC[0]
                    else:
                        self.nextdirection=self.statusI[0]
                self.crashX+=1
                return False
        elif str=='B':
            self.superB=True if self.superB==False else False
            return self.nextdirection
        elif str=='I':
            self.status='I' if self.status=='C' else 'C'
            return self.nextdirection
        elif str=='T':
            for T in self.listT:
                if self.next_move!=T:
                    self.next_move=T
                    break
            return self.nextdirection
        else:
            direction=self.nextdirection
            for i in self.statusC:
                if str==i[0]:
                    self.nextdirection=i
            self.crashX=0#开始运动后次数置为0
            return direction


    def work(self):

        go=True
        mv_list=[]
        while go:

            if self.nextdirection=='SOUTH':
                self.next_move=self.move[0]+1,self.move[1]
                str=self.text[self.next_move[0]][self.next_move[1]]
                direction=self.direction(str)
                if not direction==False:
                    self.move=self.next_move

            elif self.nextdirection=='EAST':
                self.next_move=self.move[0],self.move[1]+1
                str=self.text[self.next_move[0]][self.next_move[1]]
                direction=self.direction(str)
                if not direction==False:
                    self.move=self.next_move

            elif self.nextdirection=='NORTH':
                self.next_move=self.move[0]-1,self.move[1]
                str=self.text[self.next_move[0]][self.next_move[1]]
                direction=self.direction(str)
                if not direction==False:
                    self.move=self.next_move

            elif self.nextdirection=='WEST':
                self.next_move=self.move[0],self.move[1]-1
                str=self.text[self.move[0]][self.move[1]-1]
                direction=self.direction(str)
                if not direction==False:
                    self.move=self.next_move
            mv_list.append(direction)
            if self.move==self.end:
                go=False

            if self.next_move==self.start:
                go=False
                mv_list='Loop'

            if len(mv_list)>200:
                go=False
                mv_list='loop'
            # print str,self.move,direction
        if go==False:
            return mv_list






if __name__ == '__main__':
    main=main(text)
    mv_list=main.work()
    if isinstance(mv_list, str):
        print mv_list
    else:
        for i in mv_list:
            if not i ==False:
                print i









