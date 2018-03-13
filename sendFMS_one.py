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

from popbill import KakaoService, PopbillException, KakaoButton

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest

'''
단건의 친구톡 이미지를 전송합니다.
'''

try:
    print("=" * 15 + " 친구톡 이미지 단건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팝빌에 등록된 플러스 친구 아아디
    plusFriendID = "@팝빌"

    # 발신번호 (팝빌에 등록된 발신번호만 이용가능)
    snd = "010111222"

    # 친구톡 내용 (최대 400자)
    content = "친구톡 내용"

    # 대체문자 내용 (최대 2000byte)
    altContent = "대체문자 내용"

    # 대체문자 유형 [공백-미전송, C-알림톡내용, A-대체문자내용]
    altSendType = "A"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # 파일경로
    # 이미지 전송 규격 (전송포맷-JPG,JPEG / 용량제한-최대 500Kbte / 이미지 높이/너비 비율 : 1.333 이하, 1/2 이상)
    filePath = "test.jpg"

    # 이미지 링크 URL
    imageURL = "http://www.linkhub.co.kr"

    # 수신번호
    receiver = "01012345678"

    # 수신자 이름
    receiverName = "partner"

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
            n="메시지전달",
            t="MD",
        )
    )

    # 광고여부
    adsYN = False

    receiptNum = kakaoService.sendFMS(CorpNum, plusFriendID, snd, content, altContent,
                                      altSendType, sndDT, filePath, imageURL, receiver, receiverName,
                                      KakaoButtons, adsYN, UserID)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
