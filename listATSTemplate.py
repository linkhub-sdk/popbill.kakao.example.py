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
승인된 템플릿 목록을 확인 합니다.
- https://docs.popbill.com/kakao/python/api#ListATSTemplate
'''

try:
    print("=" * 15 + "알림톡 템플릿 목록 확인" + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = kakaoService.listATSTemplate(CorpNum, UserID)

    for info in response:
        print("\n============알림톡 템플릿 ============")
        print("templateCode (템플릿 코드) : %s" % info.templateCode)
        print("templateName (템플릿 제목) : %s" % info.templateName)
        print("plusFriendID (카카오톡 채널 검색용 아이디) : %s" % info.plusFriendID)
        print("template (템플릿 내용) : %s" % info.template)
        print("ads (광고 메시지) : %s " % info.ads)
        print("appendix (부가 메시지) : %s " % info.appendix)
        if info.btns is not None:
            for btns in info.btns:
                print("\n===btns ([배열]버튼 목록)===")
                print("n (버튼명) : %s" % btns.n)
                print("t (버튼유형) : %s" % btns.t)
                print("u1 (버튼링크1) : %s" % btns.u1)
                print("u2 (버튼링크2) : %s" % btns.u2)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
