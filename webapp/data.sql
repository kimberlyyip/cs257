--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

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
-- Name: games; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE games (
    rank integer NOT NULL,
    bgg_url text,
    game_id integer,
    name text,
    min_player integer,
    max_player integer,
    avg_time integer,
    min_time integer,
    max_time integer,
    pub_year integer,
    avg_rating double precision,
    geek_rating double precision,
    num_votes integer,
    image_url text,
    min_age integer,
    mechanic text,
    num_owned integer,
    category text,
    designer text,
    weight double precision
);


--
-- Name: games_rank_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.games_rank_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: games_rank_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.games_rank_seq OWNED BY public.games.rank;


--
-- Name: games rank; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.games ALTER COLUMN rank SET DEFAULT nextval('public.games_rank_seq'::regclass);


--
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.games (rank, bgg_url, game_id, name, min_player, max_player, avg_time, min_time, max_time, pub_year, avg_rating, geek_rating, num_votes, image_url, min_age, mechanic, num_owned, category, designer, weight) FROM stdin;
1	https://boardgamegeek.com/boardgame/13/catan	13	Catan	3	4	120	60	120	1995	7.22355	7.07593	77423	https://cf.geekdo-images.com/original/img/A-0yDJkve0avEicYQ4HoNO-HkK8=/0x0/pic2419375.jpg	10	Dice Rolling, Hand Management, Modular Board, Route/Network Building, Trading	111807	Negotiation	Klaus Teuber	2.3488
2	https://boardgamegeek.com/boardgame/121288/dixit-journey	121288	Dixit: Journey	3	6	30	30	30	2012	7.46076	6.97033	3712	https://cf.geekdo-images.com/original/img/ZkIVkgiw7QLXTL0kFiRvCbBrl48=/0x0/pic1387599.jpg	8	Acting, Simultaneous Action Selection, Storytelling, Voting	6805	Card Game, Humor, Party Game	Jean-Louis Roubira	1.304
3	https://boardgamegeek.com/boardgame/58281/summoner-wars	58281	Summoner Wars	2	4	60	30	60	2009	7.30814	6.96596	5480	https://cf.geekdo-images.com/original/img/1cfLD-e4_bfT9z2RdIV4APAs0rM=/0x0/pic2407328.jpg	9	Action Point Allowance System, Dice Rolling, Grid Movement, Hand Management, Take That, Variable Player Powers	5117	Card Game, Fantasy, Fighting	Colby Dauch	2.3103
4	https://boardgamegeek.com/boardgame/131357/coup	131357	Coup	2	6	15	15	15	2012	7.07221	6.95648	25574	https://cf.geekdo-images.com/original/img/4zmqrQ4v-rufRQM_oinFDQ6HykI=/0x0/pic2016054.jpg	9	Memory, Player Elimination, Take That, Variable Player Powers	41411	Bluffing, Card Game, Deduction, Party Game, Political	Rikki Tahta	1.4235
5	https://boardgamegeek.com/boardgame/2093/mahjong	2093	Mahjong	3	4	120	120	120	1850	7.01416	6.70213	5398	https://cf.geekdo-images.com/original/img/yxjA4SS4-6j9NgMmhLCtz0KGpWM=/0x0/pic43709.jpg	8	Hand Management, Set Collection	7432	Abstract Strategy	(Uncredited)	2.5442
6	https://boardgamegeek.com/boardgame/30618/eat-poop-you-cat	30618	Eat Poop You Cat	3	99	20	20	20	1984	7.49409	6.64038	1455	https://cf.geekdo-images.com/original/img/hjqVjXQNcBn1Lsxxp1cGLtSVeHk=/0x0/pic611630.jpg	0	Paper-and-Pencil	742	Humor, Party Game	(Uncredited)	1.1204
7	https://boardgamegeek.com/boardgame/66056/rivals-catan	66056	Rivals for Catan	2	2	120	45	120	2010	7.0429	6.68833	4352	https://cf.geekdo-images.com/original/img/bYM2AcTF4y0jXsx3BzDk6oBh0Yw=/0x0/pic3736568.jpg	10	Card Drafting, Dice Rolling, Hand Management	9155	Card Game, City Building, Medieval, Territory Building	Klaus Teuber	2.3138
8	https://boardgamegeek.com/boardgame/207830/5-minute-dungeon	207830	5-Minute Dungeon	2	5	30	5	30	2017	7.38778	6.62821	2158	https://cf.geekdo-images.com/original/img/44rTOeM8WiW-rOnrFdeKXdD_4Lg=/0x0/pic3213622.png	8	Co-operative Play, Hand Management, Variable Player Powers	4079	Card Game, Fantasy, Fighting, Real-time	Connor Reid	1.0984
9	https://boardgamegeek.com/boardgame/233371/clank-space	233371	Clank! In! Space!	2	4	60	60	60	2017	8.01024	7.20743	2593	https://cf.geekdo-images.com/original/img/fABHPKiMqPXzFg5fgybJSJkpMuY=/0x0/pic3720843.jpg	13	Card Drafting, Deck / Pool Building, Modular Board, Player Elimination, Point to Point Movement, Press Your Luck	4797	Science Fiction	Paul Dennen	2.6
10	https://boardgamegeek.com/boardgame/150376/dead-winter-crossroads-game	150376	Dead of Winter: A Crossroads Game	2	5	120	60	120	2014	7.74899	7.60396	28885	https://cf.geekdo-images.com/original/img/pOYQOSR1CnXcN6pEPx3yFDjKFaA=/0x0/pic3016500.jpg	13	Action Point Allowance System, Area Movement, Co-operative Play, Dice Rolling, Hand Management, Press Your Luck, Storytelling, Trading, Variable Player Powers, Voting	39714	Bluffing, Deduction, Horror, Zombies	Jonathan Gilmour, Isaac Vega	3.0008
\.


--
-- Name: games_rank_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.games_rank_seq', 1, false);


--
-- PostgreSQL database dump complete
--

