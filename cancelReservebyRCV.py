# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

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
사용하고자 하는 아이디의 중복여부를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/send#CancelReservebyRCV
"""

try:
    print("=" * 15 + " 회원아이디 중복확인 " + "=" * 15)

    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 카카오톡 예약전송 접수시 팝빌로부터 반환 받은 접수번호
    ReceiptNum = ""

    # 카카오톡 예약전송 접수시 팝빌로 요청한 수신번호
    ReceiveNum = ""

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = kakaoService.CancelReservebyRCV(CorpNum, ReceiptNum, ReceiveNum, UserID)

    print("처리결과 : [%d] %s" % (response.code, response.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
