```c
void entry(void)                 // 프로그램의 진짜 엔트리 포인트(실행 진입 함수, 예: WinMainCRTStartup)
{
  __security_init_cookie();      // 스택 보호용 시큐리티 쿠키(버퍼 오버플로우 방지) 초기화
  FUN_1400013e8();               // 메인 초기화 및 실행 루틴 호출(앞서 분석한 CRT 초기화 포함)
  return;                        // 함수 종료(실제 이 함수는 main 반환값을 신경 안 씀)
}
```
위 코드는 CRT 코드임
뭘보고 아느냐? __security_init_cookie()와 같은 CRT 라이브러리 함수 이름들을 보고 알지

- CRT(C Run Time)
  - C/C++로 작성한 프로그램이 “진짜 실행”되려면, 운영체제에 따라 필수적으로 실행되는 코드들이 있는데 그것을 CRT라고 함

- CRT가 하는 일
  - 프로그램 실행 전 “준비 작업” (예: 글로벌/스태틱 변수 초기화, 보안 세팅, 환경변수 등)
  - 표준 입출력, 메모리 할당, 문자열 처리 등 C 표준 함수 제공(CRT 라이브러리라고 함)
  - exit, atexit, 예외 처리 등 종료 처리
  - main/WinMain 같은 진짜 “사용자 코드”를 “실제로 호출”해줌

- 윈도우 프로그램 실행 순서
  - 윈도우 커널 → (entry/CRT 스타트업) → CRT 라이브러리 초기화 → main/WinMain 호출 → (종료 시) CRT 종료 루틴 → 커널로 반환




```c
/* WARNING: Function: _guard_dispatch_icall replaced with injection: guard_dispatch_icall */

int FUN_1400013e8(void) // 프로그램 엔트리 함수(보통 main 실행 전 호출)
{
    bool bVar1;
    int iVar2;
    undefined8 uVar3;
    longlong *plVar4;
    ulonglong uVar5;
    undefined8 uVar6;
    undefined8 *puVar7;
    uint *puVar8;
    ulonglong uVar9;
    undefined8 unaff_RBX;
    undefined8 in_R9;

    iVar2 = (int)unaff_RBX; // RBX 값(아마 0) int로 변환해서 임시 저장
    uVar3 = __scrt_initialize_crt(1); // CRT(C 런타임) 초기화 시도
    if ((char)uVar3 == '\0') { // 초기화 실패 시
        __scrt_fastfail(7); // 치명적 예외로 프로그램 강제 종료
    }
    else {
        bVar1 = false; // 잠금 중복 여부 flag 초기화
        uVar3 = __scrt_acquire_startup_lock(); // 스타트업 락(초기화 중복 방지) 획득
        iVar2 = (int)CONCAT71((int7)((ulonglong)unaff_RBX >> 8),(char)uVar3); // iVar2 재설정 (락 정보 조합)
        if (DAT_1400035c0 != 1) { // 이미 CRT가 완전히 초기화됐는지 확인
            if (DAT_1400035c0 == 0) { // 아직 초기화 안 됨
                DAT_1400035c0 = 1; // 초기화 중으로 표시
                iVar2 = _initterm_e(&DAT_1400021e0,&DAT_1400021f8); // .CRT$XCA ~ .CRT$XCZ 함수 실행(에러 발생 시 중단)
                if (iVar2 != 0) { // 에러 발생 시
                    return 0xff; // 255 반환하고 종료
                }
                _initterm(&DAT_1400021c8,&DAT_1400021d8); // .CRT$XIA ~ .CRT$XIZ 함수 실행(일반 전역 객체 생성)
                DAT_1400035c0 = 2; // 초기화 완료 표시
            }
            else { // 이미 초기화 중이었다면
                bVar1 = true; // 중복 초기화 flag
            }
            __scrt_release_startup_lock((char)uVar3); // 스타트업 락 해제
            plVar4 = (longlong *)FUN_140001a44(); // TLS(스레드 로컬 저장소) cleanup 함수 포인터 가져오기
            if ((*plVar4 != 0) &&
                (uVar5 = __scrt_is_nonwritable_in_current_image((longlong)plVar4), (char)uVar5 != '\0')) {
                (*(code *)*plVar4)(0,2); // 함수 포인터가 유효하고, 현재 이미지에 비가변(nonwritable)이면 cleanup 콜백 호출
            }
            plVar4 = (longlong *)FUN_140001a4c(); // TLS(스레드 로컬) atexit 콜백 포인터 가져오기
            if ((*plVar4 != 0) &&
                (uVar5 = __scrt_is_nonwritable_in_current_image((longlong)plVar4), (char)uVar5 != '\0')) {
                _register_thread_local_exe_atexit_callback(*plVar4); // 스레드 종료 시 콜백 등록
            }
            uVar6 = _get_initial_narrow_environment(); // 초기 환경변수 영역 포인터 가져오기
            puVar7 = (undefined8 *)__p___argv(); // argv 배열 포인터 가져오기
            uVar3 = *puVar7; // argv 값
            puVar8 = (uint *)__p___argc(); // argc 포인터 가져오기
            uVar9 = (ulonglong)*puVar8; // argc 값
            iVar2 = FUN_140001100(uVar9,uVar3,uVar6,in_R9); // main 또는 WinMain 진입 함수 호출(실제 사용자 코드 실행)
            uVar5 = __scrt_is_managed_app(); // .NET managed 어플리케이션인지 확인
            if ((char)uVar5 != '\0') { // managed app인 경우
                if (!bVar1) {
                    _cexit(); // exit 루틴 실행(정상 종료)
                }
                __scrt_uninitialize_crt(CONCAT71((int7)(uVar9 >> 8),1),'\0'); // CRT 언인스톨/해제
                return iVar2; // 실제 main 함수의 반환값 리턴
            }
            goto LAB_140001554; // unmanaged면 바로 exit로 이동
        }
    }
    __scrt_fastfail(7); // 이도 저도 아니면 치명적 오류로 강제 종료
LAB_140001554:
    /* WARNING: Subroutine does not return */
    exit(iVar2); // main 함수 결과 코드로 프로세스 종료(이 줄은 반환하지 않음)
}
```
위 함수도 CRT 코드다. 실제 사용자가 작성한 함수는 FUN_140001100(uVar9,uVar3,uVar6,in_R9); 안에!

