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
등록된 알림톡 템플릿의 정보를 확인합니다.
- https://docs.popbill.com/kakao/python/api#GetATSTemplate
'''

try:
    print("=" * 15 + " 템플릿 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    #템플릿 코드
    templateCode = "021010000076"

    templateInfo = kakaoService.getATSTemplate(CorpNum, templateCode, UserID)

    print("templateCode (응답코드) : %s " % templateInfo.templateCode)
    print("templateName (응답메시지) : %s " % templateInfo.templateName)
    print("template (검색결과 건수) : %s " % templateInfo.template)
    print("plusFriendID (페이지당 검색개수) : %s " % templateInfo.plusFriendID)

    for btns in templateInfo.btns:
        print("*" * 50)
        print("n (버튼명) : %s " % btns.n)
        print("t (버튼유형) : %s " % btns.t)
        print("u1 (버튼링크1) : %s " % btns.u1)
        print("u2 (버튼링크2) : %s " % btns.u2)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
