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
* time complexity 는 **O(logN)** 이다.
* left / right , pivot 으로 찾아가는 방법으로
  * arr[pivot]과 target 값 비교 후 left를 pivot+1 혹은 right를 pivot-1로 옮기는 과정을 통해 진행한다.
  * 종료 조건은 left와 right의 크기 비교로 한다. while(left<=right) 

## Array vs. List ? 
### Array
* 같은 자료형으로 grouping되어있으며 고정된 크기를 가지고 있다.
  > ex. 48평에 10명이 같이 합숙생활을 하며 순서대로 각 방을 사용하고 있다. <br>
  > 만약 누군가가 새로 들어오고 원하는 위치가 중간 방일 때 나머지 사람들이 순차적으로 모두 이동해야한다.
* **삽입/삭제시 많은 일이 필요하다는 단점을 가지고 있다.** 
* **인덱스를 사용하여 빠른 검색이 가능하다.**

### List 
* Node로 구성되어있으며 각 Node는 Pointer를 가지고 있다.
* **인덱스를 사용하지 않기 때문에 느린 탐색속도를 가지고 있다.**
* **Pointer를 사용하여 유연한 삽입/삭제가 가능하다.**
* ArrayList / Linked List 종류가 있으며
  * ArrayList 는 array의 장점을 가져온 것 
