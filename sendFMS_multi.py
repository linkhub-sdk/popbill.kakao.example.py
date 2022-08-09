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

from popbill import KakaoService, PopbillException, KakaoButton, KakaoReceiver

kakaoService = KakaoService(testValue.LinkID, testValue.SecretKey)
kakaoService.IsTest = testValue.IsTest
kakaoService.IPRestrictOnOff = testValue.IPRestrictOnOff
kakaoService.UseStaticIP = testValue.UseStaticIP
kakaoService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
이미지가 첨부된 다수건의 친구톡 전송을 팝빌에 접수하며, 수신자 별로 개별 내용을 전송합니다. (최대 1,000건)
- 친구톡의 경우 야간 전송은 제한됩니다. (20:00 ~ 익일 08:00)
- 전송실패시 사전에 지정한 변수 'altSendType' 값으로 대체문자를 전송할 수 있고, 이 경우 문자(SMS/LMS) 요금이 과금됩니다.
- 대체문자의 경우, 포토문자(MMS) 형식은 지원하고 있지 않습니다.
- https://docs.popbill.com/kakao/python/api#SendFMS_multi
'''

try:
    print("=" * 15 + " 친구톡 이미지 대량 전송 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팝빌에 등록된 카카오톡 채널 아아디
    plusFriendID = "@팝빌"

    # 팝빌에 사전 등록된 발신번호
    snd = ""

    # 대체문자 유형 (None , "C" , "A" 중 택 1)
    # None = 미전송, C = 알림톡과 동일 내용 전송 , A = 대체문자 내용(altContent)에 입력한 내용 전송
    altSendType = ""

    # 대체문자 제목
    # - 메시지 길이(90byte)에 따라 장문(LMS)인 경우에만 적용.
    # - 수신정보 배열에 대체문자 제목이 입력되지 않은 경우 적용.
    # - 모든 수신자에게 다른 제목을 보낼 경우 82번 라인에 있는 altsjt 를 이용.
    altSubject = "대체문자 제목"

    # 예약일시 (작성형식 : yyyyMMddHHmmss)
    sndDT = ""

    # 첨부이미지 파일 경로
    # 이미지 파일 규격: 전송 포맷 - JPG 파일 (.jpg, .jpeg), 용량 - 최대 500 Kbyte, 크기 - 가로 500px 이상, 가로 기준으로 세로 0.5 ~ 1.3배 비율 가능
    filePath = "test.jpg"

    # 이미지 링크 URL
    # └ 수신자가 친구톡 상단 이미지 클릭시 호출되는 URL
    # 미입력시 첨부된 이미지를 링크 기능 없이 표시
    # └ 수신자가 친구톡 상단 이미지 클릭시 호출되는 URL
    # 미입력시 첨부된 이미지를 링크 기능 없이 표시
    imageURL = "http://www.linkhub.co.kr"

    # 수신정보 배열, 최대 1,000건
    KakaoMessages = []
    for x in range(0, 10):
        KakaoMessages.append(
            KakaoReceiver(
                rcv="",  # 수신번호
                rcvnm="",  # 수신자 이름
                msg="안녕하세요 링크허브입니다.",  # 친구톡 내용 (최대 400자)
                
                # 대체문자 제목
                # - 메시지 길이(90byte)에 따라 장문(LMS)인 경우에만 적용.
                # - 모든 수신자에게 동일한 제목을 보낼 경우 배열의 모든 원소에 동일한 값을 입력하거나
                #   값을 입력하지 않고 53번 라인에 있는 altSubject 를 이용
                altsjt="(친구톡 대체문자 제목) [링크허브]"+str(x),
                
                # 대체문자 내용 (최대 2000byte)
                altmsg="(친구톡 대체문자) 안녕하세요 링크허브입니다.",
                interOPRefKey="20220803-"+str(x)    # 파트너 지정키, 수신자 구별용 메모
            )
        )

    # 버튼 목록 (최대 5개)
    KakaoButtons = []

    KakaoButtons.append(
        KakaoButton(
            n="팝빌 바로가기",  # 버튼명
            t="WL",  # 버튼유형 [DS-배송조회, WL-웹링크, AL-앱링크, MD-메시지전달, BK-봇키워드]
            u1="http://www.popbill.com",  # [앱링크-iOS, 웹링크-Mobile]
            u2="http://www.popbill.com"  # [앱링크-Android, 웹링크-PC URL]
        )
    )

    KakaoButtons.append(
        KakaoButton(
            n="메시지전달",
            t="MD",
        )
    )

    # 광고여부
    adsYN = False

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    requestNum = ""

    receiptNum = kakaoService.sendFMS_multi(CorpNum, plusFriendID, snd, "", "",
                                            altSendType, sndDT, filePath, imageURL, KakaoMessages,
                                            KakaoButtons, adsYN, UserID, requestNum, altSubject)
    print("접수번호 (receiptNum) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
