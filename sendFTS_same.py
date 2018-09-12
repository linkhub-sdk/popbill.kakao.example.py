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
동일한 내용의 친구톡 텍스트를 대량 전송 합니다.
'''

try:
    print("=" * 15 + " 친구톡 텍스트 대량 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팝빌에 등록된 플러스 친구 아아디
    plusFriendID = "@팝빌"

    # 발신번호 (팝빌에 등록된 발신번호만 이용가능)
    snd = "010111222"

    # [동보] 친구톡 내용 (최대 1000자)
    content = "안녕하세요 팝빌 플친님 파이썬입니다."

    # [동보] 대체문자 내용 (최대 2000byte)
    altContent = "(친구톡 대체문자) 안녕하세요 팝빌 플친님 파이썬입니다."

    # 대체문자 유형 [공백-미전송, C-알림톡내용, A-대체문자내용]
    altSendType = "A"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    KakaoMessages = [] # 1회 최대 전송 1,000건 전송 가능
    for x in range(0, 2):
        KakaoMessages.append(
            KakaoReceiver(
                rcv="0101235678",   #수신번호
                rcvnm="팝친"  #수신자 이름
            )
        )

    # 버튼 목록 (최대 5개)
    KakaoButtons = []
    for x in range(0, 1):
        KakaoButtons.append(
            KakaoButton(
                n="팝빌 바로가기",  # 버튼명
                t="WL",  # [버튼유형 WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
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

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    requestNum = ""

    receiptNum = kakaoService.sendFTS_multi(CorpNum, plusFriendID, snd, content, altContent, altSendType,
                                            sndDT, KakaoMessages, KakaoButtons, adsYN, UserID, requestNum)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
