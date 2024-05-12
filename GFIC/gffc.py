import os
import re
import shutil
import tkinter
import ctypes
from tkinter import filedialog

#소녀전선 이미지 정리
#선택한 폴더 내 이미지 이름을 확인
#이미지 이름에 따른 파일명 변경
#그리고 result 파일로 이동
#전문 예시:
"""
일반 : pic_이름(_D)_HD.png
스킨 : pic_이름_스킨번호(_D)_HD.png
개조 : pic_이름Mod_HD.png
@@ 푸른 바다 위 검은 돛 이후 스킨(3.0클라이후)은 hd이름 없음
즉 : pic_이름(_스킨번호)(_D).png
"""

#인형이름 사전 // 파일이름(대문자) : 진짜이름
#숫자~z 번호순 정렬 23.05.15 MSBS 까지
cName = {
    "4type" : "4식"
    ,"06TypeSMG" : "CF05"
    ,"6P62" : "6P62"
    ,"9A91" : "9A-91"
    ,"56-1type" : "56-1식"
    ,"56typeR" : "56식 반"
    ,"59type" : "59식"
    ,"63type" : "63식"
    ,"64type" : "64식"
    ,"79type" : "79식"
    ,"80type" : "80식"
    ,"81typeR" : "81식 카빈"
    ,"88type" : "한양조 88식"
    ,"92type" : "92식"
    ,"95type" : "95식"
    ,"97type" : "97식"
    ,"97typeS" : "97식 산탄총"
    ,"98K" : "Kar98K"
    ,"357" : "아스트라 리볼버"
    ,"A91" : "A-91"
    ,"A545" : "A-545"
    ,"AA12" : "AA-12"
    ,"AAT52" : "AAT52"
    ,"ACR" : "ACR"
    ,"ADS" : "ADS"
    ,"AEK999" : "AEK-999"
    ,"Ai" : "미즈노 아이"
    ,"Ak5" : "Ak5"
    ,"AK12" : "AK-12"
    ,"AK15" : "AK-15"
    ,"AK47" : "AK-47"
    ,"AK74M" : "AK74M"
    ,"AK74U" : "AK-74U"
    ,"AKAlfa" : "AK-Alfa"
    ,"Alma" : "알마 알머스"
    ,"Ameli" : "아멜리"
    ,"AN94" : "AN-94"
    ,"Angelica" : "안젤리카"
    ,"APC9K" : "APC9K"
    ,"APC556" : "APC556"
    ,"APS" : "스테츠킨"
    ,"AR" : "갈릴"
    ,"AR15" : "ST AR-15"
    ,"AR18" : "AR-18"
    ,"AR57" : "AR-57"
    ,"AR70" : "AR70"
    ,"ART556" : "ART556"
    ,"ARX160" : "ARX160"
    ,"Ash127" : "Ash.127"
    ,"ASVAL" : "AS Val"
    ,"AUG" : "AUG"
    ,"AUGPARA" : "AUG Para"
    ,"Ballista" : "발리스타"
    ,"BB_Noel" : "노엘"
    ,"BM59" : "BM59"
    ,"BrenMK" : "브렌"
    ,"BrenTen" : "Bren Ten"
    ,"Bronya" : "브로냐"
    ,"BrowningHP" : "HP-35"
    ,"C14" : "C14"
    ,"C93" : "C93"
    ,"C96" : "C96"
    ,"CAR" : "CAR"
    ,"Carcano1891" : "카르카노M1891"
    ,"Carcano1938" : "카르카노M91 38"
    ,"CBJMS" : "C-MS"
    ,"CETME556" : "Model L"
    ,"ChauchatM1915" : "쇼샤"
    ,"Claes" : "클라에스"
    ,"CLEAR" : "클리어"
    ,"CMR30" : "CMR-30"
    ,"ColtDefender" : "콜드 디펜더"
    ,"ColtSCW" : "SCW"
    ,"ColtWalker" : "콜트 워커"
    ,"Contender" : "컨텐더"
    ,"CR21" : "CR21"
    ,"Cx4Storm" : "Cx4 스톰"
    ,"CZ52" : "CZ52"
    ,"CZ75" : "CZ75"
    ,"CZ100" : "CZ 100"
    ,"CZ805" : "CZ805"
    ,"CZ2000" : "CZ2000"
    ,"Dana" : "다나 제인"
    ,"Danuvia43M" : "43M"
    ,"Delisle" : "드 라일"
    ,"Derringer" : "데린저"
    ,"DesertEagle" : "데저트이글"
    ,"Dorothy" : "도로시 헤이즐"
    ,"DP12" : "DP-12"
    ,"DP28" : "DP-28"
    ,"DSR50" : "DSR-50"
    ,"DTASRS" : "SRS"
    ,"EM2" : "EM-2"
    ,"Erma" : "Erma"
    ,"EVO3" : "EVO 3"
    ,"F1" : "F1"
    ,"F2000" : "F2000"
    ,"FAIL" : "페일"
    ,"Falcon" : "팔콘"
    ,"FAMAS" : "FAMAS"
    ,"FARA83" : "FARA 83"
    ,"Fedorov" : "표도로프"
    ,"FG42" : "FG42"
    ,"FMG9" : "FMG-9"
    ,"FN49" : "FN-49"
    ,"FN57" : "Five-seveN"
    ,"FNFAL" : "FAL"
    ,"FNFNC" : "FNC"
    ,"FNP9" : "FNP"
    ,"FNSPR" : "SPR A3G"
    ,"FO12" : "FO-12"
    ,"FP6" : "FP-6"
    ,"FX05" : "FX-05"
    ,"G3" : "G3"
    ,"G11" : "G11"
    ,"G28" : "G28"
    ,"G36" : "G36"
    ,"G36C" : "G36C"
    ,"G41" : "G41"
    ,"G43" : "G43"
    ,"GeneralLiu" : "류 소총"
    ,"GepardM1" : "게파드 M1"
    ,"GG_elfeldt" : "엘펠트"
    ,"Glock17" : "글록17"
    ,"Gm6Lynx" : "Gm6 Lynx"
    ,"Grizzly" : "그리즐리 MkV"
    ,"GSH18" : "GSH-18"
    ,"Henrietta" : "헨리에타"
    ,"HEZISM1" : "SM-1"
    ,"Himeko" : "히메코"
    ,"HK21" : "HK21"
    ,"HK23" : "HK23"
    ,"HK33" : "HK33"
    ,"HK45" : "HK45"
    ,"HK416" : "HK416"
    ,"HK416Agent" : "요원 HK416"
    ,"HK512" : "HK512"
    ,"HKCAWS" : "CAWS"
    ,"HowaType89" : "89식 소총"
    ,"HS50" : "HS.50"
    ,"HS2000" : "HS2000"
    ,"HSM10" : "HS10"
    ,"IDW" : "IDW"
    ,"INSAS" : "INSAS"
    ,"Ithaca37" : "M37"
    ,"IWS2000" : "IWS2000"
    ,"Jashinchan" : "사신짱"
    ,"Jericho" : "제리코"
    ,"Jill" : "질 스팅레이"
    ,"JS9mm" : "JS 9"
    ,"JS-127" : "JS 50"
    ,"Junko" : "콘노 준코"
    ,"K2" : "K2"
    ,"K3" : "K3"
    ,"K5" : "K5"
    ,"K11" : "K11"
    ,"K31" : "K31"
    ,"KAC" : "KAC PDW"
    ,"KH2002" : "KH2002"
    ,"Kiana" : "키아나"
    ,"KLIN" : "KLIN"
    ,"Kolibri" : "콜리브리"
    ,"Kord" : "Kord"
    ,"KP31" : "수오미"
    ,"KS23" : "KS-23"
    ,"KSG" : "KSG"
    ,"KSVK" : "KSVK"
    ,"L85A1" : "L85A1"
    ,"Lewis" : "루이스"
    ,"Liberator" : "리버레이터"
    ,"Lily" : "호시카와 릴리"
    ,"LS26" : "LS26"
    ,"LTLX7000" : "LTLX7000"
    ,"Lusa" : "Lusa"
    ,"LWMMG" : "LWMMG"
    ,"M1" : "개런드 M1"
    ,"M1A1" : "M1A1"
    ,"M2HB" : "M2HB"
    ,"M3" : "M3"
    ,"M4 SOPMOD II" : "M4 SOPMOD II"
    ,"M4A1" : "M4A1"
    ,"M6ASW" : "M6 ASW"
    ,"M9" : "M9"
    ,"M12" : "M12"
    ,"M14" : "M14"
    ,"M16A1" : "M16A1"
    ,"M21" : "M21"
    ,"M26MASS" : "M26 MASS"
    ,"m45" : "m45"
    ,"M60" : "M60"
    ,"M82" : "M82"
    ,"M82A1" : "M82A1"
    ,"M99" : "M99"
    ,"M110" : "M110"
    ,"M200" : "M200"
    ,"M240L" : "M240L"
    ,"M249SAW" : "M249 SAW"
    ,"M327" : "M327"
    ,"M500" : "M500"
    ,"M590" : "M590"
    ,"M870P" : "M870"
    ,"M950A" : "M950A"
    ,"M1014" : "M1014"
    ,"M1873" : "콜트 리볼버"
    ,"M1887" : "M1887"
    ,"M1891" : "모신나강"
    ,"M1895" : "나강 리볼버"
    ,"M1895MG" : "M1895 CB"
    ,"M1897" : "M1897"
    ,"M1903" : "스프링필드"
    ,"M1911" : "M1911"
    ,"M1918" : "M1918"
    ,"M1919A4" : "M1919A4"
    ,"M1928A1" : "톰슨"
    ,"MAB38" : "베레타 38형"
    ,"MAC10" : "MAC-10"
    ,"MAG7" : "MAG-7"
    ,"Magal" : "마갈"
    ,"MAS38" : "MAS-38"
    ,"MAT49" : "MAT-49"
    ,"MDR" : "MDR"
    ,"Medusa" : "메두사"
    ,"MG3" : "MG3"
    ,"MG4" : "MG4"
    ,"MG5" : "MG5"
    ,"MG34" : "MG34"
    ,"MG36" : "MG36"
    ,"MG42" : "MG42"
    ,"MG338" : "MG338"
    ,"MicroUZI" : "마이크로 우지"
    ,"Minosu" : "미노스"
    ,"mk3A1" : "MK3A1"
    ,"mk12" : "Mk12"
    ,"mk23" : "Mk23"
    ,"mk46" : "Mk46"
    ,"mk48" : "Mk48"
    ,"MLEMK1" : "리엔필드"
    ,"MondragonM1908" : "몬드라곤 M1908"
    ,"MP5" : "MP5"
    ,"MP7" : "MP7"
    ,"MP40" : "MP40"
    ,"MP41" : "MP41"
    ,"MP443" : "MP443"
    ,"MP446" : "MP446"
    ,"MP448" : "MP448"
    ,"MPK" : "MPK"
    ,"MPL" : "MPL"
    ,"MSBS" : "MSBS"
    ,"MT9" : "MT-9"
    ,"NEGEV" : "네게브"
    ,"Nova" : "노바"
    ,"NPC_Kalina" : "카리나"
    ,"NPC_Persica" : "페르시카"
    ,"NS2000" : "NS2000"
    ,"NTW20" : "NTW-20"
    ,"NZ75" : "NZ75"
    ,"OBR" : "OBR"
    ,"OC44" : "OTs-44"
    ,"OTs12" : "OTs-12"
    ,"OTs14" : "OTs-14"
    ,"OTs39" : "OTs-39"
    ,"P7" : "P7"
    ,"P08" : "P08"
    ,"P10C" : "P10C"
    ,"P22" : "P22"
    ,"P30" : "P30"
    ,"P38" : "P38"
    ,"P90" : "P90"
    ,"P99" : "P99"
    ,"P226" : "P226"
    ,"P290" : "P290"
    ,"PA15" : "PA-15"
    ,"PDW" : "허니뱃저"
    ,"Pekora" : "페코라"
    ,"PK" : "PK"
    ,"PKP" : "PKP"
    ,"PM" : "마카로프"
    ,"PM06" : "PM-06"
    ,"PM9" : "PM-9"
    ,"PM1910" : "PM1910"
    ,"PP19" : "PP-19"
    ,"PP90" : "PP-90"
    ,"PP1901" : "PP-19-01"
    ,"PP2000" : "PP2000"
    ,"PPD40" : "PPD-40"
    ,"PPK" : "PPK"
    ,"PPQ" : "PPQ"
    ,"PPS43" : "PPS-43"
    ,"PPsh41" : "PPsh-41"
    ,"PSG1" : "PSG-1"
    ,"PSM" : "PSM"
    ,"PTRD" : "PTRD"
    ,"Px4Storm" : "Px4 스톰"
    ,"Python" : "콜트 파이슨"
    ,"PzB39" : "PzB39"
    ,"QBU88" : "QBU-88"
    ,"QBZ191" : "QBZ-191"
    ,"QSB91" : "QSB-91"
    ,"R5RGP" : "R5"
    ,"R93" : "R93"
    ,"RaidenMei" : "라이든 메이"
    ,"RexZero1" : "Rex Zero 1"
    ,"RFB" : "RFB"
    ,"Rhino" : "라이노"
    ,"Ribeyrolles" : "리베롤"
    ,"Rico" : "리코"
    ,"RMB93" : "RMB93"
    ,"RO635" : "RO635"
    ,"RPD" : "RPD"
    ,"RPK16" : "RPK-16"
    ,"RPK203" : "RPK-203"
    ,"RT20" : "RT-20"
    ,"SACR" : "S-ACR"
    ,"SAF" : "SAF"
    ,"Saiga12" : "Saiga-12"
    ,"Saiga308" : "Saiga-308"
    ,"Saki" : "니카이도 사키"
    ,"Sakura" : "미나모토 사쿠라"
    ,"SAR21" : "SAR-21"
    ,"SAT8" : "S.A.T.8"
    ,"Savage99" : "Savage99"
    ,"SCARH" : "SCAR-H"
    ,"SCARL" : "SCAR-L"
    ,"scout" : "스카웃"
    ,"SCR" : "SCR"
    ,"Seele" : "제레"
    ,"SEI" : "세이 아사기리"
    ,"Shipka" : "시프카"
    ,"SIG510" : "SIG-510"
    ,"SIG556" : "SIG-556"
    ,"SIGMCX" : "MCX"
    ,"Six12" : "Six12"
    ,"SKS" : "시모노프"
    ,"SL8" : "SL8"
    ,"SP9" : "SP9"
    ,"SPAS12" : "SPAS-12"
    ,"SPAS15" : "SPAS-15"
    ,"SpectreM4" : "SpectreM4"
    ,"Spitfire" : "스핏파이어"
    ,"SPP1" : "SPP-1"
    ,"SPS" : "셰르듀코프"
    ,"SR2" : "SR-2"
    ,"SR3MP" : "SR-3MP"
    ,"SSG69" : "SSG 69"
    ,"SSG3000" : "SSG 3000"
    ,"Stella" : "스텔라 호시이"
    ,"StenMK2" : "스텐MkII"
    ,"Sterling" : "스털링"
    ,"STG44" : "STG-44"
    ,"stg940" : "STG-940"
    ,"SUB2000" : "SUB 2000"
    ,"SuperSASS" : "SuperSASS"
    ,"SuperShorty" : "SuperShorty"
    ,"SV98" : "SV-98"
    ,"SVCh" : "SVCh"
    ,"SVD" : "SVD"
    ,"SVT38" : "SVT-38"
    ,"T65" : "T65"
    ,"T77" : "T77"
    ,"T91" : "T91"
    ,"T5000" : "T-5000"
    ,"Tabuk" : "타부크 저격소총"
    ,"TAC50" : "TAC-50"
    ,"Tae" : "야마다 타에"
    ,"TAR21" : "TAR-21"
    ,"TavorTS12" : "TS12"
    ,"TCMS" : "T-CMS"
    ,"TEC9" : "TEC-9"
    ,"TFQ" : "TF-Q"
    ,"Theresa" : "테레사"
    ,"Thunder50" : "썬더"
    ,"TKB408" : "TKB408"
    ,"TMP" : "TMP"
    ,"Triela" : "트리엘라"
    ,"TT33" : "토카레프"
    ,"Type03" : "03식"
    ,"Type62" : "62식"
    ,"Type64-AR" : "64식 소총"
    ,"Type88" : "88식"
    ,"Type100" : "100식"
    ,"UKM2000" : "UKM2000"
    ,"UMP9" : "UMP9"
    ,"UMP40" : "UMP40"
    ,"UMP45" : "UMP45"
    ,"USAS12" : "USAS-12"
    ,"USPCompact" : "USPCompact"
    ,"UTS15" : "UTS-15"
    ,"Vector" : "Vector"
    ,"VectorAgent" : "요원 Vector"
    ,"VEPR" : "VEPR"
    ,"VHS" : "VHS"
    ,"VigneronM2" : "비뉴홍 M2"
    ,"VP70" : "VP70"
    ,"VP1915" : "VP1915"
    ,"VPM5" : "V-PM5"
    ,"VSK" : "VSK-94"
    ,"VZ61" : "스콜피온"
    ,"WA2000" : "WA2000"
    ,"Webley" : "웨블리"
    ,"Welrod" : "웰로드 MkII"
    ,"WKP" : "WKP"
    ,"wz29" : "wz.29"
    ,"X95" : "X95"
    ,"xm3" : "XM3"
    ,"XM8" : "XM8"
    ,"Yurine" : "하나조노 유리네"
    ,"Yuugiri" : "유우기리"
    ,"Z62" : "Z62"
    ,"ZasM76" : "Zas M76"
    ,"ZastavaM21" : "Zas M21"
    ,"ZB26" : "ZB-26"
    ,"ZIP22" : "ZIP .22"
    
    
}
#인형번호 사전 // 파일이름(대문자) : 인형번호
cNumber = {
    #일반
    "M1873" : "001"
    ,"M1911" : "002"
    ,"M9" : "003"
    ,"Python" : "004"
    ,"M1895" : "005"
    ,"TT33" : "006"
    ,"APS" : "007"
    ,"PM" : "008"
    ,"P38" : "009"
    ,"PPK" : "010"
    ,"P08" : "011"
    ,"C96" : "012"
    ,"92type" : "013"
    ,"357" : "014"
    ,"Glock17" : "015"
    ,"M1928A1" : "016"
    ,"M3" : "017"
    ,"MAC10" : "018"    
    ,"FMG9" : "019"
    ,"Vector" : "020"
    ,"PPsh41" : "021"
    ,"PPS43" : "022"
    ,"PP90" : "023"
    ,"PP2000" : "024"
    ,"MP40" : "025"
    ,"MP5" : "026"
    ,"VZ61" : "027"
    ,"MP7" : "028"
    ,"StenMK2" : "029"
    ,"MAB38" : "031"
    ,"MicroUZI" : "032"
    ,"m45" : "033"
    ,"M1" : "034"
    ,"M1A1" : "035"
    ,"M1903" : "036"
    ,"M14" : "037"
    ,"M21" : "038"
    ,"M1891" : "039"
    ,"SVT38" : "040"
    ,"SKS" : "041"
    ,"PTRD" : "042"
    ,"SVD" : "043"
    ,"SV98" : "044"
    ,"98K" : "046"
    ,"G43" : "047"
    ,"WA2000" : "048"
    ,"56typeR" : "049"
    ,"MLEMK1" : "050"
    ,"FN49" : "051"
    ,"BM59" : "052"
    ,"NTW20" : "053"
    ,"M16A1" : "054"
    ,"M4A1" : "055"
    ,"M4 SOPMOD II" : "056"
    ,"AR15" : "057"
    ,"AK47" : "058"
    ,"AK74U" : "059"
    ,"ASVAL" : "060"
    ,"STG44" : "061"
    ,"G41" : "062"
    ,"G3" : "063"
    ,"G36" : "064"
    ,"HK416" : "065"
    ,"56-1type" : "066"
    ,"L85A1" : "068"
    ,"FAMAS" : "069"
    ,"FNFNC" : "070"
    ,"AR" : "071"
    ,"TAR21" : "072"
    ,"AUG" : "073"
    ,"SIG510" : "074"
    ,"M1918" : "075"
    ,"M2HB" : "077"
    ,"M60" : "078"
    ,"M249SAW" : "079"
    ,"M1919A4" : "080"
    ,"LWMMG" : "081"
    ,"DP28" : "082"
    ,"RPD" : "084"
    ,"PK" : "085"
    ,"MG42" : "086"
    ,"MG34" : "087"
    ,"MG3" : "088"
    ,"BrenMK" : "089"
    ,"FNP9" : "090"
    ,"MP446" : "091"
    ,"SpectreM4" : "092"
    ,"IDW" : "093"
    ,"64type" : "094"
    ,"88type" : "095"
    ,"Grizzly" : "096"
    ,"M950A" : "097"
    ,"SPP1" : "098"
    ,"Mk23" : "099"
    ,"P7" : "100"
    ,"UMP9" : "101"
    ,"UMP40" : "102"
    ,"UMP45" : "103"
    ,"G36C" : "104"
    ,"OTs12" : "105"
    ,"FNFAL" : "106"
    ,"F2000" : "107"
    ,"CZ805" : "108"
    ,"MG5" : "109"
    ,"FG42" : "110"
    ,"AAT52" : "111"
    ,"NEGEV" : "112"
    ,"SPS" : "113"
    ,"Welrod" : "114"
    ,"KP31" : "115"
    ,"Z62" : "116"
    ,"PSG1" : "117"    
    ,"9A91" : "118"
    ,"OTs14" : "119"
    ,"ARX160" : "120"
    ,"MK48" : "121"
    ,"G11" : "122"
    ,"P99" : "123"
    ,"SuperSASS" : "124"
    ,"MG4" : "125"
    ,"NZ75" : "126"
    ,"79type" : "127"
    ,"M99" : "128"
    ,"95type" : "129"
    ,"97type" : "130"
    ,"EVO3" : "131"
    ,"59type" : "132"
    ,"63type" : "133"
    ,"AR70" : "134"
    ,"SR3MP" : "135"
    ,"PP19" : "136"
    ,"PP1901" : "137"
    ,"6P62" : "138"
    ,"BrenTen" : "139"
    ,"PSM" : "140"
    ,"USPCompact" : "141"
    ,"FN57" : "142"
    ,"RO635" : "143"
    ,"MT9" : "144"
    ,"OC44" : "145"
    ,"G28" : "146"
    ,"SSG69" : "147"
    ,"IWS2000" : "148"
    ,"AEK999" : "149"
    ,"Shipka" : "150"
    ,"M1887" : "151"
    ,"M1897" : "152"
    ,"Ithaca37" : "153"
    ,"M500" : "154"
    ,"M590" : "155"
    ,"SuperShorty" : "156"
    ,"KSG" : "157"
    ,"KS23" : "158"
    ,"RMB93" : "159"
    ,"Saiga12" : "160"
    ,"97typeS" : "161"
    ,"SPAS12" : "162"
    ,"AA12" : "163"
    ,"FP6" : "164"
    ,"M1014" : "165"
    ,"CZ75" : "166"
    ,"HK45" : "167"
    ,"Spitfire" : "168"
    ,"ColtSCW" : "169"
    ,"Ash127" : "170"
    ,"Ribeyrolles" : "171"
    ,"RFB" : "172"
    ,"PKP" : "173"
    ,"81typeR" : "174"
    ,"ART556" : "175"
    ,"TMP" : "176"
    ,"KLIN" : "177"
    ,"F1" : "178"
    ,"DSR50" : "179"
    ,"PzB39" : "180"
    ,"T91" : "181"
    ,"wz29" : "182"
    ,"Contender" : "183"
    ,"T5000" : "184"
    ,"Ameli" : "185"
    ,"P226" : "186"
    ,"Ak5" : "187"
    ,"SAT8" : "188"
    ,"USAS12" : "189"
    ,"NS2000" : "190"
    ,"M12" : "191"
    ,"JS-127" : "192"
    ,"T65" : "193"
    ,"K2" : "194"
    ,"HK23" : "195"
    ,"ZastavaM21" : "196"
    ,"Carcano1891" : "197"
    ,"Carcano1938" : "198"
    ,"80type" : "199"
    ,"xm3" : "200"
    ,"GepardM1" : "201"
    ,"Thunder50" : "202"
    ,"PDW" : "203"
    ,"Ballista" : "204"
    ,"AN94" : "205"
    ,"AK12" : "206"
    ,"CZ2000" : "207"
    ,"HK21" : "208"
    ,"OTs39" : "209"
    ,"CZ52" : "210"
    ,"DTASRS" : "211"
    ,"K5" : "212"
    ,"CBJMS" : "213"
    ,"ADS" : "214"
    ,"MDR" : "215"
    ,"XM8" : "216"
    ,"HEZISM1" : "217"
    ,"T77" : "218"
    ,"MP443" : "220"
    ,"GSH18" : "221"
    ,"TAC50" : "222"
    ,"CETME556" : "223"
    ,"PM06" : "224"
    ,"Cx4Storm" : "225"
    ,"Mk12" : "226"
    ,"A91" : "227"
    ,"Type100" : "228"
    ,"M870P" : "229"
    ,"OBR" : "230"
    ,"M82A1" : "231"
    ,"MP448" : "232"
    ,"Px4Storm" : "233"
    ,"JS9mm" : "234"
    ,"FNSPR" : "235"
    ,"K11" : "236"
    ,"SAR21" : "237"
    ,"Type88" : "238"
    ,"Type03" : "239"
    ,"Mk46" : "240"
    ,"RT20" : "241"
    ,"P22" : "242"
    ,"Type64-AR" : "243"
    ,"TEC9" : "244"
    ,"P90" : "245"
    ,"K31" : "247"
    ,"Jericho" : "248"
    ,"Type62" : "249"
    ,"HS2000" : "250"
    ,"X95" : "251"
    ,"KSVK" : "252"
    ,"Lewis" : "253"
    ,"UKM2000" : "254"
    ,"scout" : "255"
    ,"Falcon" : "256"
    ,"M200" : "257"
    ,"Magal" : "258"
    ,"PM9" : "259"
    ,"PA15" : "260"
    ,"QBU88" : "261"
    ,"EM2" : "262"
    ,"MG36" : "263"
    ,"ChauchatM1915" : "264"
    ,"HK33" : "265"
    ,"R93" : "266"
    ,"MP41" : "267"
    ,"TCMS" : "268"
    ,"P30" : "269"
    ,"4type" : "270"
    ,"K3" : "271"
    ,"DesertEagle" : "272"
    ,"SSG3000" : "273"
    ,"ACR" : "274"
    ,"M1895MG" : "275"
    ,"Kord" : "276"
    ,"VP70" : "277"
    ,"Six12" : "278"
    ,"INSAS" : "279"
    ,"MAT49" : "280"
    ,"HKCAWS" : "281"
    ,"DP12" : "282"
    ,"Liberator" : "283"
    ,"ZasM76" : "284"
    ,"C93" : "285"
    ,"KAC" : "286"
    ,"SIG556" : "287"
    ,"CR21" : "288"
    ,"R5RGP" : "289"
    ,"HowaType89" : "290"
    ,"Danuvia43M" : "291"
    ,"RPK16" : "292"
    ,"AK15" : "293"
    ,"Webley" : "294"
    ,"06TypeSMG" : "295"
    ,"SL8" : "296"
    ,"M82" : "297"
    ,"VEPR" : "298"
    ,"HSM10" : "299"
    ,"CAR" : "300"
    ,"MAS38" : "301"
    ,"ColtDefender" : "302"
    ,"BrowningHP" : "303"
    ,"SAF" : "304"
    ,"Tabuk" : "305"
    ,"AKAlfa" : "306"
    ,"ZB26" : "307"
    ,"C14" : "308"
    ,"WKP" : "309"
    ,"RexZero1" : "310"
    ,"Lusa" : "311"
    ,"VSK" : "312"
    ,"SACR" : "313"
    ,"stg940" : "314"
    ,"AUGPARA" : "315"
    ,"GeneralLiu" : "316"
    ,"MondragonM1908" : "317"
    ,"VHS" : "318"
    ,"PM1910" : "319"
    ,"Gm6Lynx" : "320"
    ,"TavorTS12" : "321"
    ,"QSB91" : "322"
    ,"LTLX7000" : "323"
    ,"M6ASW" : "324"
    ,"VPM5" : "325"
    ,"HK512" : "326"
    ,"SUB2000" : "327"
    ,"AR57" : "328"
    ,"SVCh" : "329"
    ,"FX05" : "330"
    ,"Kolibri" : "331"
    ,"Derringer" : "332"
    ,"VP1915" : "333"
    ,"Savage99" : "334"
    ,"Fedorov" : "335"
    ,"PPD40" : "336"
    ,"Delisle" : "337"
    ,"SIGMCX" : "338"
    ,"RPK203" : "339"
    ,"TKB408" : "340"
    ,"SP9" : "341"
    ,"KH2002" : "342"
    ,"APC556" : "343"
    ,"FARA83" : "344"
    ,"MG338" : "345"
    ,"CZ100" : "346"
    ,"SR2" : "347"
    ,"HS50" : "348"
    ,"AK74M" : "349"
    ,"FO12" : "350"
    ,"M26MASS" : "351"
    ,"Nova" : "352"
    ,"MAG7" : "353"
    ,"ZIP22" : "354"
    ,"VigneronM2" : "355"
    ,"A545" : "356"
    ,"Rhino" : "357"
    ,"PPQ" : "358"
    ,"Sterling" : "359"
    ,"TFQ" : "360"
    ,"QBZ191" : "361"
    ,"LS26" : "362"
    ,"MPL" : "363"
    ,"MPK" : "364"
    ,"SCR" : "365"
    ,"SPAS15" : "366"
    ,"MK3A1" : "367"
    ,"UTS15" : "368"
    ,"M327" : "369"
    ,"P290" : "370"
    ,"Saiga308" : "371"
    ,"AR18" : "372"
    ,"CMR30" : "373"
    ,"M240L" : "374"
    ,"ColtWalker" : "375"
    ,"Erma" : "376"
    ,"SCARH" : "377"
    ,"SCARL" : "378"
    ,"P10C" : "379"
    ,"APC9K" : "380"
    ,"M110" : "381"
    ,"MSBS" : "382"
    ,"VP9" : "383"
    
    #npc
    ,"NPC_Kalina" : ""
    ,"NPC_Persica" : ""
    #콜라보
    ,"BB_Noel" : "1001"
    ,"GG_elfeldt" : "1002"
    ,"Kiana" : "1003"
    ,"RaidenMei" : "1004"
    ,"Bronya" : "1005"
    ,"Theresa" : "1006"
    ,"Himeko" : "1007"
    ,"Seele" : "1008"
    ,"CLEAR" : "1009"
    ,"FAIL" : "1010"
    ,"Jill" : "1017"    
    ,"SEI" : "1018"
    ,"Dorothy" : "1019"
    ,"Stella" : "1020"
    ,"Alma" : "1021"
    ,"Dana" : "1022"
    ,"Henrietta" : "1023"
    ,"Rico" : "1024"
    ,"Triela" : "1025"
    ,"Claes" : "1026"
    ,"Angelica" : "1027"
    ,"VectorAgent" : "1028"
    ,"HK416Agent" : "1029"
    ,"Jashinchan" : "1030"
    ,"Pekora" : "1031"
    ,"Medusa" : "1032"
    ,"Yurine" : "1033"
    ,"Minosu" : "1034"
    ,"Tae" : "1035"
    ,"Lily" : "1036"
    ,"Sakura" : "1037"
    ,"Ai" : "1038"
    ,"Junko" : "1039"
    ,"Yuugiri" : "1040"
    ,"Saki" : "1041"
    
    
}

#제거 처리할 파일명 세트
exceptFileName = {
    "spscarh_big_hd@pic_spSCARH_HD.png"
    ,"spscarh_big_hd@pic_spSCARH_D_HD.png"
    ,"spscarl_big_hd@pic_spSCARL_HD.png"
    ,"spscarl_big_hd@pic_spSCARL_D_HD.png"
    ,"desktop.ini"
    ,"whatever.ini"
}

#dict, list 포함 dict 모든 key 값 대문자
def dict_key_upper(data):
    if(isinstance(data, dict)):
        return {k.upper():dict_key_upper(v) for k,v in data.items()}
    elif(isinstance(data, list)):
        return [dict_key_upper(v) for v in data]
    else:
        return data

#결과 경로 설정
def setResultPath(dir_path : str):
    #반환값
    result_path = ""
    
    #경로 폴더 단위로 리스트화
    pathList = dir_path.split("/")
    #마지막 경로 result로 변경
    pathList[len(pathList)-1] = "result"
    #경로 재조합
    result_path = "/".join(pathList)
    print("결과 저장 경로 : ",result_path)

    return result_path

#이미지 파일 이름 확인 if(fileName.contains("pic_이름"))

#전체 파일 이름 조정
def namerAllFile(file_list):
    #반환값
    modFile_list = []

    #print(file_list)
    for fileName in file_list:
        #1. 개조 인형이면 "Mod" 문자를 "_M"으로 대체
        if("Mod" in fileName):
            fileName = re.sub("Mod","_M",fileName)

        #2. "_HD" 문자 제거
        if("_HD" in fileName):
            fileName = re.sub("_HD","",fileName)

        #3. result 폴더는 제외
        if(fileName == "result"):
            continue

        #반환 리스트에 추가
        modFile_list.append(fileName)

    #print("끝: ",modFile_list)

    return modFile_list
