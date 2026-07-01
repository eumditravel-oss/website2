import os

subpages = {
    "about_greeting.html": ("회사소개", "인사말", "0101_1.jpg"),
    "about_history.html": ("회사소개", "연혁", "0102_1.jpg"),
    "about_projects.html": ("회사소개", "주요실적", "0103_1.jpg"),
    "about_location.html": ("회사소개", "오시는길", "0104_1.jpg"),
    "business_01.html": ("업무분야", "안전진단", "0201_1.jpg"),
    "business_02.html": ("업무분야", "안전점검", "0202_1.jpg"),
    "business_03.html": ("업무분야", "건축물관리점검", "0203_1.jpg"),
    "business_04.html": ("업무분야", "건설공사 정기안전점검", "0204_1.jpg"),
    "business_05.html": ("업무분야", "내진성능평가", "0205_1.jpg"),
    "business_06.html": ("업무분야", "법원감정", "0206_1.jpg"),
    "business_07.html": ("업무분야", "인접건축물 사전조사", "0207_1.jpg"),
    "business_08.html": ("업무분야", "구조설계/감리", "0208_1.jpg"),
    "business_09.html": ("업무분야", "시설물보수/보강공사", "0209_1.jpg"),
    "cert_01.html": ("인증 및 장비현황", "인증현황", "0301_1.jpg"),
    "cert_02.html": ("인증 및 장비현황", "장비보유현황", "0302_1.jpg"),
    "notice.html": ("고객센터", "공지사항", "0401_1.jpg"),
    "inquiry.html": ("무료견적문의", "견적문의", "0402_1.jpg")
}

template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - (주)신영에스씨엠</title>
    <link rel="stylesheet" href="./css/style.css">
</head>
<body>
    <div id="hd" class="sticky">
        <div id="hd_wrapper">
            <div id="logo">
                <a href="index.html"><img src="http://sinyoungscm.com/img/logo.png" alt="로고"></a>
            </div>
            <nav id="gnb">
                <ul id="gnb_1dul">
                    <li class="gnb_1dli"><a href="about_greeting.html" class="gnb_1da">회사소개</a></li>
                    <li class="gnb_1dli"><a href="business_01.html" class="gnb_1da">업무분야</a></li>
                    <li class="gnb_1dli"><a href="cert_01.html" class="gnb_1da">인증 및 장비현황</a></li>
                    <li class="gnb_1dli"><a href="notice.html" class="gnb_1da">고객센터</a></li>
                    <li class="gnb_1dli"><a href="inquiry.html" class="gnb_1da">무료견적문의</a></li>
                </ul>
            </nav>
        </div>
    </div>

    <!-- 공통 상단 (Subtop) -->
    <div class="subtop">
        <div class="txt">
            <h2>{category}</h2>
            <h3>{title}</h3>
        </div>
    </div>

    <!-- 본문 레이아웃 -->
    <div class="container_wrap">
        <!-- LNB (좌측 그룹메뉴) -->
        <div id="aside">
            <section id="groupmenu">
                <div class="nanum-gb">{category}</div>
                <div id="nav1">
                    <ul>
                        <li class="on"><a href="#">{title}</a></li>
                    </ul>
                </div>
            </section>
        </div>

        <!-- 본문 Container -->
        <div id="container">
            <h2 id="container_title">{title}</h2>
            <div class="sub_wrap">
                <div class="img">
                    <img src="http://sinyoungscm.com/img/{img}" alt="{title}" onerror="this.src='http://sinyoungscm.com/img/main01.jpg'">
                </div>
                <div class="txt">
                    <h1>신뢰를 최우선으로 하는 안전진단 전문기관</h1>
                    <h2>(주)신영에스씨엠 - {title}</h2>
                    <p>저희는 최신 기술과 엄격한 안전진단 기준을 바탕으로 다양한 분야의 안전진단 서비스를 제공합니다.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div id="ft">
        <div class="container">
            <div id="ft_company">
                <p>
                    <b>(주)신영에스씨엠</b><br>
                    대표 : 이관배 | 사업자등록번호 : 212-81-91777 | E-mail : scm4700@naver.com<br>
                    서울사무실 : 서울특별시 성동구 성수일로4길 25 | TEL : 02-484-4700
                </p>
            </div>
            <div id="ft_copy">Copyright &copy; <b>(주)신영에스씨엠.</b> All rights reserved.</div>
        </div>
    </div>
    
    <!-- MR Script Ver 2.0 (실시간 문의 플로팅 위젯) -->
    <script async="true" src="//log1.toup.net/mirae_log_chat_common.js?adkey=plvbh" charset="UTF-8"></script>
    <script src="./js/main.js"></script>
</body>
</html>
"""

for filename, (category, title, img) in subpages.items():
    with open(f"f:/webpage2/{filename}", "w", encoding="utf-8") as f:
        f.write(template.format(category=category, title=title, img=img))

print("Successfully generated all 17 subpages.")
