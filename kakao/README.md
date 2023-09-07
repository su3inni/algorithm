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
  * for i in range(3, _**int(num ** 0.5) + 1**_, 2):
            if num%i==0:
