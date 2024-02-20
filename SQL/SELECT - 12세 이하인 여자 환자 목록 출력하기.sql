https://school.programmers.co.kr/learn/courses/30/lessons/132201

-- 코드를 입력하세요
SELECT PT_NAME,PT_NO,GEND_CD,AGE,IFNULL(TLNO,'NONE') FROM PATIENT WHERE (AGE<=12 AND GEND_CD='W') ORDER BY AGE DESC,PT_NAME ASC

#12세 이하 여자환자 이름을 출력. ORDER BY를 나이로 하고, 그 조건이 충족된다면 이름으로.