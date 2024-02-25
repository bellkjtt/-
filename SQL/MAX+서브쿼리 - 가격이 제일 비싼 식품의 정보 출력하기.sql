https://school.programmers.co.kr/learn/courses/30/lessons/131115

-- 코드를 입력하세요
SELECT * FROM FOOD_PRODUCT 
    WHERE PRICE= (SELECT MAX(PRICE) FROM FOOD_PRODUCT);

WHERE을 사용하여 하나의 값으로 나온 서브쿼리를 특정하도록 만들 수 있다.


