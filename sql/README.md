## Remind Points 
### 1. 데이터 정렬할 때 
+ order by <col#1> desc, <col#2>
   + col#1에 대해서 내림차순으로 정렬한 뒤, col#2에 대해서 오름차순 정렬하겠다는 구문

### 2. date format 
+ DATE_FORMAT(<col>, '%Y-%m-%d') AS <col>
   + '%Y-%M-%D' 하면 또 다른 포맷 나오니까 잘 맞추기

### 3. Null 값 대체하기 
+ IFNULL(<col#1>,'대체값')

### 4. Null 값 찾기 
+ WHERE <COL#1> IS NULL

### 5. JOIN 
+ FROM <TABLE#1> A
   INNER JOIN <TABLE#2> B ON A.COL#1 = B.COL#1
  > table 1을 A라고 하고, table 2는 B라고 하고 col#1을 기준으로 join 한다

### 6. 평균값과 반올림 
+ ROUND(COL,2)
  > 3째자리에서 반올림하는 구문
+ AVG(<col>)

### 7. WHERE절에 SELECT문 있는 서브쿼리 
ex. WHERE ITEM_ID NOT IN ( SELECT PARENT_ITEM_ID 
                     FROM ITEM_TREE WHERE NOT PARENT_ITEM_ID IS NULL) 
