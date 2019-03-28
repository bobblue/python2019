SELECT *
FROM
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE DATE LIKE '%.%'
AND content LIKE '%운동화%') AS a
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE DATE LIKE '%.%'
AND content LIKE '%스니커즈%') AS b
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE DATE LIKE '%.%'
AND content LIKE '%슬립온%') AS c
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE DATE LIKE '%.%'
AND content LIKE '%런닝화%') AS d
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE DATE LIKE '%.%'
AND content LIKE '%조깅화%') AS e
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE DATE LIKE '%.%'
AND content LIKE '%마라톤화%') AS f
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%트레이닝화%') AS g
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%헬스화%') AS h
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%테니스화%') AS i
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%농구화%') AS n
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%워킹화%') AS m
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%트레이닝화%') AS j
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%등산화%') AS k
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
where date LIKE '%.%'
AND content LIKE '%어글리슈즈%') AS l