#파일명의 인형 이름에 해당하는 부분 자르기
def tokenizer(fileName : str):
    #반환값
    dollFullName = ""

    print("전문: "+fileName)
    try:
        #앞부분 자르기
        #pic, Pic 구분
        if("pic_" in fileName):
            subFront = fileName.split("pic_")    
        elif("Pic_" in fileName):
            subFront = fileName.split("Pic_")    
        print("pic 이후: ",subFront)
        #확장자 제거
        subExe = subFront[1].split(".png")
        #뒷부분 자르기
        subBack = subExe[0].split("_")
        print("_ 문항별 자르기: ",subBack)
        #subBack[1] 이 숫자라면 = 스킨번호 일때 앞에 S붙이기
        if(len(subBack) > 1):
            if(subBack[1].isdigit()):
                subBack[1] = "S"+subBack[1]
        #결과 반환값에 대입
        dollFullName = subBack

        return dollFullName
    except:
        print("파일 이름 : ",fileName,"에서 에러 발생")

#인형 이름 계산
def setName(dollInfo : list):
    #반환값
    name = ""

    #값 설정
    #@@ 하드코딩 "_" 가 들어가는 인형명 예외 처리 
    if(dollInfo[0] == "BB" or dollInfo[0] == "GG" or dollInfo[0] == "NPC"):
        name = dollInfo[0] + "_" + dollInfo[1]
    else:
        name = dollInfo[0]

    print("이름 : ",name)
    

    return name

