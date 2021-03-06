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
팝빌에 등록된 카카오톡 채널 목록을 반환 합니다.
- https://docs.popbill.com/kakao/python/api#ListPlusFriendID
'''

try:
    print("=" * 15 + "  카카오톡 채널 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = kakaoService.listPlusFriendID(CorpNum, UserID)

    for info in response:
        print("plusFriendID (카카오톡 채널 아이디) : %s" % info.plusFriendID)
        print("plusFriendName (카카오톡 채널 이름) : %s" % info.plusFriendName)
        print("regDT (등록일시) : %s" % info.regDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
