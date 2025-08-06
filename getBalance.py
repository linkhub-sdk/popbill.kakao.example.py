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
연동회원의 잔여포인트를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/common-api/point#GetBalance
"""

try:
    print("=" * 15 + " 연동회원 잔여포인트 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    balance = kakaoService.getBalance(CorpNum)

    print("잔여포인트 : %d" % balance)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
