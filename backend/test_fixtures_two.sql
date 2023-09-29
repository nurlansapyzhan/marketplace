--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Ubuntu 15.1-1.pgdg22.04+1)
-- Dumped by pg_dump version 15.1 (Ubuntu 15.1-1.pgdg22.04+1)

-- Started on 2023-09-29 13:59:33 +06

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 232 (class 1259 OID 63050)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 62923)
-- Name: brand; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.brand (
    id integer NOT NULL,
    brand_name character varying NOT NULL
);


ALTER TABLE public.brand OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 62922)
-- Name: brand_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.brand_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.brand_id_seq OWNER TO postgres;

--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 214
-- Name: brand_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.brand_id_seq OWNED BY public.brand.id;


--
-- TOC entry 217 (class 1259 OID 62933)
-- Name: collection; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.collection (
    id integer NOT NULL,
    name character varying NOT NULL,
    created_at timestamp without time zone,
    added_db_at timestamp without time zone
);


ALTER TABLE public.collection OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 62932)
-- Name: collection_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.collection_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collection_id_seq OWNER TO postgres;

--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 216
-- Name: collection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.collection_id_seq OWNED BY public.collection.id;


--
-- TOC entry 219 (class 1259 OID 62943)
-- Name: color; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.color (
    id integer NOT NULL,
    color_name character varying NOT NULL,
    number_color integer NOT NULL
);


ALTER TABLE public.color OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 62942)
-- Name: color_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.color_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.color_id_seq OWNER TO postgres;

--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 218
-- Name: color_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.color_id_seq OWNED BY public.color.id;


--
-- TOC entry 221 (class 1259 OID 62953)
-- Name: compound; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.compound (
    id integer NOT NULL,
    compound_name character varying NOT NULL
);


ALTER TABLE public.compound OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 62952)
-- Name: compound_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.compound_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.compound_id_seq OWNER TO postgres;

--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 220
-- Name: compound_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.compound_id_seq OWNED BY public.compound.id;


--
-- TOC entry 223 (class 1259 OID 62963)
-- Name: pattern; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pattern (
    id integer NOT NULL,
    patterns_name character varying NOT NULL
);


ALTER TABLE public.pattern OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 62962)
-- Name: pattern_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pattern_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pattern_id_seq OWNER TO postgres;

--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 222
-- Name: pattern_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pattern_id_seq OWNED BY public.pattern.id;


--
-- TOC entry 227 (class 1259 OID 62983)
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    id integer NOT NULL,
    name character varying NOT NULL,
    brand_id integer,
    description character varying,
    color_id integer,
    product_rating double precision,
    number_of_reviews integer,
    compound_id integer,
    pattern_id integer,
    season_id integer,
    collection_id integer,
    created_at timestamp without time zone,
    added_db_at timestamp without time zone
);


ALTER TABLE public.product OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 62982)
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO postgres;

--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 226
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- TOC entry 229 (class 1259 OID 63023)
-- Name: role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.role (
    id integer NOT NULL,
    name character varying NOT NULL,
    permissions json
);


ALTER TABLE public.role OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 63022)
-- Name: role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.role_id_seq OWNER TO postgres;

--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 228
-- Name: role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.role_id_seq OWNED BY public.role.id;


--
-- TOC entry 225 (class 1259 OID 62973)
-- Name: season; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.season (
    id integer NOT NULL,
    seasons_name character varying NOT NULL
);


ALTER TABLE public.season OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 62972)
-- Name: season_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.season_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.season_id_seq OWNER TO postgres;

--
-- TOC entry 3480 (class 0 OID 0)
-- Dependencies: 224
-- Name: season_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.season_id_seq OWNED BY public.season.id;


--
-- TOC entry 231 (class 1259 OID 63032)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying NOT NULL,
    username character varying NOT NULL,
    registered_at timestamp without time zone,
    role_id integer,
    hashed_password character varying NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    is_verified boolean NOT NULL
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 63031)
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO postgres;

--
-- TOC entry 3481 (class 0 OID 0)
-- Dependencies: 230
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- TOC entry 3264 (class 2604 OID 62926)
-- Name: brand id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.brand ALTER COLUMN id SET DEFAULT nextval('public.brand_id_seq'::regclass);


