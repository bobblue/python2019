
# 데상트_신발_부정찾기
SET @brand = '디스커버리 익스페디션';

SELECT size_neg.feed_count AS '부정_사이즈', hardness.feed_count AS '부정_내구성', price_neg.feed_count AS '부정_가격', fit_neg.feed_count AS '부정_착화감', 
	quality_neg.feed_count AS '부정_품질', fake.feed_count AS '부정_가품의심', smell.feed_count AS '냄새'
FROM
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND (content REGEXP ('작아|작은|작긴|끼는|끼네|큰|커|크긴|남네|작음|작게|낑겨|껴|작네|크네|타이트|아파|아픈|좁은')
	OR (content REGEXP ('사이즈') AND content REGEXP ('애매|주의|실수')))
AND brand = @brand
) AS size_neg
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('약하|약해|부실|헤지|해진|낡아|약한')
AND brand = @brand
) AS hardness
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND ((content REGEXP ('가격|값') AND content REGEXP ('ㄷㄷ'))
	OR content REGEXP ('비싸|비싼|바가지|돈아깝|돈 아깝|돈아까|돈 아까'))
AND brand = @brand
) AS price_neg
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('딱딱|불편|발 아파|발아파|발볼 껴|발볼 끼|조이는|조여|둔탁|좁아|낑낑|무겁|무게감')
AND brand = @brand
) AS fit_neg
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('물빠짐|물 빠지|물 빠져|오염|미끌|밑창이 약|미끄러|세탁|더러워|먼지|싸구려|싼티|마모|질찢어')
AND brand = @brand
) AS quality_neg
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('가품|가짜|짝퉁|정품 맞나|정품 맞는지|정품 의심|정품인지')
AND brand = @brand
) AS fake
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('냄새')
AND brand = @brand
) AS smell



