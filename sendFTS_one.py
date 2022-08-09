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
텍스트로 구성된 1건의 친구톡 전송을 팝빌에 접수합니다.
- 친구톡의 경우 야간 전송은 제한됩니다. (20:00 ~ 익일 08:00)
- 전송실패시 사전에 지정한 변수 'altSendType' 값으로 대체문자를 전송할 수 있고, 이 경우 문자(SMS/LMS) 요금이 과금됩니다.
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

    # 팝빌에 사전 등록된 발신번호
    snd = ""

    # 친구톡 내용 (최대 1000자)
    content = "친구톡 내용 입니다."

    # 대체문자 제목
    # - 메시지 길이(90byte)에 따라 장문(LMS)인 경우에만 적용.
    altSubject = "대체문자 제목"

    # 대체문자 유형(altSendType)이 "A"일 경우, 대체문자로 전송할 내용 (최대 2000byte)
    # └ 팝빌이 메시지 길이에 따라 단문(90byte 이하) 또는 장문(90byte 초과)으로 전송처리
    altContent = "대체문자 내용"

    # 대체문자 유형 (null , "C" , "A" 중 택 1)
    # null = 미전송, C = 알림톡과 동일 내용 전송 , A = 대체문자 내용(altContent)에 입력한 내용 전송
    altSendType = ""

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
                                      receiver, receiverName, KakaoButtons, adsYN, UserID, requestNum, altSubject)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
