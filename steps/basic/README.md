## Remind Point
### 1. 두 정수 A,B 를 사용할 때 대소비교하기 
+ A<B , A>B , **A==B** 인 경우 모두 고려했는지 다시 한 번 확인하기

### 2. 빠른 입력을 받아야하는 경우
+ [ input과 sys.stdin.readline 비교 ](https://github.com/su3inni/algorithm/issues/5)
+ 예를 들어, T번 반복하는데 최대 1,000,000 이라면
  + input()대신 **sys.stdin.readline()** 을 사용한다. 
    > [sys.stdin.readline 사용법 참고](https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline)
  

### 3. 배열을 정렬이 아닌 뒤집는 경우 
+ arr[::-1] 

### 4. bruteforce로 인해 너무 많은 for문을 사용하는가 싶을때 
+ 반대의 경우를 생각해보기 

### 5. 특정 조건이 붙는 경우 
+ 특정 조건을 제외한 상황과 특정 조건의 상황을 나누어 생각하기
  > 1475번 방번호와 같은 문제
+ 특정 조건의 수가 **홀수인 경우와 짝수인 경우** 고려하기

### 6. 배열의 크기가 너무 클때 
+ **Two Pointer** 방법 고려해보기
  + 배열 정렬 후 > python정렬 시간복잡도 O(NlogN)
    > [정렬 알고리즘 개념 정리](https://github.com/su3inni/algorithm/issues/3#issuecomment-1753235209)
  + left, right 인덱스로 조절하며 O(n)으로 문제해결하기

### 7. str 입력의 길이가 1,000,000 일때 O(N)의 방법으로 해결하기 
+ for 문 내에 python list insert 가 들어가면 O(N**2)의 시간 복잡도가 발생한다.
  + 입력을 기준에 따라 나누어서 배열에 넣는 방법 고려하기 left, right 
+ list extend, reversed 방법 익히기

### 8. 시간초과 계산 방법 
+ python 시간제한 1초 > 약 10^6 정도의 작업 횟수
  + N의 범위가 5000이여도 5000*5000 작업의 경우 시간초과 가능하므로 알고리즘 시간복잡도 계산 잘하기
  + 특히 list 의 append,pop, sum 과 같은 연산작업할때의 시간복잡도 계산 잘하기 

### 9. list로 시간초과가 걱정된다면 deque 사용 고려하기 
+ 요소 삽입/삭제가 빈번한 경우 deque 사용하기
  + list의 pop(0) 의 경우, 요소 제거 후 재정렬하므로 O(N)의 시간복잡도가 소요되지만
  + deque의 popleft의 경우 재정렬과정이 없어 O(1)의 시간복잡도가 소요된다.
+ 원형 큐의 경우 deque로 효율적인 알고리즘 작성이 가능하다

### 10. deque 사용시 
+ deque가 비었는지 값이 있는지 확인하는 과정 필수!

### 11. "최소" 의 문제를 풀때는 
+ if문 조건 꼼꼼하게 확인하기
  + 부등호와 = 신경써서 다시 한 번 검토하기
