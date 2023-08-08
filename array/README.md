## Array 
index 로 문제를 접근하는 유형이며 BackTracking과 DP 문제와 함께 자주 사용된다. 
* two pointer
* sliding
  * 배열이 모두 양수일 때 사용 가능 
### Sorting 
* heap, quick, merge sorting의 종류가 있으며
* time complexity 는 **O(nlogn)**
* stable? Unstable? 에 따라 sorting 종류를 나눌 수 있다.
  정렬 후에도 기존 배열의 순서를 유지하는가? 
  * YES > Stable : merge sort
  * NO > Unstable : quick , heap sort
 
### Search 
* time complexity 는 **O(n)** 으로 하나하나 확인하는 방법이며

### Binary Search 
배열이 **정렬되어있을 때** 사용할 수 있는 방법으로 
* time complexity 는 **O(logN)**이다.
* left / right , pivot 으로 찾아가는 방법으로
  * arr[pivot]과 target 값 비교 후 left를 pivot+1 혹은 right를 pivot-1로 옮기는 과정을 통해 진행한다.
  * 종료 조건은 left와 right의 크기 비교로 한다. while(left<=right) 
