# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:04:43 2020

@author: Dominic
"""

##############################################################################
# JTWC best_track 자료를 다운받고 정리하는 파일입니다. 
# PATH와 연도만 수정해서 사용하면 됩니다. 
# 저장되는 파일은 WP TC만을 저장하며 시간, 경도, 위도, 풍속, 기압만을 저장합니다. 
# JTWC best_track 자료를 정리하는데 걸리는 시간은 약 1분 20초 가량 소요됩니다.
##############################################################################


# =============================================================================
# Library

import wget
import zipfile
import os
# =============================================================================


##############################################################################
# 설정할 부분 
PATH = 'D:/DATA/Best_track/JTWC/'
start_year = 2020 
end_year = 2021
##############################################################################
# =============================================================================
# JTWC 자료 다운받고 각 폴더에 저장 

PATH = 'D:/DATA/Best_track/JTWC/'
os.mkdir(PATH +'Original_Data')


for i in range(start_year,end_year):       # 연도설정입니다. 

    url = "https://www.metoc.navy.mil/jtwc/products/best-tracks/" + str(i) + "/" + str(i) + "s-bwp/bwp" + str(i) + ".zip"
    
    wget.download(url, out = PATH )     # JTWC 자료 다운로드
    
    
    os.mkdir(PATH + 'Original_Data/bwp' + str(i))     # 파일 디렉토리 만들기 
    os.mkdir(PATH + 'best_track_' + str(i) + '/')


    fantasy_zip = zipfile.ZipFile(PATH +'bwp' + str(i) +'.zip')              # JTWC 자료 알집 풀 자료  
    fantasy_zip.extractall(PATH +'Original_Data/bwp' + str(i) + '/')     # JTWC 자료 알집 풀고 저장 위치  
    fantasy_zip.close()                                                      # JTWC 자료 알집 close  
    
    os.remove(PATH + 'bwp' + str(i) + '.zip')       # JTWC 자료 알집을 풀었으니 삭제 

# =============================================================================
#  JTWC 중 WP TC만을 읽고 시간, 경도, 위도, 풍속, 기압만 뽑아 track_[year] 에 저장

    FILE_ID = os.listdir(PATH +'Original_Data/bwp' + str(i) + '/')
    

    for kk in FILE_ID:      # 각 해당 연도에 TC 리스트를 읽고 bwp가 아니면 다음 강제로 for를 돌림
        if kk[0:3] != 'bwp':
            continue

        TC_data = []
        # print(kk)
        
        kk[3:5]
        
        with open(PATH +'Original_Data/bwp' + str(i) + '/' + kk,'r') as f: 
            for line in f:
            
                s = line.strip().split(',')
                
                   
                if s[7][-1] =='W':
                    lon = 360 - (float(s[7][:-1])*0.1)
                else:
                    lon = float(s[7][:-1])*0.1

                date = int(s[2])
                lat = float(s[6][:-1])*0.1
                WS = int(s[8])

                
                if i > 2000:
                    Press = int(s[9])
                    TC_data.append([date, lat, lon, WS, Press])
                else:
                    TC_data.append([date, lat, lon, WS])

            
# =============================================================================
# 파일을 저장하는 부분 
        with open(PATH +'best_track_'  + str(i) + '/bwp' + ('%2.2d' %(int(kk[3:5]))) + str(i) + '.txt','w') as outf:
            for iii in range(len(TC_data)):
                
                
                if int(i) > 2000:
                    outf.write('%s %3.1f %3.1f %s %s \n' % (TC_data[iii][0],TC_data[iii][1],TC_data[iii][2],TC_data[iii][3],TC_data[iii][4]))
                else:
                    outf.write('%s %3.1f %3.1f %s \n' % (TC_data[iii][0],TC_data[iii][1],TC_data[iii][2],TC_data[iii][3]))


