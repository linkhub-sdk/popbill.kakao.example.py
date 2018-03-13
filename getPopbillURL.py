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

'''
팝빌 관련 팝업 URL을 반환합니다. (팝빌 로그인, 연동회원 포인트충전)
- 보안정책에 따라 반환된 URL은 30초의 유효시간을 갖습니다.
'''

try:
    print("=" * 15 + " 팝빌 관련 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # LOGIN-팝빌 로그인, CHRG-연동회원 포인트충전
    TOGO = "CHRG"

    url = kakaoService.getPopbillURL(CorpNum, UserID, TOGO)

    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
