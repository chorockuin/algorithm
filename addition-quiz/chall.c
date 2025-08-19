// Name: chall.c
// Compile Option: gcc chall.c -o chall -fno-stack-protector

#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>

#define FLAG_SIZE 0x45   // 플래그 버퍼 크기(69바이트)

void alarm_handler() {
    puts("TIME OUT");    // 알람(타임아웃) 발생 시 출력
    exit(1);             // 프로그램 종료
}

void initialize() {
    // 표준입출력 버퍼링 비활성화: I/O 지연 줄이기
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    // SIGALRM(알람 시그널) 발생 시 처리할 핸들러 등록
    signal(SIGALRM, alarm_handler);
}

int main(void) {
    int fd;
    char *flag;

    initialize();          // 입출력 및 시그널 초기화
    srand(time(NULL));     // 현재 시각으로 난수 시드 설정

    // 플래그를 위한 동적 메모리 할당
    flag = (char *)malloc(FLAG_SIZE);

    // ./flag 파일 열고 내용 읽기
    fd = open("./flag", O_RDONLY);
    read(fd, flag, FLAG_SIZE);  // 주의: 널문자 보장 없음!
    close(fd);

    int num1 = 0;   // 첫 번째 피연산자
    int num2 = 0;   // 두 번째 피연산자
    int inpt = 0;   // 사용자 입력값

    // 총 50문제
    for (int i = 0; i < 50; i++){
        alarm(1);                       // 각 문제당 1초 타임아웃 설정
        num1 = rand() % 10000;          // 0~9999
        num2 = rand() % 10000;          // 0~9999
        printf("%d+%d=?\n", num1, num2);// 문제 출력
        scanf("%d", &inpt);             // 사용자 입력 받기

        if(inpt != num1 + num2){        // 틀리면 종료
            printf("Wrong...\n");
            return 0;
        }
    } 
    
    // 모두 맞으면 플래그 출력
    puts("Nice!");
    puts(flag);   // 주의: flag에 '\0'이 없으면 UB(정의되지 않은 동작)
                  // (보통 파일 끝에 개행 또는 널이 있어 운 좋게 출력되지만 안전하지 않음)

    return 0;
}
