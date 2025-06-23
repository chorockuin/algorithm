from scapy.all import *  # Scapy는 패킷을 생성, 조작, 전송, 캡처할 수 있는 강력한 네트워크 도구입니다.
import netifaces as ni   # netifaces는 시스템의 네트워크 인터페이스 정보(IP, MAC 등)를 가져오는 데 사용됩니다.

# 주어진 네트워크 인터페이스(기본값: 'eth0')의 IPv4 주소를 반환하는 함수
def get_internal_ip(interface='eth0'):
    ni.ifaddresses(interface)  # 지정된 인터페이스의 주소 정보를 미리 로딩 (필수 아님, 단순 호출 가능)
    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']  # IPv4(AF_INET) 주소 정보 중 첫 번째 항목에서 'addr' 추출
    return ip  # 예: '192.168.0.2'

# 자신의 IP 주소를 기반으로 이웃 IP 주소를 계산하는 함수
# 마지막 옥텟을 +1하여 가상의 "이웃" 주소로 설정 (예: 192.168.0.2 → 192.168.0.3)
def calculate_neighbor_ip(own_ip):
    ip_parts = own_ip.split('.')  # IP 주소를 '.' 단위로 나누어 리스트로 변환
    ip_parts[3] = str((int(ip_parts[3]) + 1) % 256)  # 마지막 숫자(옥텟)를 정수로 바꾼 후 1 증가, 256 넘어가면 0으로 순환
    return '.'.join(ip_parts)  # 수정된 리스트를 다시 문자열 IP로 결합하여 반환

# 현재 머신의 eth0 인터페이스에 설정된 IPv4 주소를 가져옴
own_ip = get_internal_ip('eth0')

# 위에서 얻은 own_ip를 바탕으로 가상의 이웃 IP 주소 계산
neighbor_ip = calculate_neighbor_ip(own_ip)

# 전송 대상 정보 설정: 이웃 IP와 BGP가 사용하는 기본 포트 179
target_host = neighbor_ip  # 목적지 IP 주소
target_port = 179          # BGP는 TCP 포트 179번을 사용

# 실제로 전송할 데이터: DreamHack CTF 스타일의 가짜 플래그 문자열 (예시)
flag = "DH{fakeflagfakeflagfakeflagfakeflagfakeflagfakeflag}"

# IP 헤더 구성: 목적지 IP만 지정 (출발지는 시스템이 자동 설정함)
ip = IP(dst=target_host)

# TCP 헤더 구성:
# - sport: 출발지 포트 (무작위 짧은 포트)
# - dport: 목적지 포트 (BGP = 179)
# - flags="S": SYN 패킷 (TCP 연결 시작 신호)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# 비정상적인 SYN 패킷 구성:
# - 일반적인 SYN 패킷은 페이로드(데이터)를 포함하지 않음
# - 하지만 여기서는 Raw 데이터를 TCP 세그먼트에 실어서 전송함 → 이는 의도적으로 잘못된 사용
malformed_syn = ip / tcp / Raw(load=flag)

# 위에서 구성한 비정상 SYN 패킷을 실제 네트워크로 전송
# - send()는 L3(IP) 계층에서 전송
# - 보통 이 작업은 루트(root) 권한이 필요함
send(malformed_syn)
