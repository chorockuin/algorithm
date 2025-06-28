```bash
file chall

chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7cbc60d6b591837f08c1570ca2eee3ab3d22a3e9, for GNU/Linux 3.2.0, not stripped
```

ELF 64-bit LSB pie executable
    ELF: Executable and Linkable Format의 약자로, 리눅스에서 실행 파일과 공유 라이브러리 등에 쓰이는 바이너리 포맷입니다.
    64-bit: 64비트 시스템용으로 컴파일된 파일입니다. 이는 CPU가 64비트 명령어 집합을 지원해야 실행할 수 있다는 뜻입니다.
    LSB (Little Endian): 데이터를 메모리에 저장할 때 하위 바이트부터 먼저 저장하는 형식입니다. x86 및 x86-64는 모두 Little Endian입니다.
        예를 들어서 0x1234 값을 메모리 주소 0x00부터 저장한다고 하자. 상위 바이트: 0x12, 하위 바이트: 0x34
        Little Endian: 끝이 작다? = 끝의 주소 값이 작다 = 끝의 값(0x34)의 주소 값이 작다.(0x00) = 0x00: 0x34, 0x01: 0x12 = 계산 편함
        Big Endian: 끝이 크다? = 끝의 주소 값이 크다 = 끝의 값(0x34)의 주소 값이 크다.(0x01) = 0x00: 0x12, 0x01: 0x34 = 보기 편함
    PIE (Position Independent Executable):
    주소 독립 실행 파일입니다. 즉, 메모리 어느 위치에 로드되어도 실행될 수 있도록 만들어졌습니다.
    PIE 파일은 보안 기능인 ASLR (Address Space Layout Randomization)을 사용할 수 있게 해줍니다.
    일반 실행 파일은 고정 주소에 로드되지만, PIE는 매번 다른 위치에 로드될 수 있어 익스플로잇을 어렵게 만듭니다
        mov rax, 0x601040    ; 절대 주소(절대 주소라고 하지만 가상 메모리 주소 내의 절대 주소임. 실제 물리 메모리 주소는 매번 고정일 수가 없음) 접근
        lea rax, [rip + offset]  ; Load Effective Address, Register Instruction Pointer(현재 실행 중인 명령어의 주소를 담고 있는 레지스터), offset은 컴파일러나 링커가 계산해줌
x86-64
    이 실행 파일은 x86-64 (AMD64) 아키텍처용입니다. 즉, 64비트 Intel 또는 AMD CPU에서 동작합니다.
    i386이나 i686은 32비트 아키텍처를 의미합니다. x86-64는 64비트 확장판입니다.

version 1 (SYSV)
    ELF 포맷의 ABI(Application Binary Interface) 버전입니다.
    SYSV는 System V ABI를 따른다는 뜻으로, 대부분의 리눅스 시스템은 이 표준을 따릅니다.
    특별한 목적이 아닌 이상, 대부분 ELF 실행 파일은 이 ABI를 사용합니다.

dynamically linked
    실행 파일이 정적 링크가 아닌 동적 링크로 컴파일되었음을 의미합니다.
    즉, 이 파일은 실행 시점에 외부 공유 라이브러리 (.so 파일들)를 불러와서 사용합니다.
    대표적으로 libc.so.6, libm.so.6, ld-linux.so.2 등 리눅스 시스템 라이브러리들이 여기에 포함됩니다.
    정적 링크된 실행 파일은 모든 라이브러리를 내부에 포함하고 있어서 외부 의존성이 적지만, 크기가 큽니다.

interpreter /lib64/ld-linux-x86-64.so.2
    동적 로딩을 담당하는 인터프리터(런타임 링커)의 경로입니다.
    이 파일은 실행 시 공유 라이브러리를 메모리에 로드하고, 실제 실행을 시작하기 위한 준비를 합니다.
    ld-linux-x86-64.so.2는 일반적으로 glibc에 포함된 프로그램입니다.
    PIE든 아니든 동적 링크된 ELF 파일은 이 인터프리터를 통해 실행됩니다.

BuildID[sha1]=7cbc60d6b591837f08c1570ca2eee3ab3d22a3e9
    Build ID는 빌드 시 생성된 고유한 식별자로, 디버깅이나 크래시 리포트 분석에 사용됩니다.
    sha1 해시 기반으로 생성됩니다.
    GDB나 debuginfod와 같은 도구에서 빌드 ID를 이용해 디버깅 심볼(.debug 파일)을 자동으로 찾아줄 수 있습니다.
    리눅스 배포판에서는 /usr/lib/debug/.build-id/ 경로에서 BuildID 기반 디버깅 파일을 찾습니다.

for GNU/Linux 3.2.0
    이 실행 파일이 최소한 리눅스 커널 3.2.0 버전 이상에서 실행되도록 빌드되었음을 의미합니다.
    커널의 uname -r이 이보다 낮다면 실행되지 않을 수도 있습니다.
    일반적으로 glibc 버전이 사용하는 커널 기능에 따라 이 값이 정해집니다.

