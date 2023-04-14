-- 4.1 --

CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

CREATE TABLE movie_info (
	Movie_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(100),
    Movie_Length TIME,
    Age_Rating VARCHAR(4));

CREATE TABLE screens (
	Screen_ID INT PRIMARY KEY,
    Four_K bool);

CREATE TABLE showings (
	Showing_ID INT PRIMARY KEY,
    Movie_ID int,
    Screen_ID int,
    Start_Time TIME,
    Available_Seats INT,
    FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
    FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
    );

-- 4.2 --
use foundation_assessment_ii;

select * from movie_info;
select * from screens;
select * from showings;

select m.movie_name, sh.start_time
from movie_info m
inner join showings sh
on m.movie_id = sh.movie_id
where sh.start_time > '12:00:00'
and sh.available_seats > 1
order by sh.start_time;

--4.3--
select movie_name from movie_info
where movie_id in (select movie_id, sum(movie_id) from showings
group by movie_id
order by sum(movie_id) desc
limit 1);