#파일명 계산
def setFileName(dollInfo : list , name : str):
    #반환값
    newFileName = ""
    #키값 대문자화
    name = name.upper()

    #dollInfo[0] = 이름 부분을 "No.인형번호 인형이름" 으로 변경
    dollInfo[0] = "No." + cNumber[name] + " " + cName[name]
    #dollInfo 리스트 _으로 결합
    newFileName = "_".join(dollInfo)
    #확장자 추가
    newFileName += ".png"
    print("결과 : ",newFileName)

    return newFileName

#리스트내 파일명 변경
def namer(file_list : list):
    #반환값
    modFile_list = []

    for fileName in file_list:
        #정보 전문 리스트화
        dollInfo = tokenizer(fileName)
        #인형 이름
        name = setName(dollInfo)
        #파일명 계산
        newFileName = setFileName(dollInfo=dollInfo,name=name)
        #파일명 변경 및 result 폴더로 이동
        print("변경 전:", fileName)
        print("변경 후:", newFileName)
        modFile_list.append(newFileName)




        print("===================================")

    return modFile_list

#원본 리스트와 변경할 리스트 교체 및 result 폴더로 이동
def replacer(originFile_list : list, modFile_list : list, dir_path : str, result_path : str):
    #파일 이동
    for i in range(len(originFile_list)):
        #원본 전체 파일명
        originFilePath = dir_path+"/"+originFile_list[i]
        #변경한 전체 파일명
        modFilePath = result_path+"/"+modFile_list[i]
        #파일 복사
        shutil.copy2(originFilePath, modFilePath) 

