## Remind Point
### 1. 두 정수 A,B 를 사용할 때 대소비교하기 
+ A<B , A>B , **A==B** 인 경우 모두 고려했는지 다시 한 번 확인하기

### 2. 빠른 입력을 받아야하는 경우 
+ T번 반복하는데 최대 1,000,000 이라면
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

