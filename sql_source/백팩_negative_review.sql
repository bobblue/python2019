
SELECT size.f AS '사이즈', strong.f AS '내구성', price.f AS '가격', fit.f AS '착용감', smell.f AS '냄새', pocket.f AS '수납',
        material.f AS '재질', zipper.f AS '지퍼', design.f '디자인'
FROM
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('사이즈|크기|치수') AND content REGEXP ('애매|주의|실수|작아|작은|작긴|끼는|끼네|남네|작음|작게|낑겨|껴|작네|타이트|아파|아픈|좁은'))
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
) AS size
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('약하|약해|부실|헤지|해진|낡아|약한|헐거워')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS strong
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('비싸|비싼|바가지|돈아깝|돈 아깝|돈아까|돈 아까')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS price
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('딱딱|불편|조이는|조여|둔탁|좁아|낑낑|무겁|무게감|무거')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS fit
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('냄새')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS smell
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('수납') AND content REGEXP ('없어|부족|아쉽'))
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS pocket
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('재질|품질|가죽') AND content REGEXP ('별로|떨어|너덜|얇아|빳빳|않네|더러워|먼지|싸구려|싼티|마모'))
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS material
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('지퍼') AND content REGEXP ('불편|퍽퍽|별로|뻑뻑|힘들|짜증|빳빳'))
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS zipper
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('촌스러|얇아')
	AND brand LIKE '%로아드로아%'
	AND m1.sort LIKE '2019년봄'
)AS design
