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
승인된 알림톡 템플릿의 정보를 확인합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/template#GetATSTemplate
"""

try:
    print("=" * 15 + " 템플릿 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 템플릿 코드
    templateCode = "022040000374"

    templateInfo = kakaoService.getATSTemplate(CorpNum, templateCode)

    print("templateCode (템플릿 코드) : %s " % templateInfo.templateCode)
    print("templateName (템플릿 제목) : %s " % templateInfo.templateName)
    print("template (템플릿 내용) : %s " % templateInfo.template)
    print("plusFriendID (검색용 아이디) : %s " % templateInfo.plusFriendID)
    print("ads (광고 메시지) : %s " % templateInfo.ads)
    print("appendix (부가 메시지) : %s " % templateInfo.appendix)
    print("secureYN (보안템플릿 여부) : %s" % templateInfo.secureYN)
    print("state (템플릿 상태) : %s" % templateInfo.state)
    print("stateDT (템플릿 상태 일시) : %s" % templateInfo.stateDT)

    if templateInfo.btns is not None:
        for btns in templateInfo.btns:
            print("*" * 50)
            print("n (버튼명) : %s " % btns.n)
            print("t (버튼유형) : %s " % btns.t)
            print("u1 (버튼링크1) : %s " % btns.u1)
            print("u2 (버튼링크2) : %s " % btns.u2)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