not stripped
    디버깅 심볼(함수 이름, 변수 이름, 라인 정보 등)이 제거되지 않았다는 의미입니다.
    stripped는 디버깅 정보를 제거해서 파일 크기를 줄이고 보안을 높입니다.
    not stripped인 파일은 리버싱할 때 함수 이름, 디버깅 정보 등을 활용할 수 있어서 분석이 훨씬 수월합니다.
    strip 명령어를 사용하면 stripped 상태로 만들 수 있습니다.

```bash
sudo apt install gdb binutils ltrace strace
```

```bash
readelf -h chall          # ELF 헤더 확인

ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Position-Independent Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x11a0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14544 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         13
  Size of section headers:           64 (bytes)
  Number of section headers:         31
  Section header string table index: 30
```
프로그램 헤더 (Program Header Table): 13개
운영체제가 ELF 파일을 실행할 때 사용하는 정보.(실제 데이터 정보는 그냥 바이너리 덩어리임)
각 항목은 세그먼트(Segment)를 설명함.
세그먼트는 메모리 매핑 단위임.
실행 가능한 코드, 초기화된 데이터, 동적 링킹 정보 등을 메모리에 어떻게 배치할지 알려줌.

섹션 헤더 (Section Header Table): 31개
링커/디버거/컴파일러가 사용하는 헤더 정보.(실제 데이터 정보는 그냥 바이너리 덩어리임)
각 항목은 섹션(Section)을 설명함.
섹션은 컴파일 산출물 단위로, 코드/데이터/디버그 정보 등으로 나뉨.
디버깅이나 분석을 위한 심볼 정보, 디버그 정보, 문자열 테이블 등을 포함함.
컴파일, 링킹, 디버깅 시(static time)에 사용됨

섹션 헤더 문자열 테이블의 인덱스: 30
섹션의 표현 이름들(.text, .data, .bss)이 저장되어 있는 테이블
섹션 헤더 내에 위치하고, 위치한 인덱스 번호

```bash
readelf -l chall          # 메모리 로딩 관련 정보 확인 (Program Header)

Elf file type is DYN (Position-Independent Executable file)
Entry point 0x11a0
There are 13 program headers, starting at offset 64

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
                 
  PHDR           0x0000000000000040 0x0000000000000040 0x0000000000000040
                 0x00000000000002d8 0x00000000000002d8  R      0x8
  INTERP         0x0000000000000318 0x0000000000000318 0x0000000000000318
                 0x000000000000001c 0x000000000000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x00000000000008f0 0x00000000000008f0  R      0x1000
  LOAD           0x0000000000001000 0x0000000000001000 0x0000000000001000
                 0x00000000000004dd 0x00000000000004dd  R E    0x1000
  LOAD           0x0000000000002000 0x0000000000002000 0x0000000000002000
                 0x000000000000019c 0x000000000000019c  R      0x1000
  LOAD           0x0000000000002d68 0x0000000000003d68 0x0000000000003d68
                 0x00000000000002a8 0x00000000000002c8  RW     0x1000
  DYNAMIC        0x0000000000002d78 0x0000000000003d78 0x0000000000003d78
                 0x00000000000001f0 0x00000000000001f0  RW     0x8
  NOTE           0x0000000000000338 0x0000000000000338 0x0000000000000338
                 0x0000000000000030 0x0000000000000030  R      0x8
  NOTE           0x0000000000000368 0x0000000000000368 0x0000000000000368
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_PROPERTY   0x0000000000000338 0x0000000000000338 0x0000000000000338
                 0x0000000000000030 0x0000000000000030  R      0x8
  GNU_EH_FRAME   0x0000000000002068 0x0000000000002068 0x0000000000002068
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x10
  GNU_RELRO      0x0000000000002d68 0x0000000000003d68 0x0000000000003d68
                 0x0000000000000298 0x0000000000000298  R      0x1

 Section to Segment mapping:
  Segment Sections...
   00
   01     .interp
   02     .interp .note.gnu.property .note.gnu.build-id .note.ABI-tag .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt
   03     .init .plt .plt.got .plt.sec .text .fini
   04     .rodata .eh_frame_hdr .eh_frame
   05     .init_array .fini_array .dynamic .got .data .bss
   06     .dynamic
   07     .note.gnu.property
   08     .note.gnu.build-id .note.ABI-tag
   09     .note.gnu.property
   10     .eh_frame_hdr
   11
   12     .init_array .fini_array .dynamic .got
```

