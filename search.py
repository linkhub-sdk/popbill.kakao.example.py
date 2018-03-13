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

try:
    print("=" * 15 + " 알림톡/친구톡 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호("-"제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20180227"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20180228"

    # 전송상태 배열 [0-대기, 1-전송중, 2-성공, 3-대체 4-실패, 5-취소]
    State = ["0", "1", "2", "3", "4", "5"]

    # 전송유형 [ATS(알림톡) / ATS(친구톡 텍스트) / FMS(친구톡 이미지)]
    Item = ["ATS", "ATS", "FMS"]

    # 예약전송 검색여부, [공백-전체조회, 0-즉시전송조회, 1-예약전송조회]
    ReserveYN = "0"

    # 개인조회여부 [0-전체조회, 1-개인조회]
    SenderYN = "0"

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향 [D-내림차순, A-오름차순]
    Order = "D"

    response = kakaoService.search(CorpNum, SDate, EDate, State, Item, ReserveYN, SenderYN, Page, PerPage, Order, UserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s " % response.pageCount)
    print()

    i = 1
    for info in response.list:
        print("====== 전송내역 [%d] ======" % i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print()

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
