
# 데상트_신발_긍정찾기
SET @brand = '디스커버리 익스페디션';

SELECT size.feed_count AS '사이즈', price.feed_count AS '가격', fit.feed_count AS '착화감', couple.feed_count AS '커플', daily.feed_count AS '데일리', color.feed_count AS '색상',
	design.feed_count AS '디자인', light.feed_count AS '경량감', trend.feed_count AS '유행', gift.feed_count AS '선물', season.feed_count AS '계절', new_semester.feed_count AS '신학기', running.feed_count AS '운동용'
FROM
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND ((content REGEXP ('사이즈|크기|치수') AND content REGEXP ('잘|딱|적당|적정|좋'))
	OR content REGEXP ('정사이즈|정 사이즈|딱맞아'))
AND brand = @brand
) AS size
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND ((content REGEXP ('가격') AND content REGEXP ('적당|합리적|싼'))
	OR content REGEXP ('세일가|싸게|저렴'))
AND brand = @brand
) AS price
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND ((content REGEXP ('착화감|착용감|발볼') AND content REGEXP ('좋|편하|편해|굿|굳|괜찮'))
	OR content REGEXP ('편안|편하|안아프|만보|기동성|푹신|행복|마음에 듭|마음에 들|너무 편합|만족'))
AND brand = @brand
) AS fit
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('커플|남친|여친|남자친구|여자친구|신랑|와이프|데이트|남자 친구|여자 친구')
AND brand = @brand
) AS couple
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND ((content REGEXP ('코디|매치') AND content REGEXP ('편하|편해|좋은|좋아'))
	OR content REGEXP ('데일리|아무옷|아무 옷|어느 옷|어디에나|다양하게|매일|집앞|어느룩|모든바지|기본템|모든 핏|베이직'))
AND brand = @brand
) AS daily
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('색감|색상|블랙|검정|검은|화이트|하얀|흰색|핑크|아이보리|베이지|색갈|색깔|색이|검검|흰검|검흰')
AND brand = @brand
) AS color
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('디자인|트렌디|예쁘|예쁜|예뽀|이쁘|이쁜|심플|깔끔|말끔|핏|존예|추천|깔끔')
AND brand = @brand
) AS design
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('경량|가볍|가벼')
AND brand = @brand
) AS light
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('국민신발|국민 신발|유행') 
AND brand = @brand
) AS trend
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('선물|주려고|사줬')
AND brand = @brand
) AS gift
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('봄|여름|가을|겨울|계절|환절기|시즌|봄날')
AND brand = @brand
) AS season
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('신학기|신 학기|개강|개학|입학')
AND brand = @brand
) AS new_semester
JOIN
(SELECT COUNT(*) AS feed_count
FROM musinsa_review
WHERE table_index LIKE ('%spring%')
AND content REGEXP ('운동|다이어트|러닝|조깅|등산|바이크|하이킹|골프')
AND brand = @brand
) AS running




