# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import KakaoService, PopbillException

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff
kakaoService.UseStaticIP = testValue.UseStaticIP
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
파트너가 할당한 전송요청 번호를 통해 알림톡/친구톡 전송상태 및 결과를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/info#GetMessagesRN
"""

try:
    print("=" * 15 + " 알림톡/친구톡 전송결과 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 알림톡/친구톡 전송 요청시 할당한 전송요청번호(requestNum)
    requestNum = ""

    response = kakaoService.getMessagesRN(CorpNum, requestNum)

    print("contentType (카카오톡 유형): %s " % response.contentType)
    print("templateCode (템플릿 코드): %s " % response.templateCode)
    print("plusFriendID (검색용 아이디): %s " % response.plusFriendID)
    print("sendNum (발신번호): %s " % response.sendNum)
    print("altSubject (대체문자 제목): %s " % response.altSubject)
    print("altContent (대체문자 내용): %s " % response.altContent)
    print("altSendType (대체문자 유형): %s " % response.altSendType)
    print("reserveDT (예약일시): %s " % response.reserveDT)
    print("adsYN (광고여부): %s " % response.adsYN)
    print("imageURL (친구톡 이미지 URL): %s " % response.imageURL)
    print("sendCnt (전송건수): %s " % response.sendCnt)
    print("successCnt (성공건수): %s " % response.successCnt)
    print("failCnt (실패건수): %s " % response.failCnt)
    print("altCnt (대체문자 건수): %s " % response.altCnt)
    print("cancelCnt (취소건수): %s " % response.cancelCnt+ "\n")

    print("====== [배열] 버튼 목록 ======")
    if response.btns is not None:
        for info in response.btns:
            print("n (버튼명) : %s" % info.n)
            print("t (버튼유형) : %s" % info.t)
            print("u1 (버튼링크1) : %s" % info.u1)
            print("u2 (버튼링크2) : %s" % info.u2)
            print("tg (아웃링크) : %s" % info.tg + "\n")

    print("====== 전송결과 정보 배열 ======")
    for info in response.msgs:
        print("state (상태코드) : %s" % info.state)
        print("sendDT (전송일시) : %s" % info.sendDT)
        print("result (카카오 결과코드) : %s" % info.result)
        print("resultDT (전송결과 수신일시) : %s" % info.resultDT)
        print("contentType (카카오톡 유형): %s " % response.contentType)

        print("receiveNum (수신번호) : %s" % info.receiveNum)
        print("receiveName (수신자명) : %s" % info.receiveName)
        print("content (알림톡/친구톡 내용) : %s" % info.content)
        print("altSubject (대체문자 제목) : %s" % info.altSubject)
        print("altContent (대체문자 내용) : %s" % info.altContent)
        print("altContentType (대체문자 전송타입) : %s" % info.altContentType)
        print("altSendDT (대체문자 전송일시) : %s" % info.altSendDT)
        print("altResult (대체문자 통신사 결과코드) : %s" % info.altResult)
        print("altResultDT (대체문자 전송결과 수신일시) : %s" % info.altResultDT)
        print("receiptNum (접수번호) : %s" % info.receiptNum)
        print("requestNum (요청번호) : %s" % info.requestNum)
        print("interOPRefKey (파트너 지정키) : %s" % info.interOPRefKey + "\n")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