--
-- TOC entry 3265 (class 2604 OID 62936)
-- Name: collection id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.collection ALTER COLUMN id SET DEFAULT nextval('public.collection_id_seq'::regclass);


--
-- TOC entry 3266 (class 2604 OID 62946)
-- Name: color id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.color ALTER COLUMN id SET DEFAULT nextval('public.color_id_seq'::regclass);


--
-- TOC entry 3267 (class 2604 OID 62956)
-- Name: compound id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compound ALTER COLUMN id SET DEFAULT nextval('public.compound_id_seq'::regclass);


--
-- TOC entry 3268 (class 2604 OID 62966)
-- Name: pattern id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pattern ALTER COLUMN id SET DEFAULT nextval('public.pattern_id_seq'::regclass);


--
-- TOC entry 3270 (class 2604 OID 62986)
-- Name: product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- TOC entry 3271 (class 2604 OID 63026)
-- Name: role id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role ALTER COLUMN id SET DEFAULT nextval('public.role_id_seq'::regclass);


--
-- TOC entry 3269 (class 2604 OID 62976)
-- Name: season id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season ALTER COLUMN id SET DEFAULT nextval('public.season_id_seq'::regclass);


--
-- TOC entry 3272 (class 2604 OID 63035)
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- TOC entry 3467 (class 0 OID 63050)
-- Dependencies: 232
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alembic_version (version_num) VALUES ('c0f44759455b');


--
-- TOC entry 3450 (class 0 OID 62923)
-- Dependencies: 215
-- Data for Name: brand; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.brand (id, brand_name) VALUES (1, 'adsasas');


--
-- TOC entry 3452 (class 0 OID 62933)
-- Dependencies: 217
-- Data for Name: collection; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.collection (id, name, created_at, added_db_at) VALUES (1, 'jljasasalkjl', NULL, NULL);


--
-- TOC entry 3454 (class 0 OID 62943)
-- Dependencies: 219
-- Data for Name: color; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.color (id, color_name, number_color) VALUES (1, 'jljlkjl', 1);


--
-- TOC entry 3456 (class 0 OID 62953)
-- Dependencies: 221
-- Data for Name: compound; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.compound (id, compound_name) VALUES (1, 'jljasasalkjl');


--
-- TOC entry 3458 (class 0 OID 62963)
-- Dependencies: 223
-- Data for Name: pattern; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pattern (id, patterns_name) VALUES (1, 'jljaasasasassasalkjl');


--
-- TOC entry 3462 (class 0 OID 62983)
-- Dependencies: 227
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at) VALUES (1, 'jljlkjl', 1, 'asdasasasda', 1, 1, 1, 1, 1, 1, 1, NULL, NULL);
INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at) VALUES (2, 'string', 1, 'string', 1, 1, NULL, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53');
INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at) VALUES (3, 'string', 1, 'string', 1, 1, NULL, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53');
INSERT INTO public.product (id, name, brand_id, description, color_id, product_rating, number_of_reviews, compound_id, pattern_id, season_id, collection_id, created_at, added_db_at) VALUES (6, 'string', 1, 'string', 1, 1, NULL, 1, 1, 1, 1, '2023-09-22 11:12:41.53', '2023-09-22 11:12:41.53');


--
-- TOC entry 3464 (class 0 OID 63023)
-- Dependencies: 229
-- Data for Name: role; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3460 (class 0 OID 62973)
-- Dependencies: 225
-- Data for Name: season; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.season (id, seasons_name) VALUES (1, 'jljlkjl');


--
-- TOC entry 3466 (class 0 OID 63032)
-- Dependencies: 231
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3482 (class 0 OID 0)
-- Dependencies: 214
-- Name: brand_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.brand_id_seq', 1, false);


--
-- TOC entry 3483 (class 0 OID 0)
-- Dependencies: 216
-- Name: collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.collection_id_seq', 1, false);


--
-- TOC entry 3484 (class 0 OID 0)
-- Dependencies: 218
-- Name: color_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.color_id_seq', 1, false);


--
-- TOC entry 3485 (class 0 OID 0)
-- Dependencies: 220
-- Name: compound_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.compound_id_seq', 1, false);


--
-- TOC entry 3486 (class 0 OID 0)
-- Dependencies: 222
-- Name: pattern_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pattern_id_seq', 1, false);


--
-- TOC entry 3487 (class 0 OID 0)
-- Dependencies: 226
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_seq', 1, false);


--
-- TOC entry 3488 (class 0 OID 0)
-- Dependencies: 228
-- Name: role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.role_id_seq', 1, false);


--
-- TOC entry 3489 (class 0 OID 0)
-- Dependencies: 224
-- Name: season_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.season_id_seq', 1, false);


--
-- TOC entry 3490 (class 0 OID 0)
-- Dependencies: 230
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 1, false);


