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
환불 가능한 포인트를 확인합니다. (보너스 포인트는 환불가능포인트에서 제외됩니다.)
- https://developers.popbill.com/reference/kakaotalk/python/api/point#GetRefundableBalance
"""

try:
    print("=" * 15 + " 환불 가능 포인트 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    refundableBalance = kakaoService.getRefundableBalance(CorpNum, UserID)

    print(" refundableBalance (환불 가능한 포인트) : %s" % refundableBalance)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
