<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width"/>
<meta property="og:title" content="阿美語-法語萌典"/>
<meta property="og:description" content="阿美語-法語字典電子化 +1"/>
<meta property="og:image" content="https://raw.github.com/g0v/style-guide/master/logo/png/double-line/g0v-2line-white-s.png">
<meta property="og:url" content="http://ckhis.ck.tp.edu.tw/~ljm/amis-fr">
<title>阿美語-法語萌典</title>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.2.2/bootstrap.min.js"></script>
<script type="text/javascript">
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-54332820-1', 'auto');
  ga('send', 'pageview');
</script>
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.2.2/css/bootstrap.css">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h3>阿美語-法語字典OCR校對</h3>
    <h4>目前戰況：二校</span>
    <h4>進度：</h4>
    <div class="progress">
      <div class="bar" style="width: 80%;"></div>
      <span id="progress_text"></span>
    </div>
    <div class="man">
      <p>
        參戰說明：<br />
        請照著圖片顯示之文句輸入框框內<br />
        當圖片顯示的內容為空白、頁碼、索引、手寫等狀況時，請選擇「這是空白」的按鈕<br />
        手寫的字體不要打呦，謝謝。
      </p>
      <span id="manual-link"><a href="https://g0v.hackpad.com/ep/pad/static/0dhleAxPa9c">詳細說明書請按我</a></span>
      <span>特殊符號參考：&nbsp;&nbsp;&nbsp;&nbsp;é &nbsp; è &nbsp; ç &nbsp; à &nbsp; â &nbsp; ê &nbsp; î &nbsp; ô &nbsp; û &nbsp; ä &nbsp; ë &nbsp; ï &nbsp; ö &nbsp; ü</span>
    </div>
    <div width="100%">
      <input id="ans" class="form-control ans" type="text" name="ans" tabindex="1" placeholder="在此輸入"/>
    </div>
    <button id="submit" class="btn btn-primary submit" tabindex="2">　送出　</button>
    <button id="no-content" class="btn no-content btn-danger" tabindex="3">這是空白</button>
    <button id="unclear" class="btn btn-warning unclear" tabindex="-1" style="display: none;">圖片不清楚</button>
    <input id="ans-shadow" class="form-control ans-shadow" type="text" readonly="true" tabindex="-1" style="display: none"/>
    <div class="tip">神乎其技的快速鍵參考： Enter: 送出 / shift+Enter: 這是空白 / ctrl+Enter: 這答案沒錯</div>

    <h3>校對圖</h3>
    <div>
        <span class="cell-info"></span>
        <button id="confirm" class="btn btn-success confirm" tabindex="5566" style="display: none; margin-left: 43%">這答案沒錯</button>
    </div>
    <div class="cell-image"></div>

    <div style="height: 150px">&nbsp;</div>
</div>
<script src="cell.js"></script>
<link rel="stylesheet" href="cell.css">
</body>
</html>
