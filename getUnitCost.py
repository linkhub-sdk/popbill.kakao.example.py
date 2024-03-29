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
카카오톡 전송시 과금되는 포인트 단가를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/point#GetUnitCost
"""

try:
    print("=" * 15 + " 알림톡/친구톡 전송단가 확인 " + "=" * 15)

    # 팝빌회원 아이디("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 전송유형 [ATS(알림톡), FTS(친구톡 텍스트), FMS(친구톡 이미지)]
    MsgType = "ATS"

    unitCost = kakaoService.getUnitCost(CorpNum, MsgType)

    print(MsgType + " 전송단가 : %d" % unitCost)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
