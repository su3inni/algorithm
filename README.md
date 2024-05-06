# Remind Points
## #0. 시간 복잡도 
### 제한사항 확인하기 
+ 제한사항 범위를 확인하고 어떤 방식으로 문제를 해결할 것인지 파악하기
  > 1억번 == 1초 라고 생각하고 N크기가 10000보다 큰 경우 완전탐색은 어렵다
+ 너무 값이 크면 완전탐색이 어렵기 때문에 **규칙성을 찾아보자**

### str 입력의 길이가 1,000,000 일때 O(N)의 방법으로 해결하기 
+ for 문 내에 python list insert 가 들어가면 O(N**2)의 시간 복잡도가 발생한다.
  + 입력을 기준에 따라 나누어서 배열에 넣는 방법 고려하기 left, right 
+ list extend, reversed 방법 익히기

### 시간초과 계산 방법 
+ python 시간제한 1초 > 약 10^6 정도의 작업 횟수
  + N의 범위가 5000이여도 5000*5000 작업의 경우 시간초과 가능하므로 알고리즘 시간복잡도 계산 잘하기
  + 특히 list 의 append,pop, sum 과 같은 연산작업할때의 시간복잡도 계산 잘하기 

### 완전탐색을 하기에 범위가 너무 클 때 
+ 패턴을 이용한 구현으로 해결할 수 있는지 생각하기
  > ex. 프로그래머스 Lv2 : 도넛과 막대그래프
  
## #1. 구현  
### % 연산 사용시 주의하기 
+ % 연산 후, 나머지가 0이 되는 경우에 대한 고려하기
   +  **날짜같은 경우는 0일이 없음!**
### / 나눗셈 연산시 주의하기 
+ / 연산할 때 분모가 0인 경우 처리해주기
  > if 분모가 0이 아닐때 
### 시간을 다루는 문제라면
+ **59분 다음이 00분인 경우의 처리**가 잘 되었는지 확인하기
  > 11:59 에서 00:00 넘어가는 시점같은

### 특정 변수를 사용한 if 문을 진행하는 경우 
> 예를 들면 숫자문자열과영단어.py 에서 part 변수 
+ 진행한 반복문이 끝난 후 특정 변수에 저장된 값에 따라 한번 더 진행해야하는지 꼭 확인하기
+ 사용한 변수 마지막까지 잘 확인하기

### 소수판별하는 경우 시간복잡도 줄이기 
+ for문 범위에서 (2,i//2) 는 연산 시간을 반으로 줄일 수 있고
+ 루트를 활용한다면 엄청난 연산 단축을 할 수 있다.
  > k_primenum.py ( K진법으로 소수 개수 구하기) 코드 확인

### K 진법 변환 
+ while 문으로 몫과 나머지 활용
  > k_primenum.py ( K진법으로 소수 개수 구하기) 코드 확인

### 두 정수 A,B 를 사용할 때 대소비교하기 
+ A<B , A>B , **A==B** 인 경우 모두 고려했는지 다시 한 번 확인하기

### 빠른 입력을 받아야하는 경우
+ [ input과 sys.stdin.readline 비교 ](https://github.com/su3inni/algorithm/issues/5)
+ 예를 들어, T번 반복하는데 최대 1,000,000 이라면
  + input()대신 **sys.stdin.readline()** 을 사용한다. 
    > [sys.stdin.readline 사용법 참고](https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline)

### "최소" 의 문제를 풀때는 
+ if문 조건 꼼꼼하게 확인하기
  + 부등호와 = 신경써서 다시 한 번 검토하기


### bruteforce로 인해 너무 많은 for문을 사용하는가 싶을때 
+ 반대의 경우를 생각해보기 

### 특정 조건이 붙는 경우 
+ 특정 조건을 제외한 상황과 특정 조건의 상황을 나누어 생각하기
  > 1475번 방번호와 같은 문제
+ 특정 조건의 수가 **홀수인 경우와 짝수인 경우** 고려하기

### deque 사용시 
+ deque가 비었는지 값이 있는지 확인하는 과정 필수!

### 회전할 때 
+ 배열 회전 후 영향받는 다른 파라미터가 있는지 꼭 확인하기
  > 예를 들면, 배열 회전 후 업데이트해야하는 다른 파라미터값 혹은 배열

## #2. 배열 
### 배열의 인덱스 활용하기 
+ 바로 이전 값을 활용해야하는 경우 `arr[-1]`, 혹은 누적해서 영향을 받는 경우 `arr[-2]`
  + 효과가 중첩되는 경우에는 새로 배열을 생성해서 값을 업데이트하는 방법을 떠올리자
 
### 배열의 시간복잡도와 deque 활용
+ list 의 pop(0)보다 deque의 popleft()를 사용하는 것이 시간복잡도에 유리
+ 반복문 내에서 sum() 을 하는 경우 시간 복잡도가 늘어날 수 있으니 값을 -= += 하는 것으로 대체할 수 있는지 확인하기

### 배열을 정렬이 아닌 뒤집는 경우 
+ arr[::-1] 

### 배열의 크기가 너무 클때 
+ **Two Pointer** 방법 고려해보기
  + 배열 정렬 후 > python정렬 시간복잡도 O(NlogN)
    > [정렬 알고리즘 개념 정리](https://github.com/su3inni/algorithm/issues/3#issuecomment-1753235209)
  + left, right 인덱스로 조절하며 O(n)으로 문제해결하기

### list로 시간초과가 걱정된다면 deque 사용 고려하기 
+ 요소 삽입/삭제가 빈번한 경우 deque 사용하기
  + list의 pop(0) 의 경우, 요소 제거 후 재정렬하므로 O(N)의 시간복잡도가 소요되지만
  + deque의 popleft의 경우 재정렬과정이 없어 O(1)의 시간복잡도가 소요된다.
+ 원형 큐의 경우 deque로 효율적인 알고리즘 작성이 가능하다


## #3. 그래프 
### DFS로 조합하기 
+ [가능한 모든 조합을 DFS](https://github.com/su3inni/algorithm/blob/main/kakao/Level2/이모티콘할인행사.py)로 구하기
  > 단,범위가 작아서 완전탐색이 가능할 때

###  BFS 진행할 때 메모리초과 유의하기 
+ BFS 큐에 들어가는 값의 중복 여부, 값 자체의 범위 여부 확인하기

