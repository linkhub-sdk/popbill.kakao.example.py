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
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff
kakaoService.UseStaticIP = testValue.UseStaticIP
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
친구톡(텍스트) 전송을 요청합니다.
- 친구톡은 심야 전송(20:00~08:00)이 제한됩니다.
- https://docs.popbill.com/kakao/python/api#SendFTS_one
'''

try:
    print("=" * 15 + " 친구톡 텍스트 단건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팝빌에 등록된 카카오톡 채널 아아디
    plusFriendID = "@팝빌"

    # 발신번호 (팝빌에 등록된 발신번호만 이용가능)
    snd = "07043042992"

    # 친구톡 내용 (최대 1000자)
    content = "친구톡 내용 입니다."

    # 대체문자 내용 (최대 2000byte)
    altContent = "대체문자 내용"

    # 대체문자 유형 [공백-미전송, C-친구톡내용, A-대체문자내용]
    altSendType = "A"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # 수신번호
    receiver = "010000111"

    # 수신자 이름
    receiverName = "partner"

    # 버튼 목록 (최대 5개)
    KakaoButtons = []

    KakaoButtons.append(
        KakaoButton(
            n="팝빌 바로가기",  # 버튼명
            t="WL",  # 버튼유형 [DS-배송조회, WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
            u1="http://www.popbill.com",  # [앱링크-iOS, 웹링크-Mobile]
            u2="http://www.popbill.com"  # [앱링크-Android, 웹링크-PC URL]
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

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    requestNum = ""

    receiptNum = kakaoService.sendFTS(CorpNum, plusFriendID, snd, content, altContent, altSendType, sndDT,
                                      receiver, receiverName, KakaoButtons, adsYN, UserID, requestNum)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
