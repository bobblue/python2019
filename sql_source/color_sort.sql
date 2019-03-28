
SELECT black.f AS '블랙', beige.f AS '베이지', charcoal.f AS '차콜', grey.f AS '그레이', pink.f AS '핑크', ivory.f AS '아이보리', 
	navy.f AS '네이비', white.f AS '화이트', brown.f AS '브라운', red.f AS '레드', blue.f AS '블루', 
	green.f AS '그린', puple.f AS '퍼플', mint.f AS '민트'
FROM
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('블랙BLACK검은검정')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS black
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('베이지BEIGE')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS beige
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('차콜CHARCOAL')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS charcoal
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('그레이GRAY회색')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS grey
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('핑크PINK분홍')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS pink
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('아이보리IVORYCream크림')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS ivory
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('네이비Navy남색')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS navy
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('화이트White하얀하양')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS white
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('브라운Brown갈색')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS brown
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('레드RED빨간빨강')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS red
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('블루BLUE파란파랑')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS blue
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('그린GREEN초록')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS green
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('퍼플PUPLEViolet보라라벤더lavender')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS puple
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('민트MINT')
	#AND brand LIKE '%네이키드니스%'
	AND m1.sort LIKE '2018년봄'
) AS mint







