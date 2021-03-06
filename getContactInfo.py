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
kakaoService.UseStaticIP = testValue.UseStaticIP
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
연동회원의 담당자 정보를 확인합니다.
- https://docs.popbill.com/kakao/python/api#GetContactInfo
'''

try:
    print("=" * 15 + " 담당자 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 아이디
    contactID = 'testkorea'

    contactInfo = kakaoService.getContactInfo(CorpNum, contactID, UserID)

    print("id (아이디) : %s " % contactInfo.id)
    print("personName (담당자 성명) : %s " % contactInfo.personName)
    print("tel (담당자 연락처(전화번호)) : %s " % contactInfo.tel)
    print("hp (담당자 휴대폰번호) : %s " % contactInfo.hp)
    print("fax (담당자 팩스번호) : %s " % contactInfo.fax)
    print("email (담당자 이메일) : %s " % contactInfo.email)
    print("regDT (등록일시) : %s " % contactInfo.regDT)
    print("searchRole (담당자 조회권한) : %s " % contactInfo.searchRole)
    print("mgrYN (관리자 여부) : %s " % contactInfo.mgrYN)
    print("state (계정상태) : %s " % contactInfo.state)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
