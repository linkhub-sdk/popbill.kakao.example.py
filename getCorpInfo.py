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
연동회원의 회사정보를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/member#GetCorpInfo
"""

try:
    print("=" * 15 + " 회사정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    response = kakaoService.getCorpInfo(CorpNum)

    tmp = "ceoname(대표자성명) : " + response.ceoname + "\n"
    tmp += "corpName(상호) : " + response.corpName + "\n"
    tmp += "addr(주소) : " + response.addr + "\n"
    tmp += "bizType(업태) : " + response.bizType + "\n"
    tmp += "bizClass(종목) : " + response.bizClass + "\n"

    print(tmp)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
