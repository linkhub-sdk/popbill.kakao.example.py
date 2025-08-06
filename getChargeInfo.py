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
팝빌 카카오톡 API 서비스 과금정보를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/common-api/point#GetChargeInfo
"""

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 전송유형 [ATS(알림톡), FTS(친구톡 텍스트), FMS(친구톡 이미지)]
    MsgType = "ATS"

    response = kakaoService.getChargeInfo(CorpNum, MsgType)

    print(" unitCost (전송단가) : %s" % response.unitCost)
    print(" chargeMethod (과금유형) : %s" % response.chargeMethod)
    print(" rateSystem (과금제도) : %s" % response.rateSystem)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
