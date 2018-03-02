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
플러스친구 계정관리 / 발신번호 관리 / 알림톡 템플릿관리 / 카카오톡전송내역 URL을 반환합니다.
 - 보안정책에 따라 반환된 URL은 30초의 유효시간을 갖습니다.
'''

try:
    print("=" * 15 + " 카카오 서비스 관련 팝업 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # PLUSFRIEND(플러스친구계정관리), SENDER(발신번호관리), TEMPLATE(알림톡템플릿관리), BOX(카카오톡전송내역)
    TOGO = "TEMPLATE"

    url = kakaoService.getURL(CorpNum, UserID, TOGO)

    print("URL : " + url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