- 커널 함수
  - 운영체제(윈도우 NT 커널 등)에서 제공
  - 예: NtCreateFile, ZwReadFile, 시스템 콜 등
  - 커널 모드에서만 실행
  - 대부분 드라이버, 시스템 수준 프로그래밍에서 사용

- CRT 함수
  - 사용자 모드(유저 모드) 프로그램에서 실행
  - 표준 라이브러리 함수이거나, 런타임에서 제공하는 부트스트랩/초기화 함수
  - 프로그램의 메인/WinMain 호출, 환경설정, 종료처리 등 담당




```c

void FUN_140001100(undefined8 param_1, undefined8 param_2, undefined8 param_3, undefined8 param_4)
{
  bool bVar1;
  undefined7 extraout_var;  // 타입 알 수 없는 7비트짜리 변수
  longlong lVar2;
  char *pcVar3;
  undefined1 auStack_138 [32];        // (스택 보호 및 정렬용 더미 영역)
  char local_118 [256];               // 사용자 입력 저장 버퍼
  ulonglong local_18;                 // 스택 쿠키값 (보안 체크용)

  local_18 = DAT_140003008 ^ (ulonglong)auStack_138; // 스택 보호용 쿠키 세팅(전역값 XOR 스택주소)
  pcVar3 = local_118;                 // 입력 버퍼 포인터를 pcVar3에 대입
  for (lVar2 = 0x100; lVar2 != 0; lVar2 = lVar2 + -1) { // 256회 반복(버퍼 초기화)
    *pcVar3 = '\0';                   // 입력 버퍼를 0으로 초기화(널문자 채움)
    pcVar3 = pcVar3 + 1;              // 포인터 다음 위치로 이동
  }
  FUN_140001190("Input : ", param_2, param_3, param_4); // "Input : " 메시지 출력(추정)
  FUN_1400011f0("%256s", local_118, param_3, param_4);  // 사용자 입력을 local_118에 받아옴(256바이트 문자열 입력)
  bVar1 = FUN_140001000(local_118);    // 입력값(local_118)이 정답인지 판정하는 함수 호출
  if ((int)CONCAT71(extraout_var, bVar1) == 0) { // 정답이 아니면(7비트 타입(1바이트)과 1비트 타입을 이어붙여서, 8비트(1바이트)로 합치는 CONCAT71 매크로. 리버싱 과정에서 들어간 듯)
    puts("Wrong");                     // "Wrong" 메시지 출력
  }
  else {
    puts("Correct");                   // 정답이면 "Correct" 메시지 출력
  }
  __security_check_cookie(local_18 ^ (ulonglong)auStack_138); // 스택 보호 쿠키 체크(스택 오버플로우 감지)
  return;                              // 함수 종료
}
```



```c
int FUN_140001190(char *param_1, undefined8 param_2, undefined8 param_3, undefined8 param_4)
{
  int iVar1;
  FILE *_File;
  undefined8 local_res10;
  undefined8 local_res18;
  undefined8 local_res20;

  local_res10 = param_2;     // 가변 인자(param_2)를 지역 변수에 저장
  local_res18 = param_3;     // 가변 인자(param_3)를 지역 변수에 저장
  local_res20 = param_4;     // 가변 인자(param_4)를 지역 변수에 저장
  _File = (FILE *)__acrt_iob_func(1); // 표준 출력(FILE*) 핸들 가져오기(stdout, 1)
  iVar1 = _vfprintf_l(_File, param_1, (_locale_t)0x0, (va_list)&local_res10); 
  // 지역 변수(local_res10 주소부터 시작해서 local_res20까지겠지)에 담긴 인자를 va_list로 넘겨서
  // param_1 포맷 문자열을 _File(stdout)에 출력(로케일은 기본)
  return iVar1;              // 출력된 문자의 개수 반환
}
```



```c
int FUN_1400011f0(char *param_1, undefined8 param_2, undefined8 param_3, undefined8 param_4)
{
  int iVar1;
  FILE *_File;
  undefined8 local_res10;
  undefined8 local_res18;
  undefined8 local_res20;

  local_res10 = param_2;      // 가변 인자(param_2)를 지역 변수에 저장
  local_res18 = param_3;      // 가변 인자(param_3)를 지역 변수에 저장
  local_res20 = param_4;      // 가변 인자(param_4)를 지역 변수에 저장
  _File = (FILE *)__acrt_iob_func(0);  // 표준 입력(FILE*) 핸들 가져오기(stdin, 0)
  iVar1 = _vfprintf_l(_File, param_1, (_locale_t)0x0, (va_list)&local_res10);  
  // 포맷 문자열(param_1)과 인자들을 va_list로 묶어
  // 표준 입력(stdin)에 출력(로케일은 기본값)
  return iVar1;               // 출력된 문자의 개수 반환
}
```


```c
bool FUN_140001000(char *param_1)

{
  int iVar1;
  
  iVar1 = strcmp(param_1,"Compar3_the_str1ng");
  return iVar1 == 0;
}
```



```c

```