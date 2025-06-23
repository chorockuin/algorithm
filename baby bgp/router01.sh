#!/bin/bash  # 이 스크립트는 bash 셸에서 실행됨

# eth0 인터페이스에서 IP 주소를 추출 (예: 192.168.0.2)
IP_ADDR=$(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)

# IP 주소를 점(.)을 기준으로 배열로 나눔
IFS='.' read -ra ADDR <<< "$IP_ADDR"

# 마지막 옥텟을 +1하여 BGP 이웃(Neighbor) IP를 계산
# 예: 현재 IP가 192.168.0.2면 이웃 IP는 192.168.0.3
let "ADDR[3]+=1"
NEIGHBOR_IP="${ADDR[0]}.${ADDR[1]}.${ADDR[2]}.${ADDR[3]}"

# BIRD 라우팅 데몬 설정 파일 작성
cat > /etc/bird/bird.conf <<EOF # 아래에서 EOF까지의 내용을 cat으로 출력한 뒤, bird.conf에 저장 
log syslog all;  # 모든 로그를 syslog로 기록

router id $IP_ADDR;  # BIRD 라우터 ID 설정 (보통 로컬 IP 사용)

protocol bgp dreamhack {
    local as 65001;  # 로컬 AS 번호 (자율 시스템 번호)
    source address $IP_ADDR;  # BGP 패킷 송신 주소
    graceful restart on;  # BGP 연결 복구 중 라우팅 정보 유지
    neighbor $NEIGHBOR_IP as 65002;  # 피어(이웃)의 IP 및 AS 번호
    import all;  # 상대방의 모든 경로 수신
    export all;  # 자신의 모든 경로 광고
}

protocol kernel {
        scan time 60;  # 60초마다 커널 라우팅 테이블을 스캔
        import none;   # 커널 라우팅 테이블에서 경로 불러오지 않음
#       export all;   # 커널 라우팅 테이블에 경로 반영 (현재는 비활성화)
}

protocol device {
        scan time 60;  # 디바이스 상태를 60초마다 확인
}

EOF

# BIRD 데몬 실행, 설정 파일 경로 지정
bird -c /etc/bird/bird.conf &

# 5초마다 send.py 실행 (패킷 송신 또는 상태 확인 용도일 가능성)
while true; do
    python3 /send.py
    sleep 5
done