--
-- TOC entry 3299 (class 2606 OID 63054)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3274 (class 2606 OID 62930)
-- Name: brand brand_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.brand
    ADD CONSTRAINT brand_pkey PRIMARY KEY (id);


--
-- TOC entry 3277 (class 2606 OID 62940)
-- Name: collection collection_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.collection
    ADD CONSTRAINT collection_pkey PRIMARY KEY (id);


--
-- TOC entry 3280 (class 2606 OID 62950)
-- Name: color color_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.color
    ADD CONSTRAINT color_pkey PRIMARY KEY (id);


--
-- TOC entry 3283 (class 2606 OID 62960)
-- Name: compound compound_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compound
    ADD CONSTRAINT compound_pkey PRIMARY KEY (id);


--
-- TOC entry 3287 (class 2606 OID 62970)
-- Name: pattern pattern_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pattern
    ADD CONSTRAINT pattern_pkey PRIMARY KEY (id);


--
-- TOC entry 3293 (class 2606 OID 62990)
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- TOC entry 3295 (class 2606 OID 63030)
-- Name: role role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);


--
-- TOC entry 3290 (class 2606 OID 62980)
-- Name: season season_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season
    ADD CONSTRAINT season_pkey PRIMARY KEY (id);


--
-- TOC entry 3297 (class 2606 OID 63039)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- TOC entry 3275 (class 1259 OID 62931)
-- Name: ix_brand_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_brand_id ON public.brand USING btree (id);


--
-- TOC entry 3278 (class 1259 OID 62941)
-- Name: ix_collection_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_collection_id ON public.collection USING btree (id);


--
-- TOC entry 3281 (class 1259 OID 62951)
-- Name: ix_color_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_color_id ON public.color USING btree (id);


--
-- TOC entry 3284 (class 1259 OID 62961)
-- Name: ix_compound_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_compound_id ON public.compound USING btree (id);


--
-- TOC entry 3285 (class 1259 OID 62971)
-- Name: ix_pattern_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_pattern_id ON public.pattern USING btree (id);


--
-- TOC entry 3291 (class 1259 OID 63021)
-- Name: ix_product_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_product_id ON public.product USING btree (id);


--
-- TOC entry 3288 (class 1259 OID 62981)
-- Name: ix_season_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_season_id ON public.season USING btree (id);


--
-- TOC entry 3300 (class 2606 OID 62991)
-- Name: product product_brand_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_brand_id_fkey FOREIGN KEY (brand_id) REFERENCES public.brand(id);


--
-- TOC entry 3301 (class 2606 OID 62996)
-- Name: product product_collection_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_collection_id_fkey FOREIGN KEY (collection_id) REFERENCES public.collection(id);


--
-- TOC entry 3302 (class 2606 OID 63001)
-- Name: product product_color_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_color_id_fkey FOREIGN KEY (color_id) REFERENCES public.color(id);


--
-- TOC entry 3303 (class 2606 OID 63006)
-- Name: product product_compound_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_compound_id_fkey FOREIGN KEY (compound_id) REFERENCES public.compound(id);


--
-- TOC entry 3304 (class 2606 OID 63011)
-- Name: product product_pattern_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pattern_id_fkey FOREIGN KEY (pattern_id) REFERENCES public.pattern(id);


--
-- TOC entry 3305 (class 2606 OID 63016)
-- Name: product product_season_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_season_id_fkey FOREIGN KEY (season_id) REFERENCES public.season(id);


--
-- TOC entry 3306 (class 2606 OID 63040)
-- Name: user user_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.role(id);


-- Completed on 2023-09-29 13:59:34 +06

--
-- PostgreSQL database dump complete
--

