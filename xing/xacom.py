# 에러코드 메시지
def parseErrorCode(szTrCode):
    szTrCode = str(szTrCode)
    ht = {
        "-1" : "통신소켓 생성에 실패하였습니다",
        "-2" : "서버접속에 실패하였습니다",
        "-3" : "서버주소가 틀렸습니다",
        "-4" : "서버 접속시간이 초과되었습니다",
        "-5" : "이미 서버에 연결중입니다",
        "-6" : "해당TR은 사용할수 없습니다",
        "-7" : "로그인을 해야 사용이 가능합니다",
        "-8" : "시세전용에서는 사용이 불가능합니다",
        "-9" : "해당 계좌번호를 가지고 있지 않습니다",
        "-10" : "패킷의 크기가 잘못되었습니다",
        "-11" : "Data의 크기가 다릅니다",
        "-12" : "계좌가 존재하지 않습니다",
        "-13" : "Request ID 부족",
        "-14" : "소켓이 생성되지 않았습니다",
        "-15" : "암호화 생성에 실패했습니다",
        "-16" : "데이터 전송에 실패했습니다",
        "-17" : "암호화(RTN)처리에 실패했습니다",            
        "-18" : "공인인증 파일이 없습니다",
        "-19" : "공인인증 Function이 없습니다",
        "-20" : "메모리가 충분하지 않습니다",
        "-21" : "TR의 시간당 전송제한에 걸렸습니다",
        "-22" : "해당 TR은 해당 함수를 이용할 수 없습니다",
        "-23" : "로그인이 안되었거나, TR에 대한 정보를 찾을 수 없습니다",
        "-24" : "계좌위치가 지정되지 않았습니다",
        "-25" : "계좌를 가지고 있지 않습니다",
        "-26" : "파일 읽기에 실패했습니다 (종목 검색 조회 시, 파일이 없는 경우)",
        "0000" : "정상완료되었습니다",
        "00310" : "모의투자 조회가 완료되었습니다",
        "00136" : "조회가 완료되었습니다",
        "00020" : "application program exit[TR:CSPAQ]",
        "03669" : "비밀번호 오류입니다. (5회중 4회 남았습니다)",
        "01796" : "비밀번호 연속 오류허용횟수를 초과하였습니다. 콜센터로 문의하시기 바랍니다"
    }
    return ht[szTrCode] + " (%s)" % szTrCode if szTrCode in ht else szTrCode

# 요청 전문 제목 맵핑
def parseTR(szTrCode):
    ht = {
        "t0424" : "주식잔고",
        "t0425" : "주식체결/미체결",
        "t8407" : "멀티현재가조회",
        "t8412" : "주식챠트(N분)",
        "t8413" : "주식챠트(일주월)",
        "t8430" : "주식종목조회",
        "t1833" : "종목검색(씽API용)",
        "t1101" : "주식현재가호가조회",
        "t1102" : "주식현재가(시세)조회",
        "t1411" : "증거금율별종목조회",
        "t1702" : "외인기관종목별동향",
        "t1301" : "주식시간대별체결조회",
        "t0167" : "서버시간조회",
        "t9945" : "주식마스터조회API용",
        "CSPAQ12200" : "현물계좌예수금 주문가능금액 총평가 조회",
        "CSPAT00600" : "현물주문",
        "CSPAT00700" : "현물정정주문",
        "CSPAT00800" : "현물취소주문",
        "CSPBQ00200" : "현물계좌 증거금률별 주문가능 수량 조회",
        "HA_" : "KOSDAQ호가잔량",
        "H1_" : "KOSPI호가잔량",
        "SC0" : "주식주문접수",
        "SC1" : "주식주문체결",
        "SC2" : "주식주문정정",
        "SC3" : "주식주문취소",
        "SC4" : "주식주문거부"
    }
    return ht[szTrCode] if szTrCode in ht else ""