```bash
readelf -S chall          # 섹션 리스트 확인

There are 31 section headers, starting at offset 0x38d0:

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000000318  00000318
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.gnu.pr[...] NOTE             0000000000000338  00000338
       0000000000000030  0000000000000000   A       0     0     8
  [ 3] .note.gnu.bu[...] NOTE             0000000000000368  00000368
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .note.ABI-tag     NOTE             000000000000038c  0000038c
       0000000000000020  0000000000000000   A       0     0     4
  [ 5] .gnu.hash         GNU_HASH         00000000000003b0  000003b0
       0000000000000030  0000000000000000   A       6     0     8
  [ 6] .dynsym           DYNSYM           00000000000003e0  000003e0
       00000000000001c8  0000000000000018   A       7     1     8
  [ 7] .dynstr           STRTAB           00000000000005a8  000005a8
       00000000000000e7  0000000000000000   A       0     0     1
  [ 8] .gnu.version      VERSYM           0000000000000690  00000690
       0000000000000026  0000000000000002   A       6     0     2
  [ 9] .gnu.version_r    VERNEED          00000000000006b8  000006b8
       0000000000000040  0000000000000000   A       7     1     8
  [10] .rela.dyn         RELA             00000000000006f8  000006f8
       00000000000000f0  0000000000000018   A       6     0     8
  [11] .rela.plt         RELA             00000000000007e8  000007e8
       0000000000000108  0000000000000018  AI       6    24     8
  [12] .init             PROGBITS         0000000000001000  00001000
       000000000000001b  0000000000000000  AX       0     0     4
  [13] .plt              PROGBITS         0000000000001020  00001020
       00000000000000c0  0000000000000010  AX       0     0     16
  [14] .plt.got          PROGBITS         00000000000010e0  000010e0
       0000000000000010  0000000000000010  AX       0     0     16
  [15] .plt.sec          PROGBITS         00000000000010f0  000010f0
       00000000000000b0  0000000000000010  AX       0     0     16
  [16] .text             PROGBITS         00000000000011a0  000011a0
       0000000000000330  0000000000000000  AX       0     0     16
  [17] .fini             PROGBITS         00000000000014d0  000014d0
       000000000000000d  0000000000000000  AX       0     0     4
  [18] .rodata           PROGBITS         0000000000002000  00002000
       0000000000000065  0000000000000000   A       0     0     4
  [19] .eh_frame_hdr     PROGBITS         0000000000002068  00002068
       0000000000000044  0000000000000000   A       0     0     4
  [20] .eh_frame         PROGBITS         00000000000020b0  000020b0
       00000000000000ec  0000000000000000   A       0     0     8
  [21] .init_array       INIT_ARRAY       0000000000003d68  00002d68
       0000000000000008  0000000000000008  WA       0     0     8
  [22] .fini_array       FINI_ARRAY       0000000000003d70  00002d70
       0000000000000008  0000000000000008  WA       0     0     8
  [23] .dynamic          DYNAMIC          0000000000003d78  00002d78
       00000000000001f0  0000000000000010  WA       7     0     8
  [24] .got              PROGBITS         0000000000003f68  00002f68
       0000000000000098  0000000000000008  WA       0     0     8
  [25] .data             PROGBITS         0000000000004000  00003000
       0000000000000010  0000000000000000  WA       0     0     8
  [26] .bss              NOBITS           0000000000004010  00003010
       0000000000000020  0000000000000000  WA       0     0     16
  [27] .comment          PROGBITS         0000000000000000  00003010
       000000000000002b  0000000000000001  MS       0     0     1
  [28] .symtab           SYMTAB           0000000000000000  00003040
       00000000000004b0  0000000000000018          29    18     8
  [29] .strtab           STRTAB           0000000000000000  000034f0
       00000000000002c5  0000000000000000           0     0     1
  [30] .shstrtab         STRTAB           0000000000000000  000037b5
       000000000000011a  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  D (mbind), l (large), p (processor specific)
```

