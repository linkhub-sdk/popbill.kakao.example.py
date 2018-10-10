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

'''
알림톡/친구톡에 대한 전송내역을 확인 합니다.
'''

try:
    print("=" * 15 + " 알림톡/친구톡 전송결과 확인 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 알림톡/친구톡 전송 요청시 반환받은 접수번호
    receiptNum = "018022815501800001"

    response = kakaoService.getMessages(CorpNum, receiptNum)

    print("contentType (카카오톡 유형): %s " % response.contentType)
    print("templateCode (템플릿코드): %s " % response.templateCode)
    print("plusFriendID (플러스친구 아이디): %s " % response.plusFriendID)
    print("sendNum (발신번호): %s " % response.sendNum)
    print("altContent ([동보] 대체문자 내용): %s " % response.altContent)
    print("altSendType (대체문자 유형): %s " % response.sndDT)
    print("reserveDT (예약일시): %s " % response.reserveDT)
    print("adsYN (광고여부): %s " % response.adsYN)
    print("imageURL (친구톡 이미지 URL): %s " % response.imageURL)
    print("sendCnt (전송건수): %s " % response.sendCnt)
    print("successCnt (성공건수): %s " % response.successCnt)
    print("failCnt (실패건수): %s " % response.failCnt)
    print("altCnt (대체문자 건수): %s " % response.altCnt)
    print("cancelCnt (취소건수): %s " % response.cancelCnt)
    print("adsYN (광고전송 여부): %s " % response.adsYN)
    print("receiptNum (접수번호) : %s" % response.receiptNum)
    print("requestNum (요청번호) : %s" % response.requestNum)

    i = 1
    for info in response.btns:
        print("====== 버튼 [%d] ======" % i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print

    i = 1
    for info in response.msgs:
        print("====== 전송결과 정보 배열 [%d] ======" % i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
