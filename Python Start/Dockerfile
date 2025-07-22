FROM python:3.12-alpine          # 3.12 버전의 Python이 설치된 가볍고 보안성이 높은 Alpine 리눅스 이미지를 기반으로 사용

ENV USER rootsquare              # 환경 변수 USER에 'rootsquare' 값을 설정 (추후 유저 생성에 사용)

USER root                        # 이후 RUN 명령어들을 root 권한으로 실행

RUN apk add socat                # socat 네트워크 유틸리티 설치 (원격 연결 수신 및 포트포워딩 용도)

RUN adduser -u 1337 -D -g "" $USER   # 1337 UID를 가진 'rootsquare'라는 새 사용자 계정 생성, 홈 디렉토리 없음(-D), 그룹명 없이 생성(-g "")

WORKDIR /chall                   # 작업 디렉토리(working directory)를 /chall로 지정

COPY chall.py .                  # 호스트의 chall.py 파일을 컨테이너의 /chall 디렉토리에 복사

COPY flag.txt .                  # 호스트의 flag.txt 파일을 컨테이너의 /chall 디렉토리에 복사

RUN chown $USER:$USER /chall/chall.py /chall/flag.txt   # chall.py와 flag.txt의 소유자를 'rootsquare' 유저로 변경

RUN chmod 0500 /chall/chall.py   # chall.py 실행 파일에 소유자만 읽기/실행 권한(0500) 부여, 다른 유저는 접근 불가

RUN chmod 0400 /chall/flag.txt   # flag.txt 파일에 소유자만 읽기 권한(0400) 부여, 다른 유저는 접근 불가

USER $USER                       # 이후 모든 명령을 'rootsquare' 유저 권한으로 실행 (보안 강화 목적)

EXPOSE 5000                      # 컨테이너 외부에 5000번 포트 개방(노출) 선언 (실제 포트포워딩은 docker run에서 설정)

CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:python3 chall.py,nofork,stderr"]
# socat을 실행하여 5000번 포트에서 TCP 연결을 받아올 때마다 python3 chall.py 실행
# 연결이 들어올 때마다(=fork) 새로운 python3 chall.py 프로세스가 실행됨
# 표준에러(stderr) 연결, nofork 옵션으로 exec 명령을 하나만 실행하도록 제한, 쉽게 말하면, 각 소켓 연결마다 프로세스가 하나씩 실행되고, 그 프로세스는 다시 fork하지 않는다는 의미.