```bash
readelf -s chall          # 모든 심볼 확인

Symbol table '.dynsym' contains 19 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND _[...]@GLIBC_2.34 (2)
     2: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterT[...]
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (3)
     4: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (3)
     5: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (3)
     6: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND close@GLIBC_2.2.5 (3)
     7: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND read@GLIBC_2.2.5 (3)
     8: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (3)
     9: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    10: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (3)
    11: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (3)
    12: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND open@GLIBC_2.2.5 (3)
    13: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __[...]@GLIBC_2.7 (4)
    14: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.2.5 (3)
    15: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMC[...]
    16: 0000000000004010     8 OBJECT  GLOBAL DEFAULT   26 [...]@GLIBC_2.2.5 (3)
    17: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND [...]@GLIBC_2.2.5 (3)
    18: 0000000000004020     8 OBJECT  GLOBAL DEFAULT   26 stdin@GLIBC_2.2.5 (3)

Symbol table '.symtab' contains 50 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS Scrt1.o
     2: 000000000000038c    32 OBJECT  LOCAL  DEFAULT    4 __abi_tag
     3: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
     4: 00000000000011d0     0 FUNC    LOCAL  DEFAULT   16 deregister_tm_clones
     5: 0000000000001200     0 FUNC    LOCAL  DEFAULT   16 register_tm_clones
     6: 0000000000001240     0 FUNC    LOCAL  DEFAULT   16 __do_global_dtors_aux
     7: 0000000000004028     1 OBJECT  LOCAL  DEFAULT   26 completed.0
     8: 0000000000003d70     0 OBJECT  LOCAL  DEFAULT   22 __do_global_dtor[...]
     9: 0000000000001280     0 FUNC    LOCAL  DEFAULT   16 frame_dummy
    10: 0000000000003d68     0 OBJECT  LOCAL  DEFAULT   21 __frame_dummy_in[...]
    11: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS chall.c
    12: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    13: 0000000000002198     0 OBJECT  LOCAL  DEFAULT   20 __FRAME_END__
    14: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS
    15: 0000000000003d78     0 OBJECT  LOCAL  DEFAULT   23 _DYNAMIC
    16: 0000000000002068     0 NOTYPE  LOCAL  DEFAULT   19 __GNU_EH_FRAME_HDR
    17: 0000000000003f68     0 OBJECT  LOCAL  DEFAULT   24 _GLOBAL_OFFSET_TABLE_
    18: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_mai[...]
    19: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterT[...]
    20: 0000000000004010     8 OBJECT  GLOBAL DEFAULT   26 stdout@GLIBC_2.2.5
    21: 0000000000004000     0 NOTYPE  WEAK   DEFAULT   25 data_start
    22: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5
    23: 0000000000004020     8 OBJECT  GLOBAL DEFAULT   26 stdin@GLIBC_2.2.5
    24: 0000000000004010     0 NOTYPE  GLOBAL DEFAULT   25 _edata
    25: 00000000000014d0     0 FUNC    GLOBAL HIDDEN    17 _fini
    26: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.2.5
    27: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND snprintf@GLIBC_2.2.5
    28: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND close@GLIBC_2.2.5
    29: 0000000000001289    71 FUNC    GLOBAL DEFAULT   16 initialize
    30: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND read@GLIBC_2.2.5
    31: 0000000000004000     0 NOTYPE  GLOBAL DEFAULT   25 __data_start
    32: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strcmp@GLIBC_2.2.5
    33: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    34: 0000000000004008     0 OBJECT  GLOBAL HIDDEN    25 __dso_handle
    35: 0000000000002000     4 OBJECT  GLOBAL DEFAULT   18 _IO_stdin_used
    36: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND malloc@GLIBC_2.2.5
    37: 0000000000004030     0 NOTYPE  GLOBAL DEFAULT   26 _end
    38: 00000000000011a0    38 FUNC    GLOBAL DEFAULT   16 _start
    39: 0000000000004010     0 NOTYPE  GLOBAL DEFAULT   26 __bss_start
    40: 00000000000012d0   111 FUNC    GLOBAL DEFAULT   16 get_rand_num
    41: 000000000000133f   401 FUNC    GLOBAL DEFAULT   16 main
    42: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND setvbuf@GLIBC_2.2.5
    43: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND open@GLIBC_2.2.5
    44: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __isoc99_scanf@G[...]
    45: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.2.5
    46: 0000000000004010     0 OBJECT  GLOBAL HIDDEN    25 __TMC_END__
    47: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMC[...]
    48: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@G[...]
    49: 0000000000001000     0 FUNC    GLOBAL HIDDEN    12 _init
```

```bash
readelf -x .text chall    # .text 섹션의 기계어 코드 확인
readelf -d chall          # 동적 라이브러리 정보 확인
readelf -e chall          # 전체 요약 확인
```

