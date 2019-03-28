
SELECT size.f AS '사이즈', price.f AS '가격', fit.f AS '착용감',,color.f AS '색상', design.f AS '디자인',
        light.f AS '경량감', strong.f AS '내구성', pocket.f AS '수납', material.f AS '재질', zipper.f AS '지퍼'
FROM
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('사이즈|크기|치수') AND content REGEXP ('잘|딱|적당|적정|좋|딱맞아'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
) AS size
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE ((content REGEXP ('가격|값') AND content REGEXP ('적당|합리적|싼')) OR content REGEXP ('세일가|싸게|저렴'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS price
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('들어|들면|메고|메보니|메면|메니|매고|매보니|매면|매니|착용') AND content REGEXP ('좋|편하|편해|굿|굳|괜찮|편안|편하|안아프|푹신|행복|마음에 듭|마음에 들|너무 편합|만족|찰떡'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS fit
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('색감|색상|블랙|검정|검은|화이트|하얀|흰색|핑크|아이보리|베이지|색갈|색깔|색이|검검|흰검|검흰')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS color
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('디자인|트렌디|예쁘|예쁜|예뽀|이쁘|이쁨|이쁜|심플|깔끔|말끔|핏|존예|추천|깔끔')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS design
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('경량|가볍|가벼')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS light
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE ((content REGEXP ('내구성') AND content REGEXP ('괜찮|좋아|갑')) OR content REGEXP ('튼튼|탄탄|짱짱'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS strong
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('수납') AND content REGEXP ('넉넉|널널|많아|많고'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS pocket
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('재질|품질|가죽') AND content REGEXP ('좋고|좋아|만족'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS material
JOIN
(
SELECT COUNT(*) AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE (content REGEXP ('지퍼') AND content REGEXP ('잘열|잘 열|이쁘|예뻐|탄탄'))
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2019년봄'
)AS zipper


