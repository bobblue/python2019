
SELECT couple.f AS '커플', trend.f AS '유행', gift.f AS '선물', season.f AS '계절', new_s.f AS '신학기',
        sports.f AS '운동', travel.f AS '여행', school.f AS '학교 학원', daily.f AS '데일리'
FROM
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('커플|남친|여친|남자친구|여자친구|신랑|와이프|데이트|남자 친구|여자 친구')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
) AS couple
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('유행|국민백팩')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS trend
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('선물')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS gift
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('여름|가을|겨울|계절|환절기|시즌|봄날|봄 날|봄에|봄이라')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS season
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('신학기|신 학기|새학기|새 학기|개강|개학|입학')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS new_s
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('운동하|운동 하|운동용|운동가|운동 가|운동갈|운동 갈|다이어트|러닝|조깅|등산|바이크|하이킹|골프|보드|스키')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS sports
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('여행')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS travel
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('학교|학원')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS school
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE ((content REGEXP ('코디|매치') AND content REGEXP ('편하|편해|좋은|좋아')) OR content REGEXP ('데일리|아무옷|아무 옷|어느 옷|어디에나|다양하게|매일|집앞|어느룩|모든바지|기본템|모든 핏|베이직'))
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
) AS daily

	


    
    
    