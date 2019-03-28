
SELECT black.f AS '��', beige.f AS '������', charcoal.f AS '����', grey.f AS '�׷���', pink.f AS '��ũ', ivory.f AS '���̺���', 
	navy.f AS '���̺�', white.f AS 'ȭ��Ʈ', brown.f AS '����', red.f AS '����', blue.f AS '���', 
	green.f AS '�׸�', puple.f AS '����', mint.f AS '��Ʈ'
FROM
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('��BLACK��������')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS black
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('������BEIGE')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS beige
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('����CHARCOAL')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS charcoal
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('�׷���GRAYȸ��')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS grey
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('��ũPINK��ȫ')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS pink
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('���̺���IVORYCreamũ��')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS ivory
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('���̺�Navy����')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS navy
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('ȭ��ƮWhite�Ͼ��Ͼ�')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS white
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('����Brown����')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS brown
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('����RED��������')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS red
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('���BLUE�Ķ��Ķ�')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS blue
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('�׸�GREEN�ʷ�')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS green
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('����PUPLEViolet����󺥴�lavender')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS puple
JOIN
(
SELECT COUNT() AS f
FROM yoonah.musinsa_backpack_review AS m1
	JOIN yoonah.musinsa_backpack_info AS m2
	ON m1.product_num = m2.product_num
	WHERE content REGEXP ('��ƮMINT')
	#AND brand LIKE '%����Ű��Ͻ�%'
	AND m1.sort LIKE '2018�⺽'
) AS mint







