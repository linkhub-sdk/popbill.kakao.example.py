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
파트너가 할당한 전송 요청번호로 접수 건을 식별하여 수신번호에 예약된 카카오톡을 전송 취소합니다. (예약시간 10분 전까지 가능)
- https://developers.popbill.com/reference/kakaotalk/python/api/send#CancelReserveRNbyRCV
"""

try:
    print("=" * 15 + " 예약전송 일부 취소 (전송 요청번호) " + "=" * 15)

    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 카카오톡 예약전송 접수시 파트너가 할당한 전송 요청번호
    requestNum = "20230111_ats_23"

    # 카카오톡 예약전송 접수시 팝빌로 요청한 수신번호
    receiveNum = "01022223333"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = kakaoService.CancelReserveRNbyRCV(CorpNum, requestNum, receiveNum, UserID)

    print("처리결과 : [%d] %s" % (response.code, response.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
