drop table if exists gitrepo;
create table gitrepo (
       id int(11) not null auto_increment,
       name varchar(4096) default null,
       node_id varchar(40) default null unique,
       html_url varchar(4096) default null,
       description varchar(4096) default null,
       updated_at datetime not null default current_timestamp,
       pushed_at datetime not null default current_timestamp,
       created_at datetime not null default current_timestamp,
       primary key(id)
) ENGINE=InnoDB default charset=utf8mb4;
