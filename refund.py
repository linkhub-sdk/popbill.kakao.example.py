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
from popbill import KakaoService, PopbillException, RefundForm

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff
kakaoService.UseStaticIP = testValue.UseStaticIP
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원 포인트를 환불 신청합니다.
- https://developers.popbill.com/reference/kakaotalk/python/api/point#Refund
"""

try:
    print("=" * 15 + " 환불 신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 환불 신청 객체 정보
    refundForm = RefundForm(
        # 담당자명
        ContactName="환불신청테스트",

        # 담당자 연락처
        tel="01077777777",

        # 환불 신청 포인트
        RequestPoint="10",

        # 은행명
        AccountBank="국민",

        # 계좌번호
        AccountNum="123123123-123",

        # 예금주명
        AccountName="예금주",

        # 환불사유
        Reason="테스트 환불 사유",
    )

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    response = kakaoService.refund(CorpNum, refundForm, UserID)

    print(" code (요청에 대한 응답 상태 코드) : %s" % response.code)
    print(" message (요청에 대한 응답 메시지) : %s" % response.message)
    print(" refundCode (환불코드) : %s" % response.refundCode)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
