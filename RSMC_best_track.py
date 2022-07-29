# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 00:11:25 2020

@author: Dominic
"""



import os

PATH = 'D:/DATA/Best_track/RSMC/track_'

# 파일을 만드는 것도 자동화를 해야하지만 깔끔하게 보이고 싶었습니다.... 아직 부족합니다. 
for mk in range(1951,2020):
    os.mkdir(PATH + str(mk))

TEST = []
TC_data = [] 
T = 0
K = 0 

with open('D:/DATA/Best_track/RSMC/bst_all.txt','r') as f:
    for line in f:
        
        s = line.strip().split(' ')


        if s[0] == '66666':
            TC_info = []
                    
            for kk in range(len(s)):
                
                if not s[kk]:
                  T += 1
                else:
                    TC_info.append(str(s[kk]))
  
            TC_num = TC_info[1]        # 저장을 위한 TC number 설정
            TC_data_len = TC_info[2]   # 저장을 위한 TC length 설정
            

            
            b = 0                # TC의 data 길이에 따른 저장을 위한 b 설정 
            
            continue             # 66666을 발견했을 땐 바로 다음 줄을 읽기 위한 continue


        # RSMC 자료를 읽을 때 기압에 따라 split(' ') 결과가 달라지기 때문에 if문을 통해 고려함 
        # RSMC 자료는 1977년 이후부터 풍속이 기록됨 1977년 이후로 자료의 숫자가 달라짐 물론 위치도.

        TEST = []
        for ii in range(len(s)):
            
            if not s[ii]:
                K += 1
            else:
                K += 1
                TEST.append(s[ii])
                
        TC_data.append(TEST[:])
   
    
        b += 1

        if b == int(TC_data_len):
            if int(TC_num[0:2]) < 20 :
                Year = str('20' + TC_num[0:2])
            else:
                Year = str('19' + TC_num[0:2])
            
            with open(PATH + Year + '/' + str(TC_num) + 'tc.txt','w') as outf:
                for i in range(len(TC_data)):
                    
                    
                    if int(TC_num) < 7700:
                        outf.write('%s %s %s %s %s %s \n' % (TC_data[i][0],TC_data[i][1],TC_data[i][2],TC_data[i][3],TC_data[i][4],TC_data[i][5]))
                    else:
                         outf.write('%s %s %s %s %s %s %s \n' % (TC_data[i][0],TC_data[i][1],TC_data[i][2],TC_data[i][3],TC_data[i][4],TC_data[i][5],TC_data[i][6]))
                        
                        
                        
                # 저장을 했으니 다음 TC를 읽기 위해 clear를 해줍니다. 
                TC_data = [] 
                TC_data_len = []
                
                        
                

        
        
        
        
        
        
        