--- 3月3日 
use bytedance;
CREATE TABLE `course` (
  `ID` char(3) NOT NULL,
  `course` char(30) NOT NULL,
  `type` char(10) NOT NULL,
  `credit` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) 

CREATE TABLE `foreign_teacher` (
  `tid` varchar(6) NOT NULL,
  `tname` varchar(20) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `country` varchar(30) NOT NULL,
  `birth` datetime DEFAULT NULL,
  `hiredate` datetime DEFAULT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--- 创建数据库表
create table `runoob_tbl` (
    `runoob_id` int  unsigned auto_increment,
    `runoob_title` varchar(100) not null,
    `runoob_author` varchar(40) not null,
    `submission_data` date,
    PRIMARY KEY (`runoob_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table websites
create table `websites` (
    `id` int unsigned auto_increment,
    `name` varchar(25) not null,
    `url` varchar(100) not null,
    `alexa` int,
    `country` varchar(10),
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--- 查看表结构
desc runoob_tbl

--- 删除数据表
drop table runoob_tbl

--- 插入数据表
insert into runoob_tbl(runoob_title,runoob_author,submission_data)
VALUES
("学习mysql","学习菜鸟",now())

insert into runoob_tbl(runoob_title,runoob_author,submission_data)
VALUES
("Java教程","Runoob.com",'2023-03-03')



insert into runoob_tbl(runoob_title,runoob_author,submission_data)
VALUES
("学习 MySQL","菜鸟教程",'2017-04-12')




insert into websites(name,url,alexa,country)
VALUES
("stackoverflow","http://stackoverflow.com/ ",0,"IND")

insert into apps(app_name,url,country)
VALUES("淘宝 APP","https://www.taobao.com/","CN")

delete from websites where id = 4
--- 查询数据
select * from runoob_tbl

--- where子句
select * from runoob_tbl where runoob_title="Java教程"

--- update更新
update runoob_tbl set runoob_title = "Mysql学习" 
where runoob_id = 1 

--- delete语句
delete from runoob_tbl 
where runoob_id = 2

--- like 子句
select * from runoob_tbl where runoob_author like '%com'

--- union操作符 ----
select country from websites
union
select country from apps
order by country

--- union all
select country from websites
union all
select country from apps
order by country

--- 带where的sql union all
select country,name from websites
where country='CN'
union all
select country,app_name from apps
where country='CN'
order by country

--- 排序 ---
--- asc 升序   desc 降序
select * from runoob_tbl order by submission_data asc
select * from runoob_tbl order by submission_data desc

--- group by语句 ---
DROP TABLE IF EXISTS `employee_tbl`;
CREATE TABLE `employee_tbl` (
  `id` int(11) NOT NULL,
  `name` char(10) NOT NULL DEFAULT '',
  `date` datetime NOT NULL,
  `signin` tinyint(4) NOT NULL DEFAULT '0' COMMENT '登录次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `employee_tbl` VALUES ('1', '小明', '2016-04-22 15:25:33', '1'), ('2', '小王', '2016-04-20 15:25:47', '3'), ('3', '小丽', '2016-04-19 15:26:02', '2'), ('4', '小王', '2016-04-07 15:26:14', '4'), ('5', '小明', '2016-04-11 15:26:40', '4'), ('6', '小明', '2016-04-04 15:26:54', '2');

select name,count(*) from employee_tbl group by name

--- 使用with rollup
-- WITH ROLLUP 可以实现在分组统计数据基础上再进行相同的统计（SUM,AVG,COUNT…）。
select name,sum(signin) as signin_count from employee_tbl group by name with rollup

-- select coalesce(a,b,c);
-- 如果a==null,则选择b；如果b==null,则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（没意义）
SELECT coalesce(name, '总数'), SUM(signin) as signin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;

--- 连接的使用 ---
-- INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
-- LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
-- RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录
select * from runoob_tbl
select * from tcount_tbl

select a.runoob_id,a.runoob_author,b.runoob_count 
from runoob_tbl a 
inner join tcount_tbl b on a.runoob_author = b.runoob_author

-- where子句
select a.runoob_id,a.runoob_author,b.runoob_count
from runoob_tbl a,tcount_tbl b
where a.runoob_author = b.runoob_author

--- Left join
select a.runoob_id,a.runoob_author,b.runoob_count
from runoob_tbl a
Left join tcount_tbl b on a.runoob_author = b.runoob_author

--- Right join
select a.runoob_id,a.runoob_author,b.runoob_count
from runoob_tbl a
Right join tcount_tbl b on a.runoob_author = b.runoob_author

--- Null值处理 ---
drop table runoob_test_tbl 
create table runoob_test_tbl(
    runoob_author varchar(100) not null,
    runoob_count int
)
INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('RUNOOB', 20);
INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('中国',NULL)
INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('Google', NULL);
INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('FK', 20);

select * from runoob_test_tbl where runoob_count is null
select * from runoob_test_tbl where runoob_count is not null

--- 正则表达式 ---
-- ^：匹配输入字符串的开始位置
-- $：匹配输入字符串的结束位置

--- 事务 ---
CREATE TABLE runoob_transaction_test( id int(5)) engine=innodb; 
select * from runoob_transaction_test
begin
insert into runoob_transaction_test value(5)
insert into runoob_transaction_test value(6)
commit
select * from runoob_transaction_test
begin
insert into runoob_transaction_test values(8)
rollback
select * from 

--- alter命令 ---
create table testalter_tbl(
    i int,
    c char(1)
)
desc testalter_tbl
-- 删除，添加或修改表字段
alter table testalter_tbl drop i
alter table testalter_tbl add i int
ALTER TABLE testalter_tbl DROP i;
ALTER TABLE testalter_tbl ADD i INT FIRST;
ALTER TABLE testalter_tbl DROP i;
ALTER TABLE testalter_tbl ADD i INT AFTER c;
show columns from testalter_tbl
show columns from alter_tbl
-- 修改字段类型及名称
 alter table testalter_tbl modify c char(10);
 alter table testalter_tbl change i j bigint;
 alter table testalter_tbl change j j int;

 -- 对null和默认值的影响
 alter table testalter_tbl modify j bigint not null DEFAULT 100;

 -- 修改字段默认值
 alter table testalter_tbl alter i set DEFAULT 1000;
 alter table testalter_tbl alter i drop DEFAULT;

 alter table testalter_tbl engine = MYISAM;

 -- 修改表名
 alter table testalter_tbl rename to alter_tbl;

--- 索引 ---
-- 普通索引
create index cindex on alter_tbl(c)
alter table alter_tbl add index iindex(i)

-- 创建表的时候直接指定
create table mytable(
  ID int not null,
  username varchar(16) not null,
  index iindex(ID)
)

drop index iindex on mytable

-- 唯一索引
create unique index indexName on alter_tbl(i)
alter table alter_tbl add unique indexName(c)

CREATE TABLE mytable(  
ID INT NOT NULL,   
username VARCHAR(16) NOT NULL,  
UNIQUE [indexName] (username(length))  
);  

 ALTER TABLE testalter_tbl ADD INDEX (c);
 ALTER TABLE testalter_tbl DROP INDEX c;





