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

from popbill import KakaoService, PopbillException

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
해당 사업자의 파트너 연동회원 가입여부를 확인합니다.
'''

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 사업자번호 ("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    result = kakaoService.checkIsMember(CorpNum)

    print("가입여부 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
