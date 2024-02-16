## Remind Point 
### 1. 우선순위 큐 사용 방법 
**import heapq**
+ 힙에 요소 추가하기: **heapq.heappush(heap, element)**
+ 힙에서 요소 제거하기: **heapq.heappop(heap)**
  > 힙에서 최소(또는 최대) 요소를 제거하고 반환 <br>
  > heapq.heappop(heap) 하면 가장 작은 값이 나오는 것일 뿐, 전체가 정렬되어있지는않음
+ 힙의 최소(또는 최대) 요소 확인하기: **heapq.heappushpop(heap, element)**
+ 주어진 반복 가능한(iterable) 객체를 힙으로 변환하기 : heapq.heapify(iterable)
+ 힙의 최소(또는 최대) 요소만 확인하기
  + heapq.nsmallest(n, iterable)
  + heapq.nlargest(n, iterable)

