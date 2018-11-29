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
단건의 알림톡을 전송합니다.
'''

try:
    print("=" * 15 + " 알림톡 단건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 알림톡 템플릿코드
    # 승인된 알림톡 템플릿 코드는 ListATStemplate API, GetATSTemplateMgtURL API, 혹은 팝빌사이트에서 확인이 가능합니다.
    templateCode = "018020000002"

    # 발신번호 (팝빌에 등록된 발신번호만 이용가능)
    snd = "010111222"

    # 알림톡 내용 (최대 1000자)
    content = "테스트 템플릿 입니다."

    # 대체문자 내용 (최대 2000byte)
    altContent = "알림톡 대체 문자"

    # 대체문자 유형 [공백-미전송, C-알림톡내용, A-대체문자내용]
    altSendType = "A"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # 수신번호
    receiver = "01012341234"

    # 수신자 이름
    receiverName = "partner"

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    requestNum = ""

    receiptNum = kakaoService.sendATS(CorpNum, templateCode, snd, content, altContent,
                                      altSendType, sndDT, receiver, receiverName, UserID, requestNum)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
