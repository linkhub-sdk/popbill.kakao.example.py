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
알림톡 템플릿 목록을 확인 합니다.
'''

try:
    print("=" * 15 + "알림톡 템플릿 목록 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = kakaoService.listATSTemplate(CorpNum, UserID)

    i = 1
    for info in response:
        print("====== 알림톡 템플릿 목록 확인 [%d] ======" % i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print()


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))