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
연동회원의 담당자 정보를 수정합니다.
- https://docs.popbill.com/kakao/python/api#UpdateContact
'''

try:
    print("=" * 15 + " 담당자 정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    updateInfo = ContactInfo(

        # 담당자 아이디
        id=UserID,

        # 담당자 성명 (최대 100자)
        personName="담당자 성명",

        # 연락처 (최대 20자)
        tel="070-4304-2991",

        # 휴대폰번호 (최대 20자)
        hp="010-4324-4324",

        # 팩스번호 (최대 20자)
        fax="070-111-222",

        # 메일주소 (최대 100자)
        email="dev@linkhub.co.kr",

        ##담당자 조회권한, 1(개인) 2(읽기) 3(회사)
        searchRole=1
    )

    result = kakaoService.updateContact(CorpNum, updateInfo, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
