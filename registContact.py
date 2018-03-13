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

from popbill import KakaoService, PopbillException, ContactInfo

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest

'''
연동회원의 담당자를 신규로 등록합니다.
'''

try:
    print("=" * 15 + " 담당자 등록 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    newContact = ContactInfo(

        # 아이디
        id="kakao_test_id",

        # 비밀번호
        pwd="this_is_password",

        # 담당자명
        personName="김대리",

        # 연락처
        tel="010-1234-1234",

        # 휴대폰번호
        hp="010-1234-1234",

        # 팩스번호
        fax="070-0000-0509",

        # 메일주소
        email="test@test.co.kr",

        # 회사조회 권한여부, True(회사조회) False(개인조회)
        searchAllAllowYN=True
    )

    result = kakaoService.registContact(CorpNum, newContact, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
