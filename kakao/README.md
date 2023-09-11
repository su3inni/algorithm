## Level2
### 2018 KAKAO BLIND RECRUITMENT [1차] 캐시 > LRUcache.py
* LRU cache 방법 구현시, HIT된 경우 cache update에도 신경써야함

### 2019 카카오 개발자 겨울 인턴십 튜플 > tuple.py
* string으로 들어오는 입력값 전처리
  *  ts = s.split('},{')
* ts.sort(key=len)

### 2018 KAKAO BLIND RECRUITMENT [1차] 뉴스 클러스터링 > news_clustering.py
* **isalpha()**
* cpl2.pop(cpl2.index(st))
  * 특정 요소의 인덱스 구하고 > l1.index(value)
  * 해당 요소 인덱스 pop()

### 2022 KAKAO BLIND RECRUITMENT k진수에서 소수 개수 구하기 > k_primenum.py
+ num의 범위가 1 ≤ n ≤ 1,000,000 일때
  * for i in range(2,num) 으로 소수를 판별하려고 하면 시간초과 발생 
  * for i in range(3, _**int(num ** 0.5) + 1**_, **2**):
            if num%i==0:<br>
    #3부터 root(k)까지 2씩 증가하며 확인하는 방법으로(3, 5, 7...),<br>
    #작은 값들의 배수일 때 발생하는 중복을 제거하며 확인(소수 찾기 최적화)

### 2018 KAKAO BLIND RECRUITMENT [3차] 압축 > zip.py 
+ D = {chr(i) : i-64 for i in range(65,91)}
+ start, end 포인터 두개로 진행하기

### 2022 KAKAO BLIND RECRUITMENT 주차 요금 계산 > stack_fee.py 
* stack 같은 문제를 풀 때 주의할 점
  * 반복해서 실행하는 경우에 대한 고려를 필수적으로 하기
    * 틀렸던 부분 확인 
* 딕셔너리 정렬 방법
* 딕셔너리 삭제 방법

### 2019 KAKAO BLIND RECRUITMENT 오픈채팅방 > openchat_lognick.py
* 천천히 생각해라
