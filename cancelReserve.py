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
팝빌에서 반환받은 접수번호를 통해 예약접수된 카카오톡을 전송 취소합니다. (예약시간 10분 전까지 가능)
- https://developers.popbill.com/reference/kakaotalk/python/api/send#CancelReserve
"""

try:
    print("=" * 15 + " 알림톡/친구톡 예약전송취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 예약 알림톡/친구톡 전송요청시 발급받은 접수번호(receiptNum)
    receiptNum = "018030210070700001"

    result = kakaoService.cancelReserve(CorpNum, receiptNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