def endMessage():
    ctypes.windll.user32.MessageBoxW(0, "처리 종료", "처리 알림", 16)

#=========실행단
#0. dict 키값 전부 대문자로
cName = dict_key_upper(cName)
cNumber = dict_key_upper(cNumber)

if __name__ == "__main__" :
    root = tkinter.Tk()
    root.withdraw()
    #1. 폴더 선택
    dir_path = filedialog.askdirectory(parent=root,initialdir="/",title="이미지가 들어있는 폴더를 선택해주세요.")
    print("\n 선택된 경로 : ",dir_path)
    #폴더의 파일명 리스트
    file_list = list(set(os.listdir(dir_path)) - exceptFileName)
    #2. 전체 파일명 조정
    modFile_list = namerAllFile(file_list)
    #3. 결과 경로 설정 / 선택한 폴더와 동등한 위치에 생성
    result_path = setResultPath(dir_path)
    try:
        #4. 결과 폴더 생성
        os.makedirs(result_path)
    except:
        print("result 폴더 이미 존재")
        pass
    #5. 리스트내 파일명 변경
    modFile_list = namer(modFile_list)
    #6. 원본 파일명 리스트와 대조하여 변경된 파일명 파일 복사
    replacer(originFile_list=file_list, modFile_list=modFile_list, dir_path=dir_path, result_path=result_path)
    #7 종료 메시지
    endMessage()