## Remind Point
### 1. 두 정수 A,B 를 사용할 때 대소비교하기 
+ A<B , A>B , **A==B** 인 경우 모두 고려했는지 다시 한 번 확인하기

### 2. 빠른 입력을 받아야하는 경우 
+ T번 반복하는데 최대 1,000,000 이라면
  + input()대신 **sys.stdin.readline()** 을 사용한다. 
    > [sys.stdin.readline 사용법 참고](https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline)  

### 3. 배열을 정렬이 아닌 뒤집는 경우 
+ arr[::-1] 
