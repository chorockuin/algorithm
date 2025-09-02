<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>php7cmp4re</title>
</head>
<body>
    <!-- 상단 고정 네비게이션 바 -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">php7cmp4re</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">Index page</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
    <div class="container">
    <?php
    // 플래그 값을 포함하는 외부 파일 불러오기
    require_once('flag.php');
    // 에러 출력 억제
    error_reporting(0);

    // POST 요청만 처리
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
      // POST 값이 있으면 변수에 저장, 없으면 빈 문자열
      $input_1 = $_POST["input1"] ? $_POST["input1"] : "";
      $input_2 = $_POST["input2"] ? $_POST["input2"] : "";
      // 일부러 1초 지연
      sleep(1);

      // 두 입력이 모두 비어 있지 않은 경우
      if($input_1 != "" && $input_2 != ""){
        // input1 길이가 4 미만이어야 함
        if(strlen($input_1) < 4){
          // input1에 대한 문자열 비교 조건
          //  "8" 보다 작고
          //  "7.A" 보다 작으며
          //  "7.9" 보다 커야 함
          if($input_1 < "8" && $input_1 < "7.A" && $input_1 > "7.9"){
            // input2 길이가 2 이상 3 미만이어야 함 (즉, 길이=2)
            if(strlen($input_2) < 3 && strlen($input_2) > 1){
              // input2에 대한 비교 조건
              //   숫자 비교 시 74보다 작고
              //   문자열 비교 시 "74"보다 커야 함
              if($input_2 < 74 && $input_2 > "74"){
                // 모든 조건을 만족하면 FLAG 출력
                echo "</br></br></br><pre>FLAG\n";
                echo $flag;
                echo "</pre>";
              } else echo "<br><br><br><h4>Good try.</h4>";
            } else echo "<br><br><br><h4>Good try.</h4><br>";
          } else echo "<br><br><br><h4>Try again.</h4><br>";
        } else echo "<br><br><br><h4>Try again.</h4><br>";
      } else{
        // 입력값이 비어 있으면 안내 메시지 출력
        echo '<br><br><br><h4>Fill the input box.</h4>';
      }
    } else echo "<br><br><br><h3>WHat??!</h3>";
    ?> 
    </div> 
</body>
</html>
