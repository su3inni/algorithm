## Remind Points 
### 1. 데이터 정렬할 때 
+ order by <col#1> desc, <col#2>
   + col#1에 대해서 내림차순으로 정렬한 뒤, col#2에 대해서 오름차순 정렬하겠다는 구문

### 2. date format 
+ DATE_FORMAT(<col>, '%Y-%m-%d') AS <col>
   + '%Y-%M-%D' 하면 또 다른 포맷 나오니까 잘 맞추기

### 3. Null 값 대체하기 
+ IFNULL(<col>,'대체값')
