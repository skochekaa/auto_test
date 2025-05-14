-- Добавляем студента
insert into students (name, second_name)
values ('John', 'Wick');

-- Добавляем книги
insert into books (title, taken_by_student_id)
values
	('IPSC', 20148),
    ('My bbok', 20148),
    ('Startrack', 20148);

-- Добавляем группу
insert into `groups` (title, start_date, end_date)
values ('Practical shooting', '2020-01-01', '2020-06-01');

-- Обновляем запись студента, добавляем отношение к группе
update students
set group_id = (
  select id
  from `groups`
  where title = 'Practical shooting'
)
where name = 'John' and second_name = 'Wick'
limit 1;

-- Создаем несколько учебных предметов
insert into subjets (title)
values
	('Ptactic'),
    ('Safe handling'),
    ('Theory');

-- Создаем по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id)
values
	('Стрельба стоя', (
		select id
        from subjets
        where title = 'Ptactic'
        )
	),
    ('Стрельба в движении', (
		select id
        from subjets
        where title = 'Ptactic'
        )
	),
    ('ОБ 1', (
		select id
        from subjets
        where title = 'Safe handling'
        )
	),
    ('ОБ 2', (
		select id
        from subjets
        where title = 'Safe handling'
        )
	),
    ('Правила', (
		select id
        from subjets
        where title = 'Theory'
        )
	),
    ('Экзамен', (
		select id
        from subjets
        where title = 'Theory'
        )
	);

-- Ставим своему студенту оценки (marks) для всех созданных вами занятий
insert into marks (`value`, lesson_id, student_id)
values
	('5', (
		select id
        from lessons
        where title = 'Стрельба стоя'
		),
        (
        select id
        from students
        where name = 'John' and second_name = 'Wick'
        )
 	),
    ('5', (
		select id
        from lessons
        where title = 'Стрельба в движении'
		),
        (
        select id
        from students
        where name = 'John' and second_name = 'Wick'
        )
	),
    ('5', (
		select id
        from lessons
        where title = 'ОБ 1'
		),
        (
        select id
        from students
        where name = 'John' and second_name = 'Wick'
        )
	),
    ('5', (
		select id
        from lessons
        where title = 'ОБ 2'
		),
        (
        select id
        from students
        where name = 'John' and second_name = 'Wick'
        )
	),
    ('5', (
		select id
        from lessons
        where title = 'Правила'
		),
        (
        select id
        from students
        where name = 'John' and second_name = 'Wick'
        )
	),
    ('5', (
		select id
        from lessons
        where title = 'Экзамен'
		),
        (
        select id
        from students
        where name = 'John' and second_name = 'Wick'
        )
	);

-- Получаем все оценки студента
select `value` as 'Оценки Джона'
from marks
where student_id = (
	select id
	from students
	where name = 'John' and second_name = 'Wick'
    );

-- Получаем все книги, которые находятся у студента
select title as 'Книги у Джона'
from books
where taken_by_student_id = (
	select id
	from students
	where name = 'John' and second_name = 'Wick'
    );

-- Выводим все что есть о студенте
select *
from students
join books on students.id = books.taken_by_student_id
join `groups` on students.group_id = `groups`.id
join marks on students.id = marks.student_id
join lessons on marks.lesson_id = lessons.id
join subjets on lessons.subject_id = subjets.id
where name = 'John' and second_name = 'Wick'
