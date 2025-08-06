# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

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
팝빌에 등록한 연동회원의 카카오톡 채널 목록을 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/channel#ListPlusFriendID
"""

try:
    print("=" * 15 + "  카카오톡 채널 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    response = kakaoService.listPlusFriendID(CorpNum)

    for info in response:
        print("plusFriendID (검색용 아이디) : %s" % info.plusFriendID)
        print("plusFriendName (채널명) : %s" % info.plusFriendName)
        print("regDT (등록일시) : %s" % info.regDT)
        print("state (채널상태) : %s" % info.state)
        print("stateDT (채널 상태 일시) : %s" % info.stateDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
