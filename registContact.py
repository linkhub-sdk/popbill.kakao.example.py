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
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff
kakaoService.UseStaticIP = testValue.UseStaticIP
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
연동회원의 담당자를 신규로 등록합니다.
- https://docs.popbill.com/kakao/python/api#RegistContact
'''

try:
    print("=" * 15 + " 담당자 등록 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    newContact = ContactInfo(

        # 아이디 (6자 이상 50자 미만)
        id="popbill_test_id",

        # 비밀번호 (8자 이상 20자 미만)
        # 영문, 숫자, 특수문자 조합
        Password="password123!@#",

        # 담당자명 (최대 100자)
        personName="담당자명",

        # 담당자 연락처 (최대 20자)
        tel="010-111-222",

        # 담당자 휴대폰번호 (최대 20자)
        hp="010-111-222",

        # 담당자 팩스번호 (최대 20자)
        fax="070-111-222",

        # 담당자 이메일 (최대 100자)
        email="test@test.com",

        #담당자 조회권한, 1(개인) 2(읽기) 3(회사)
        searchRole=1
    )

    result = kakaoService.registContact(CorpNum, newContact, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
