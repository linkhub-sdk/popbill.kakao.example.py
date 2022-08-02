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
검색조건에 해당하는 카카오톡 전송내역 목록을 조회합니다. (조회기간 단위 : 최대 2개월)
- 카카오톡 접수일시로부터 6개월 이내 접수건만 조회할 수 있습니다.
- https://docs.popbill.com/kakao/python/api#Search
'''
try:
    print("=" * 15 + " 알림톡/친구톡 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 최대 검색기간 : 6개월 이내
    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20220701"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20220731"

    # 전송상태 배열 ("0" , "1" , "2" , "3" , "4" , "5" 중 선택, 다중 선택 가능)
    # └ 0 = 전송대기 , 1 = 전송중 , 2 = 전송성공 , 3 = 대체문자 전송 , 4 = 전송실패 , 5 = 전송취소
    # - 미입력 시 전체조회
    State = ["0", "1", "2", "3", "4", "5"]

    # 검색대상 배열 ("ATS", "FTS", "FMS" 중 선택, 다중 선택 가능)
    # └ ATS = 알림톡 , FTS = 친구톡(텍스트) , FMS = 친구톡(이미지)
    # - 미입력 시 전체조회
    Item = ["ATS", "FTS", "FMS"]

    # 전송유형별 조회 (null , "0" , "1" 중 택 1)
    # └ null = 전체 , 0 = 즉시전송건 , 1 = 예약전송건
    # - 미입력 시 전체조회
    ReserveYN = "0"

    # 사용자권한별 조회 (true / false 중 택 1)
    # └ false = 접수한 카카오톡 전체 조회 (관리자권한)
    # └ true = 해당 담당자 계정으로 접수한 카카오톡만 조회 (개인권한)
    # 미입력시 기본값 false 처리
    SenderYN = "0"

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향 [D-내림차순, A-오름차순]
    Order = "D"

    response = kakaoService.search(CorpNum, SDate, EDate, State, Item, ReserveYN, SenderYN, Page, PerPage, Order,
                                   UserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s " % response.pageCount)

    print("========== 전송결과 정보 배열 ==========")
    for info in response.list:
        print("state (전송 상태코드) : %s" % info.state)
        print("sendDT (전송일시) : %s" % info.sendDT)
        print("result (전송결과 코드) : %s" % info.result)
        print("resultDT (전송결과 수신일시) : %s" % info.resultDT)
        print("contentType (카카오톡 유형) : %s" % info.contentType)
        print("receiveNum (수신번호) : %s" % info.receiveNum)
        print("receiveName (수신자명) : %s" % info.receiveName)
        print("content (알림톡/친구톡 내용) : %s" % info.content)
        print("altSubject (대체문자 제목) : %s" % info.altSubject)
        print("altContent (대체문자 내용) : %s" % info.altContent)
        print("altContentType (대체문자 전송타입) : %s" % info.altContentType)
        print("altSendDT (대체문자 전송일시) : %s" % info.altSendDT)
        print("altResult (대체문자 전송결과 코드) : %s" % info.altResult)
        print("altResultDT (대체문자 전송결과 수신일시) : %s" % info.altResultDT)
        print("receiptNum (접수번호) : %s" % info.receiptNum)
        print("requestNum (요청번호) : %s" % info.requestNum  + '\n')

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
