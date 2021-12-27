# -*- coding: utf-8 -*-

"""
 팝빌 카카오톡 API Python SDK Example

 - Python SDK 연동환경 설정방법 안내 : https://docs.popbill.com/kakao/tutorial/python
 - 업데이트 일자 : 2021-12-27
 - 연동 기술지원 연락처 : 1600-9854
 - 연동 기술지원 이메일 : code@linkhubcorp.com

 <테스트 연동개발 준비사항>
 1) 28, 31번 라인에 선언된 링크아이디(LinkID)와 비밀키(SecretKey)를
    링크허브 가입시 메일로 발급받은 인증정보를 참조하여 변경합니다.
 2) 팝빌 개발용 사이트(test.popbill.com)에 연동회원으로 가입합니다.
 3) 발신번호 사전등록을 합니다. (등록방법은 사이트/API 두가지 방식이 있습니다.)
    - 1. 팝빌 사이트 로그인 > [문자/팩스] > [카카오톡] > [발신번호 사전등록] 메뉴에서 등록
    - 2. getSenderNumberMgtURL API를 통해 반환된 URL을 이용하여 발신번호 등록
 4) 카카오톡 채널 등록 및 알림톡 템플릿 신청을 합니다.
    1. 카카오톡 채널등록 (등록방법은 사이트/API 두가지 방식이 있습니다.)
     - 1. 팝빌 사이트 로그인 [문자/팩스] > [카카오톡] > [카카오톡 관리] > '카카오톡 채널 계정관리' 메뉴에서 등록
     - 2. GetPlusFriendMgtURL API 를 통해 반환된 URL을 이용하여 등록
    2. 알림톡 템플릿 신청 (등록방법은 사이트/API 두가지 방식이 있습니다.)
     - 1. 팝빌 사이트 로그인 [문자/팩스] > [카카오톡] > [카카오톡 관리] > '알림톡 템플릿 관리' 메뉴에서 등록
     - 2. GetATSTemplateMgtURL API 를 통해 반환된 URL을 이용하여 등록
"""

# 링크아이디
LinkID = 'TESTER'

# 비밀키
SecretKey = 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I='

# 연동환경 설정값, 개발용(True), 상업용(False)
IsTest = True

# 팝빌회원 사업자번호
testCorpNum = "1234567890"

# 팝빌회원 팝빌 아아디
testUserID = "testkorea"

# 발급토큰 IP 제한기능 활성화 여부 (권장-True)
IPRestrictOnOff = True

# 팝빌 API 서비스 고정 IP 사용여부, true-사용, false-미사용, 기본값(false)
UseStaticIP = False

#로컬시스템 사용여부, 권장(True)
UseLocalTimeYN = True
