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
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
승인된 템플릿의 내용을 작성하여 다수건의 알림톡 전송을 팝빌에 접수하며, 수신자 별로 개별 내용을 전송합니다. (최대 1,000건)
- 사전에 승인된 템플릿의 내용과 알림톡 전송내용(content)이 다를 경우 전송실패 처리됩니다.
- 전송실패시 사전에 지정한 변수 'altSendType' 값으로 대체문자를 전송할 수 있고, 이 경우 문자(SMS/LMS) 요금이 과금됩니다.
- https://docs.popbill.com/kakao/python/api#SendATS_multi
'''

try:
    print("=" * 15 + " 알림톡 대량 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 승인된 알림톡 템플릿코드
    # └ 알림톡 템플릿 관리 팝업 URL(GetATSTemplateMgtURL API) 함수, 알림톡 템플릿 목록 확인(ListATStemplate API) 함수를 호출하거나
    #   팝빌사이트에서 승인된 알림톡 템플릿 코드를  확인 가능.
    templateCode = "022070000338"

    # 알림톡 내용 (최대 1000자)
    # 사전에 승인된 템플릿의 내용과 알림톡 전송내용(content)이 다를 경우 전송실패 처리됩니다.
    content = "[ 팝빌 ]\n"
    content += "신청하신 #{템플릿코드}에 대한 심사가 완료되어 승인 처리되었습니다.\n"
    content += "해당 템플릿으로 전송 가능합니다.\n\n"
    content += "문의사항 있으시면 파트너센터로 편하게 연락주시기 바랍니다.\n\n"
    content += "팝빌 파트너센터 : 1600-8536\n"
    content += "support@linkhub.co.kr"

    # 팝빌에 사전 등록된 발신번호
    snd = ""

    # 대체문자 유형 (null , "C" , "A" 중 택 1)
    # null = 미전송, C = 알림톡과 동일 내용 전송 , A = 대체문자 내용(altContent)에 입력한 내용 전송
    altSendType = "C"

    # 대체문자 제목
    # - 메시지 길이(90byte)에 따라 장문(LMS)인 경우에만 적용.
    # - 수신정보 배열에 대체문자 제목이 입력되지 않은 경우 적용.
    # - 모든 수신자에게 다른 제목을 보낼 경우 81번 라인에 있는 altsjt 를 이용.
    altSubject = "대체문자 제목"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # 수신정보 배열, 최대 1000건
    KakaoMessages = []
    for x in range(0, 2):
        KakaoMessages.append(
            KakaoReceiver(
                rcv="",  # 수신번호
                rcvnm="linkhub",  # 수신자 이름
                msg=content,  # 알림톡 내용 (최대 400자)
                
                # 대체문자 제목
                # - 메시지 길이(90byte)에 따라 장문(LMS)인 경우에만 적용.
                # - 모든 수신자에게 동일한 제목을 보낼 경우 배열의 모든 원소에 동일한 값을 입력하거나
                #   값을 입력하지 않고 63번 라인에 있는 altSubject 를 이용
                altsjt="(알림톡 대체문자 제목) [링크허브]"+str(x),
                
                # 대체문자 내용 (최대 2000byte)
                altmsg="(알림톡 대체문자) 안녕하세요 링크허브입니다.",
                interOPRefKey="20220803-"+str(x)    # 파트너 지정키, 수신자 구별용 메모

            )
        )

        # 수신자별 개별 버튼내용 전송하는 경우
        # 개별 버튼의 개수는 템플릿 신청 시 승인받은 버튼의 개수와 동일하게 생성, 다를 경우 전송실패 처리
        # 버튼링크URL에 #{템플릿변수}를 기재하여 승인받은 경우 URL 수정가능.
        # 버튼명 , 버튼 유형 수정 불가능.

        # #개별 버튼정보 리스트 생성
        # btns = []
        # # # 수신자별 개별 전송할 버튼 정보
        # btns.append(
        #     KakaoButton(
        #         n="템플릿 안내",  # 버튼명
        #         t="WL",  # 버튼유형 [DS-배송조회, WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
        #         u1="https://www.popbill.com",  # [앱링크-iOS, 웹링크-Mobile]
        #         u2="http://www.popbill.com"  # [앱링크-Android, 웹링크-PC URL]
        #     )
        # )
        # btns.append(
        #     KakaoButton(
        #         n="버튼명",  # 버튼명
        #         t="WL",  # 버튼유형 [DS-배송조회, WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
        #         u1="https://www.popbill" + str(x) + ".com",  # [앱링크-iOS, 웹링크-Mobile]
        #         u2="https://www.popbill" + str(x) + ".com"  # [앱링크-Android, 웹링크-PC URL]
        #     )
        # )
        # # 개별 버튼정보 리스트 수신정보에 추가
        # KakaoMessages[x].btns = btns

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    requestNum = ""

    # 동일 버튼정보 리스트, 수신자별 동일 버튼내용 전송하는경우
    # 버튼링크URL에 #{템플릿변수}를 기재하여 승인받은 경우 URL 수정가능.
    # 버튼의 개수는 템플릿 신청 시 승인받은 버튼의 개수와 동일하게 생성, 다를 경우 전송실패 처리
    # 알림톡 버튼정보를 템플릿 신청시 기재한 버튼정보와 동일하게 전송하는 경우 btns를 빈 리스트 처리.
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

    receiptNum = kakaoService.sendATS_multi(CorpNum, templateCode, snd, "", "",
                                            altSendType, sndDT, KakaoMessages, UserID, requestNum, btns, altSubject)
    print("접수번호 (receiptNum) : %s" % receiptNum)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
