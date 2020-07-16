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

from popbill import KakaoService, PopbillException, KakaoReceiver, KakaoButton

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff
kakaoService.UseStaticIP = testValue.UseStaticIP

'''
[동보전송] 알림톡 전송을 요청합니다.
- 사전에 승인된 템플릿의 내용과 알림톡 전송내용(content)이 다를 경우 전송실패 처리됩니다.
'''

try:
    print("=" * 15 + " 알림톡 동보 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 알림톡 템플릿 코드
    # 승인된 알림톡 템플릿 코드는 ListATStemplate API, GetATSTemplateMgtURL API, 혹은 팝빌사이트에서 확인이 가능합니다.
    templateCode = "019020000163"

    # 발신번호 (팝빌에 등록된 발신번호만 이용가능)
    snd = "07043042991"

    # 알림톡 내용 (최대 1000자)
    # 사전에 승인된 템플릿의 내용과 알림톡 전송내용(content)이 다를 경우 전송실패 처리됩니다.
    content = "[ 팝빌 ]\n"
    content += "신청하신 #{템플릿코드}에 대한 심사가 완료되어 승인 처리되었습니다.\n"
    content += "해당 템플릿으로 전송 가능합니다.\n\n"
    content += "문의사항 있으시면 파트너센터로 편하게 연락주시기 바랍니다.\n\n"
    content += "팝빌 파트너센터 : 1600-8536\n"
    content += "support@linkhub.co.kr"

    # [동보] 대체문자 내용 (최대 2000byte)
    altContent = "[테스트] 알림톡 대체 문자"

    # 대체문자 유형 [공백-미전송, C-알림톡내용, A-대체문자내용]
    altSendType = "A"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # [배열] 알림톡 전송정보 최대 1,000개 전송 가능
    KakaoMessages = []
    for x in range(0, 10):
        KakaoMessages.append(
            KakaoReceiver(
                rcv="010111222",  # 수신번호
                rcvnm="popbill"  # 수신자 이름
            )
        )

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    requestNum = ""

    # 알림톡 버튼정보를 템플릿 신청시 기재한 버튼정보와 동일하게 전송하는 경우 btns를 빈 배열로 처리.
    btns = []

    # 알림톡 버튼 URL에 #{템플릿변수}를 기재한경우 템플릿변수 값을 변경하여 버튼정보 구성
    # btns.append(
    #     KakaoButton(
    #         n="템플릿 안내",  # 버튼명
    #         t="WL",  # 버튼유형 [DS-배송조회, WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
    #         u1="https://www.popbill.com",  # [앱링크-iOS, 웹링크-Mobile]
    #         u2="http://www.popbill.com"  # [앱링크-Android, 웹링크-PC URL]
    #     )
    # )

    receiptNum = kakaoService.sendATS_same(CorpNum, templateCode, snd, content, altContent,
                                           altSendType, sndDT, KakaoMessages, UserID, requestNum, btns)
    print("접수번호 (receiptNum) : %s" % receiptNum)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