```bash
objdump -d chall

chall:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:       f3 0f 1e fa             endbr64
    1004:       48 83 ec 08             sub    $0x8,%rsp
    1008:       48 8b 05 d9 2f 00 00    mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__@Base>
    100f:       48 85 c0                test   %rax,%rax
    1012:       74 02                   je     1016 <_init+0x16>
    1014:       ff d0                   call   *%rax
    1016:       48 83 c4 08             add    $0x8,%rsp
    101a:       c3                      ret

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 4a 2f 00 00       push   0x2f4a(%rip)        # 3f70 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:       f2 ff 25 4b 2f 00 00    bnd jmp *0x2f4b(%rip)        # 3f78 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:       0f 1f 00                nopl   (%rax)
    1030:       f3 0f 1e fa             endbr64
    1034:       68 00 00 00 00          push   $0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmp 1020 <_init+0x20>
    103f:       90                      nop
    1040:       f3 0f 1e fa             endbr64
    1044:       68 01 00 00 00          push   $0x1
    1049:       f2 e9 d1 ff ff ff       bnd jmp 1020 <_init+0x20>
    104f:       90                      nop
    1050:       f3 0f 1e fa             endbr64
    1054:       68 02 00 00 00          push   $0x2
    1059:       f2 e9 c1 ff ff ff       bnd jmp 1020 <_init+0x20>
    105f:       90                      nop
    1060:       f3 0f 1e fa             endbr64
    1064:       68 03 00 00 00          push   $0x3
    1069:       f2 e9 b1 ff ff ff       bnd jmp 1020 <_init+0x20>
    106f:       90                      nop
    1070:       f3 0f 1e fa             endbr64
    1074:       68 04 00 00 00          push   $0x4
    1079:       f2 e9 a1 ff ff ff       bnd jmp 1020 <_init+0x20>
    107f:       90                      nop
    1080:       f3 0f 1e fa             endbr64
    1084:       68 05 00 00 00          push   $0x5
    1089:       f2 e9 91 ff ff ff       bnd jmp 1020 <_init+0x20>
    108f:       90                      nop
    1090:       f3 0f 1e fa             endbr64
    1094:       68 06 00 00 00          push   $0x6
    1099:       f2 e9 81 ff ff ff       bnd jmp 1020 <_init+0x20>
    109f:       90                      nop
    10a0:       f3 0f 1e fa             endbr64
    10a4:       68 07 00 00 00          push   $0x7
    10a9:       f2 e9 71 ff ff ff       bnd jmp 1020 <_init+0x20>
    10af:       90                      nop
    10b0:       f3 0f 1e fa             endbr64
    10b4:       68 08 00 00 00          push   $0x8
    10b9:       f2 e9 61 ff ff ff       bnd jmp 1020 <_init+0x20>
    10bf:       90                      nop
    10c0:       f3 0f 1e fa             endbr64
    10c4:       68 09 00 00 00          push   $0x9
    10c9:       f2 e9 51 ff ff ff       bnd jmp 1020 <_init+0x20>
    10cf:       90                      nop
    10d0:       f3 0f 1e fa             endbr64
    10d4:       68 0a 00 00 00          push   $0xa
    10d9:       f2 e9 41 ff ff ff       bnd jmp 1020 <_init+0x20>
    10df:       90                      nop

Disassembly of section .plt.got:

00000000000010e0 <__cxa_finalize@plt>:
    10e0:       f3 0f 1e fa             endbr64
    10e4:       f2 ff 25 0d 2f 00 00    bnd jmp *0x2f0d(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    10eb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

00000000000010f0 <puts@plt>:
    10f0:       f3 0f 1e fa             endbr64
    10f4:       f2 ff 25 85 2e 00 00    bnd jmp *0x2e85(%rip)        # 3f80 <puts@GLIBC_2.2.5>
    10fb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001100 <printf@plt>:
    1100:       f3 0f 1e fa             endbr64
    1104:       f2 ff 25 7d 2e 00 00    bnd jmp *0x2e7d(%rip)        # 3f88 <printf@GLIBC_2.2.5>
    110b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001110 <snprintf@plt>:
    1110:       f3 0f 1e fa             endbr64
    1114:       f2 ff 25 75 2e 00 00    bnd jmp *0x2e75(%rip)        # 3f90 <snprintf@GLIBC_2.2.5>
    111b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001120 <close@plt>:
    1120:       f3 0f 1e fa             endbr64
    1124:       f2 ff 25 6d 2e 00 00    bnd jmp *0x2e6d(%rip)        # 3f98 <close@GLIBC_2.2.5>
    112b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001130 <read@plt>:
    1130:       f3 0f 1e fa             endbr64
    1134:       f2 ff 25 65 2e 00 00    bnd jmp *0x2e65(%rip)        # 3fa0 <read@GLIBC_2.2.5>
    113b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001140 <strcmp@plt>:
    1140:       f3 0f 1e fa             endbr64
    1144:       f2 ff 25 5d 2e 00 00    bnd jmp *0x2e5d(%rip)        # 3fa8 <strcmp@GLIBC_2.2.5>
    114b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001150 <malloc@plt>:
    1150:       f3 0f 1e fa             endbr64
    1154:       f2 ff 25 55 2e 00 00    bnd jmp *0x2e55(%rip)        # 3fb0 <malloc@GLIBC_2.2.5>
    115b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001160 <setvbuf@plt>:
    1160:       f3 0f 1e fa             endbr64
    1164:       f2 ff 25 4d 2e 00 00    bnd jmp *0x2e4d(%rip)        # 3fb8 <setvbuf@GLIBC_2.2.5>
    116b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001170 <open@plt>:
    1170:       f3 0f 1e fa             endbr64
    1174:       f2 ff 25 45 2e 00 00    bnd jmp *0x2e45(%rip)        # 3fc0 <open@GLIBC_2.2.5>
    117b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001180 <__isoc99_scanf@plt>:
    1180:       f3 0f 1e fa             endbr64
    1184:       f2 ff 25 3d 2e 00 00    bnd jmp *0x2e3d(%rip)        # 3fc8 <__isoc99_scanf@GLIBC_2.7>
    118b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001190 <exit@plt>:
    1190:       f3 0f 1e fa             endbr64
    1194:       f2 ff 25 35 2e 00 00    bnd jmp *0x2e35(%rip)        # 3fd0 <exit@GLIBC_2.2.5>
    119b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

00000000000011a0 <_start>:
    11a0:       f3 0f 1e fa             endbr64
    11a4:       31 ed                   xor    %ebp,%ebp
    11a6:       49 89 d1                mov    %rdx,%r9
    11a9:       5e                      pop    %rsi
    11aa:       48 89 e2                mov    %rsp,%rdx
    11ad:       48 83 e4 f0             and    $0xfffffffffffffff0,%rsp
    11b1:       50                      push   %rax
    11b2:       54                      push   %rsp
    11b3:       45 31 c0                xor    %r8d,%r8d
    11b6:       31 c9                   xor    %ecx,%ecx
    11b8:       48 8d 3d 80 01 00 00    lea    0x180(%rip),%rdi        # 133f <main>
    11bf:       ff 15 13 2e 00 00       call   *0x2e13(%rip)        # 3fd8 <__libc_start_main@GLIBC_2.34>
    11c5:       f4                      hlt
    11c6:       66 2e 0f 1f 84 00 00    cs nopw 0x0(%rax,%rax,1)
    11cd:       00 00 00

00000000000011d0 <deregister_tm_clones>:
    11d0:       48 8d 3d 39 2e 00 00    lea    0x2e39(%rip),%rdi        # 4010 <stdout@GLIBC_2.2.5>
    11d7:       48 8d 05 32 2e 00 00    lea    0x2e32(%rip),%rax        # 4010 <stdout@GLIBC_2.2.5>
    11de:       48 39 f8                cmp    %rdi,%rax
    11e1:       74 15                   je     11f8 <deregister_tm_clones+0x28>
    11e3:       48 8b 05 f6 2d 00 00    mov    0x2df6(%rip),%rax        # 3fe0 <_ITM_deregisterTMCloneTable@Base>
    11ea:       48 85 c0                test   %rax,%rax
    11ed:       74 09                   je     11f8 <deregister_tm_clones+0x28>
    11ef:       ff e0                   jmp    *%rax
    11f1:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    11f8:       c3                      ret
    11f9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001200 <register_tm_clones>:
    1200:       48 8d 3d 09 2e 00 00    lea    0x2e09(%rip),%rdi        # 4010 <stdout@GLIBC_2.2.5>
    1207:       48 8d 35 02 2e 00 00    lea    0x2e02(%rip),%rsi        # 4010 <stdout@GLIBC_2.2.5>
    120e:       48 29 fe                sub    %rdi,%rsi
    1211:       48 89 f0                mov    %rsi,%rax
    1214:       48 c1 ee 3f             shr    $0x3f,%rsi
    1218:       48 c1 f8 03             sar    $0x3,%rax
    121c:       48 01 c6                add    %rax,%rsi
    121f:       48 d1 fe                sar    $1,%rsi
    1222:       74 14                   je     1238 <register_tm_clones+0x38>
    1224:       48 8b 05 c5 2d 00 00    mov    0x2dc5(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable@Base>
    122b:       48 85 c0                test   %rax,%rax
    122e:       74 08                   je     1238 <register_tm_clones+0x38>
    1230:       ff e0                   jmp    *%rax
    1232:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)
    1238:       c3                      ret
    1239:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001240 <__do_global_dtors_aux>:
    1240:       f3 0f 1e fa             endbr64
    1244:       80 3d dd 2d 00 00 00    cmpb   $0x0,0x2ddd(%rip)        # 4028 <completed.0>
    124b:       75 2b                   jne    1278 <__do_global_dtors_aux+0x38>
    124d:       55                      push   %rbp
    124e:       48 83 3d a2 2d 00 00    cmpq   $0x0,0x2da2(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1255:       00
    1256:       48 89 e5                mov    %rsp,%rbp
    1259:       74 0c                   je     1267 <__do_global_dtors_aux+0x27>
    125b:       48 8b 3d a6 2d 00 00    mov    0x2da6(%rip),%rdi        # 4008 <__dso_handle>
    1262:       e8 79 fe ff ff          call   10e0 <__cxa_finalize@plt>
    1267:       e8 64 ff ff ff          call   11d0 <deregister_tm_clones>
    126c:       c6 05 b5 2d 00 00 01    movb   $0x1,0x2db5(%rip)        # 4028 <completed.0>
    1273:       5d                      pop    %rbp
    1274:       c3                      ret
    1275:       0f 1f 00                nopl   (%rax)
    1278:       c3                      ret
    1279:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001280 <frame_dummy>:
    1280:       f3 0f 1e fa             endbr64
    1284:       e9 77 ff ff ff          jmp    1200 <register_tm_clones>

0000000000001289 <initialize>:
    1289:       f3 0f 1e fa             endbr64
    128d:       55                      push   %rbp
    128e:       48 89 e5                mov    %rsp,%rbp
    1291:       48 8b 05 88 2d 00 00    mov    0x2d88(%rip),%rax        # 4020 <stdin@GLIBC_2.2.5>
    1298:       b9 00 00 00 00          mov    $0x0,%ecx
    129d:       ba 02 00 00 00          mov    $0x2,%edx
    12a2:       be 00 00 00 00          mov    $0x0,%esi
    12a7:       48 89 c7                mov    %rax,%rdi
    12aa:       e8 b1 fe ff ff          call   1160 <setvbuf@plt>
    12af:       48 8b 05 5a 2d 00 00    mov    0x2d5a(%rip),%rax        # 4010 <stdout@GLIBC_2.2.5>
    12b6:       b9 00 00 00 00          mov    $0x0,%ecx
    12bb:       ba 02 00 00 00          mov    $0x2,%edx
    12c0:       be 00 00 00 00          mov    $0x0,%esi
    12c5:       48 89 c7                mov    %rax,%rdi
    12c8:       e8 93 fe ff ff          call   1160 <setvbuf@plt>
    12cd:       90                      nop
    12ce:       5d                      pop    %rbp
    12cf:       c3                      ret

00000000000012d0 <get_rand_num>:
    12d0:       f3 0f 1e fa             endbr64
    12d4:       55                      push   %rbp
    12d5:       48 89 e5                mov    %rsp,%rbp
    12d8:       48 83 ec 20             sub    $0x20,%rsp
    12dc:       48 89 7d e8             mov    %rdi,-0x18(%rbp)
    12e0:       be 00 00 00 00          mov    $0x0,%esi
    12e5:       48 8d 05 18 0d 00 00    lea    0xd18(%rip),%rax        # 2004 <_IO_stdin_used+0x4>
    12ec:       48 89 c7                mov    %rax,%rdi
    12ef:       b8 00 00 00 00          mov    $0x0,%eax
    12f4:       e8 77 fe ff ff          call   1170 <open@plt>
    12f9:       89 45 fc                mov    %eax,-0x4(%rbp)
    12fc:       83 7d fc 00             cmpl   $0x0,-0x4(%rbp)
    1300:       79 0a                   jns    130c <get_rand_num+0x3c>
    1302:       bf 01 00 00 00          mov    $0x1,%edi
    1307:       e8 84 fe ff ff          call   1190 <exit@plt>
    130c:       48 8b 4d e8             mov    -0x18(%rbp),%rcx
    1310:       8b 45 fc                mov    -0x4(%rbp),%eax
    1313:       ba 04 00 00 00          mov    $0x4,%edx
    1318:       48 89 ce                mov    %rcx,%rsi
    131b:       89 c7                   mov    %eax,%edi
    131d:       e8 0e fe ff ff          call   1130 <read@plt>
    1322:       48 83 f8 04             cmp    $0x4,%rax
    1326:       74 0a                   je     1332 <get_rand_num+0x62>
    1328:       bf 01 00 00 00          mov    $0x1,%edi
    132d:       e8 5e fe ff ff          call   1190 <exit@plt>
    1332:       8b 45 fc                mov    -0x4(%rbp),%eax
    1335:       89 c7                   mov    %eax,%edi
    1337:       e8 e4 fd ff ff          call   1120 <close@plt>
    133c:       90                      nop
    133d:       c9                      leave
    133e:       c3                      ret

000000000000133f <main>:
    133f:       f3 0f 1e fa             endbr64
    1343:       55                      push   %rbp
    1344:       48 89 e5                mov    %rsp,%rbp
    1347:       48 83 ec 40             sub    $0x40,%rsp
    134b:       c7 45 dc 00 00 00 00    movl   $0x0,-0x24(%rbp)
    1352:       c7 45 d8 00 00 00 00    movl   $0x0,-0x28(%rbp)
    1359:       c7 45 f8 00 00 00 00    movl   $0x0,-0x8(%rbp)
    1360:       b8 00 00 00 00          mov    $0x0,%eax
    1365:       e8 1f ff ff ff          call   1289 <initialize>
    136a:       bf 45 00 00 00          mov    $0x45,%edi
    136f:       e8 dc fd ff ff          call   1150 <malloc@plt>
    1374:       48 89 45 f0             mov    %rax,-0x10(%rbp)
    1378:       be 00 00 00 00          mov    $0x0,%esi
    137d:       48 8d 05 8d 0c 00 00    lea    0xc8d(%rip),%rax        # 2011 <_IO_stdin_used+0x11>
    1384:       48 89 c7                mov    %rax,%rdi
    1387:       b8 00 00 00 00          mov    $0x0,%eax
    138c:       e8 df fd ff ff          call   1170 <open@plt>
    1391:       89 45 ec                mov    %eax,-0x14(%rbp)
    1394:       48 8b 4d f0             mov    -0x10(%rbp),%rcx
    1398:       8b 45 ec                mov    -0x14(%rbp),%eax
    139b:       ba 45 00 00 00          mov    $0x45,%edx
    13a0:       48 89 ce                mov    %rcx,%rsi
    13a3:       89 c7                   mov    %eax,%edi
    13a5:       e8 86 fd ff ff          call   1130 <read@plt>
    13aa:       8b 45 ec                mov    -0x14(%rbp),%eax
    13ad:       89 c7                   mov    %eax,%edi
    13af:       e8 6c fd ff ff          call   1120 <close@plt>
    13b4:       48 8d 45 d8             lea    -0x28(%rbp),%rax
    13b8:       48 89 c7                mov    %rax,%rdi
    13bb:       e8 10 ff ff ff          call   12d0 <get_rand_num>
    13c0:       8b 45 d8                mov    -0x28(%rbp),%eax
    13c3:       89 c6                   mov    %eax,%esi
    13c5:       48 8d 05 4c 0c 00 00    lea    0xc4c(%rip),%rax        # 2018 <_IO_stdin_used+0x18>
    13cc:       48 89 c7                mov    %rax,%rdi
    13cf:       b8 00 00 00 00          mov    $0x0,%eax
    13d4:       e8 27 fd ff ff          call   1100 <printf@plt>
    13d9:       48 8d 05 4c 0c 00 00    lea    0xc4c(%rip),%rax        # 202c <_IO_stdin_used+0x2c>
    13e0:       48 89 c7                mov    %rax,%rdi
    13e3:       b8 00 00 00 00          mov    $0x0,%eax
    13e8:       e8 13 fd ff ff          call   1100 <printf@plt>
    13ed:       48 8d 45 dc             lea    -0x24(%rbp),%rax
    13f1:       48 89 c6                mov    %rax,%rsi
    13f4:       48 8d 05 39 0c 00 00    lea    0xc39(%rip),%rax        # 2034 <_IO_stdin_used+0x34>
    13fb:       48 89 c7                mov    %rax,%rdi
    13fe:       b8 00 00 00 00          mov    $0x0,%eax
    1403:       e8 78 fd ff ff          call   1180 <__isoc99_scanf@plt>
    1408:       8b 55 d8                mov    -0x28(%rbp),%edx
    140b:       8b 45 dc                mov    -0x24(%rbp),%eax
    140e:       31 d0                   xor    %edx,%eax
    1410:       89 45 f8                mov    %eax,-0x8(%rbp)
    1413:       8b 55 f8                mov    -0x8(%rbp),%edx
    1416:       48 8d 45 cf             lea    -0x31(%rbp),%rax
    141a:       89 d1                   mov    %edx,%ecx
    141c:       48 8d 15 14 0c 00 00    lea    0xc14(%rip),%rdx        # 2037 <_IO_stdin_used+0x37>
    1423:       be 09 00 00 00          mov    $0x9,%esi
    1428:       48 89 c7                mov    %rax,%rdi
    142b:       b8 00 00 00 00          mov    $0x0,%eax
    1430:       e8 db fc ff ff          call   1110 <snprintf@plt>
    1435:       c7 45 fc 00 00 00 00    movl   $0x0,-0x4(%rbp)
    143c:       eb 1c                   jmp    145a <main+0x11b>
    143e:       b8 07 00 00 00          mov    $0x7,%eax
    1443:       2b 45 fc                sub    -0x4(%rbp),%eax
    1446:       48 98                   cltq
    1448:       0f b6 54 05 cf          movzbl -0x31(%rbp,%rax,1),%edx
    144d:       8b 45 fc                mov    -0x4(%rbp),%eax
    1450:       48 98                   cltq
    1452:       88 54 05 c6             mov    %dl,-0x3a(%rbp,%rax,1)
    1456:       83 45 fc 01             addl   $0x1,-0x4(%rbp)
    145a:       83 7d fc 07             cmpl   $0x7,-0x4(%rbp)
    145e:       7e de                   jle    143e <main+0xff>
    1460:       48 8d 45 c6             lea    -0x3a(%rbp),%rax
    1464:       48 89 c6                mov    %rax,%rsi
    1467:       48 8d 05 ce 0b 00 00    lea    0xbce(%rip),%rax        # 203c <_IO_stdin_used+0x3c>
    146e:       48 89 c7                mov    %rax,%rdi
    1471:       b8 00 00 00 00          mov    $0x0,%eax
    1476:       e8 85 fc ff ff          call   1100 <printf@plt>
    147b:       48 8d 05 c6 0b 00 00    lea    0xbc6(%rip),%rax        # 2048 <_IO_stdin_used+0x48>
    1482:       48 89 45 e0             mov    %rax,-0x20(%rbp)
    1486:       48 8b 55 e0             mov    -0x20(%rbp),%rdx
    148a:       48 8d 45 c6             lea    -0x3a(%rbp),%rax
    148e:       48 89 d6                mov    %rdx,%rsi
    1491:       48 89 c7                mov    %rax,%rdi
    1494:       e8 a7 fc ff ff          call   1140 <strcmp@plt>
    1499:       85 c0                   test   %eax,%eax
    149b:       75 1d                   jne    14ba <main+0x17b>
    149d:       48 8d 05 ad 0b 00 00    lea    0xbad(%rip),%rax        # 2051 <_IO_stdin_used+0x51>
    14a4:       48 89 c7                mov    %rax,%rdi
    14a7:       e8 44 fc ff ff          call   10f0 <puts@plt>
    14ac:       48 8b 45 f0             mov    -0x10(%rbp),%rax
    14b0:       48 89 c7                mov    %rax,%rdi
    14b3:       e8 38 fc ff ff          call   10f0 <puts@plt>
    14b8:       eb 0f                   jmp    14c9 <main+0x18a>
    14ba:       48 8d 05 9a 0b 00 00    lea    0xb9a(%rip),%rax        # 205b <_IO_stdin_used+0x5b>
    14c1:       48 89 c7                mov    %rax,%rdi
    14c4:       e8 27 fc ff ff          call   10f0 <puts@plt>
    14c9:       b8 00 00 00 00          mov    $0x0,%eax
    14ce:       c9                      leave
    14cf:       c3                      ret

Disassembly of section .fini:

00000000000014d0 <_fini>:
    14d0:       f3 0f 1e fa             endbr64
    14d4:       48 83 ec 08             sub    $0x8,%rsp
    14d8:       48 83 c4 08             add    $0x8,%rsp
    14dc:       c3                      ret
```