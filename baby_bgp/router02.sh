#!/bin/bash  # Bash 셸로 실행됨

# eth0 네트워크 인터페이스에서 IP 주소를 추출 (예: 192.168.0.3)
IP_ADDR=$(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)

# 추출한 IP 주소를 '.' 기준으로 배열(ADDR)로 분해
IFS='.' read -ra ADDR <<< "$IP_ADDR"

# 마지막 옥텟(예: 192.168.0.3의 3)을 -1하여 이웃 IP 계산
let "ADDR[3]-=1"

# 만약 마지막 옥텟이 음수가 되면(예: 0 - 1 = -1), 255로 설정 (오버플로 방지)
if [ ${ADDR[3]} -lt 0 ]; then
    ADDR[3]=255
fi

# 최종 이웃(Neighbor) IP 주소 생성
NEIGHBOR_IP="${ADDR[0]}.${ADDR[1]}.${ADDR[2]}.${ADDR[3]}"

# BIRD 설정 파일을 생성하여 /etc/bird/bird.conf에 저장
cat > /etc/bird/bird.conf <<EOF
log syslog all;  # 모든 로그를 syslog로 기록

router id $IP_ADDR;  # 이 컨테이너의 라우터 ID 설정

protocol bgp dreamhack {
    local as 65002;  # 이 컨테이너의 AS 번호
    source address $IP_ADDR;  # BGP 패킷 송신 시 사용할 IP
    graceful restart on;  # 연결 복구 중에도 라우팅 정보를 유지
    neighbor $NEIGHBOR_IP as 65001;  # 피어 라우터의 IP 및 AS 설정
    import all;  # 모든 경로를 수신
    export all;  # 모든 경로를 광고
}

protocol kernel {
        scan time 60;  # 60초마다 커널 라우팅 테이블 스캔
        import none;   # 커널 라우팅 테이블에서 경로 불러오지 않음
#       export all;   # 주석 처리됨: 커널 라우팅 테이블로 경로 내보내기 기능
}

protocol device {
        scan time 60;  # 60초마다 네트워크 디바이스 상태 확인
}

EOF

# BIRD 라우팅 데몬 실행 (-d: 디버그 모드로 포그라운드 실행, 로그 확인 가능)
bird -c /etc/b
