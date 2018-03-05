# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import KakaoService, PopbillException, KakaoButton, KakaoReceiver

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest

'''
개별 내용의 친구톡 이미지를 대량 전송 합니다.
'''

try:
    print("=" * 15 + " 친구톡 이미지 대량 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팝빌에 등록된 플러스 친구 아아디
    plusFriendID = "@팝빌"

    # 발신번호 (팝빌에 등록된 발신번호만 이용가능)
    snd = "010111222"

    # 대체문자 유형 [공백-미전송, C-알림톡내용, A-대체문자내용]
    altSendType = "A"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # 파일경로
    # 이미지 전송 규격 (전송포맷-JPG,JPEG / 용량제한-최대 500Kbte / 이미지 가로&세로 비율 : 1.5 미만)
    filePath = "test.jpg"

    # 이미지 링크 URL
    imageURL = "http://www.linkhub.co.kr"

    KakaoMessages = [] # 1회 최대 전송 1,000건 전송 가능
    for x in range(0, 10):
        KakaoMessages.append(
            KakaoReceiver(
                rcv="0101234567",   #수신번호
                rcvnm="김현진",    #수신자 이름
                msg="안녕하세요 김현진님 링크허브입니다.",  #친구톡 내용 (최대 400자)
                altmsg="(친구톡 대체문자) 안녕하세요 김현진님 링크허브입니다." #대체문자 내용 (최대 2000byte)
            )
        )

    for x in range(0, 10):
        KakaoMessages.append(
            KakaoReceiver(
                rcv="0102345678",   #수신번호
                rcvnm="kimhyunjin", #수신자 이름
                msg="안녕하세요 KIMHYUNJIN님 링크허브입니다.",   #친구톡 내용 (최대 400자)
                altmsg="(친구톡 대체문자) 안녕하세요 KIMHYUNJIN님 링크허브입니다."  #대체문자 내용 (최대 2000byte)
            )
        )


    # 버튼 목록 (최대 5개)
    KakaoButtons = []
    for x in range(0, 2):
        KakaoButtons.append(
            KakaoButton(
                n="팝빌 바로가기",  # 버튼명
                t="WL",  # 버튼유형 [WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
                u1="http://www.popbill.com",  # [앱링크-Android, 웹링크-Mobile]
                u2="http://www.popbill.com"  # [앱링크-IOS, 웹링크-PC URL]
            )
        )

    KakaoButtons.append(
        KakaoButton(
            n="봇키워드",
            t="BK",
        )
    )

    # 광고여부
    adsYN = False

    receiptNum = kakaoService.sendFMS_multi(CorpNum, plusFriendID, snd, "", "",
                                            altSendType, sndDT, filePath, imageURL, KakaoMessages,
                                            KakaoButtons, adsYN, UserID)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
