INSERT INTO public.brand (id, brand_name) VALUES (1, 'adsasas');

INSERT INTO public.collection (id, name, created_at, added_db_at) VALUES (1, 'jljasasalkjl', NULL, NULL);

INSERT INTO public.color (id, color_name, number_color) VALUES (1, 'jljlkjl', 1);

INSERT INTO public.compound (id, compound_name) VALUES (1, 'jljasasalkjl');

INSERT INTO public.pattern (id, patterns_name) VALUES (1, 'jljaasasasassasalkjl');

INSERT INTO public.season (id, seasons_name) VALUES (1, 'jljlkjl');

INSERT INTO public.affiliation (id, name) VALUES (1, 'мужской');

INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at, affiliation_id) VALUES (1, 'jljlkjl', 1, 'asdasasasda', 1, 1, 1, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53', 1);
INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at, affiliation_id) VALUES (2, 'string', 1, 'string', 1, 1, NULL, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53', 1);
INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at, affiliation_id) VALUES (3, 'string', 1, 'string', 1, 1, NULL, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53', 1);
INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at, affiliation_id) VALUES (6, 'string', 1, 'string', 1, 1, NULL, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53', 1);

INSERT INTO category VALUES (1, 'Одежда', null);
INSERT INTO category VALUES (2, 'Верхняя одежда', 1);
INSERT INTO category VALUES (3, 'Нижнее белье', 1);
INSERT INTO category VALUES (4, 'Обувь', 1);
INSERT INTO category VALUES (5, 'Штаны', 2);
INSERT INTO category VALUES (6, 'Футболка', 2);
INSERT INTO category VALUES (7, 'Рубашка', 2);
INSERT INTO category VALUES (8, 'Куртка', 2);
INSERT INTO category VALUES (9, 'Майка', 3);
INSERT INTO category VALUES (10, 'Носки', 3);
INSERT INTO category VALUES (11, 'Трусы', 3);
INSERT INTO category VALUES (12, 'Кеды', 4);
INSERT INTO category VALUES (13, 'Кросовки', 4);
INSERT INTO category VALUES (14, 'Туфли', 4);
INSERT INTO category VALUES (15, 'С длинными рукавами', 6);
INSERT INTO category VALUES (16, 'С короткими рукавами', 6);
INSERT INTO category VALUES (17, 'V образный воротник', 6);
INSERT INTO category VALUES (18, 'Поло', 6);
INSERT INTO category VALUES (19, 'С длинными рукавами', 7);
INSERT INTO category VALUES (20, 'С короткими рукавами', 7);

INSERT INTO product_category VALUES (1, 1, 17);
INSERT INTO product_category VALUES (2, 1, 16);
INSERT INTO product_category VALUES (3, 2, 20);
INSERT INTO product_category VALUES (4, 3, 13);
INSERT INTO product_category VALUES (5, 6, 6);

INSERT INTO public.user (id, email, username, hashed_password, is_active, is_superuser, is_verified) VALUES (1, 'max.max@mail.com', 'max', '123456', True, True, True);

INSERT INTO public.product_sales_type (id, name) VALUES (1, 'asacsacsй');
INSERT INTO public.seller_product (id, product_id, salesman_id, price, discount, sale_type_id) VALUES (1, 1, 1, 5000, 0, 1);
INSERT INTO public.seller_product (id, product_id, salesman_id, price, discount, sale_type_id) VALUES (2, 1, 1, 5000, 0, 1);

INSERT INTO public.size_numbers (id, size) VALUES (1, 65);
INSERT INTO public.size_letter (id, size) VALUES (1, 'm');

INSERT INTO public.size (id, size_numbers_id, size_letter_id, affiliation_id) VALUES (1, 1, 1, 1);

INSERT INTO public.seller_products_size (id, product_id, size_numbers_id, size_letter_id, quantity) VALUES (1, 1, 1, 1, 50);