-- ******************* ADMINS
create table admins(
    admin_id integer primary key,
    username text unique,
    password char(34),
    deposit numeric(12,2) default 0,
    due numeric(12,2) default 0,
    name text,
    comment text,
    creator_id integer,
    active boolean default 't'
);   

create sequence admins_id_seq;

create table admins_extended_attrs(
    admin_id integer references admins,
    attr_name text,
    attr_value text
);

create table admin_locks(
    lock_id bigint,
    locker_admin_id integer references admins,
    admin_id integer references admins,
    reason text
);

create sequence admin_locks_lock_id_seq;

create table admin_perms (
    admin_id integer references admins,
    perm_name text,
    perm_value text
);

create table admin_perm_templates (
    template_id integer primary key,
    template_name text
);

create sequence admin_perm_template_id;

create table admin_perm_templates_detail (
    template_id integer references admin_perm_templates,
    perm_name text,
    perm_value text
);

-- ****************** IP POOLS
create table ippool(
    ippool_id integer primary key,
    ippool_name text,
    ippool_comment	text
);

create sequence ippool_id_seq;

create table ippool_ips(
    ippool_id integer references ippool,
    ip	inet
);

-- *********************** RAS
create table ras (
    ras_id integer primary key,
    ras_ip inet,
    ras_type text,
    radius_secret text,
    active boolean default 't'    
);
create sequence ras_id_seq;

create table ras_ports (
    ras_id integer references ras,
    port_name text,
    phone text,
    type text,
    comment text
);
create unique index ras_ports_index on ras_ports (ras_id,port_name);

create table ras_attrs (
    ras_id integer references ras,
    attr_name text,
    attr_value text
);

create table ras_ippools (
    ras_id integer references ras,
    ippool_id integer references ippool
);

create unique index ras_attrs_index on ras_attrs (ras_id,attr_name);

-- ******************* CHARGES ***********
create table charges (
    charge_id integer primary key,
    name text unique,
    charge_type text, --'internet' or 'voip'
    comment text,
    admin_id integer references admins ,
    visible_to_all boolean default 'FALSE'
);

create sequence charges_id_seq;
create sequence charge_rules_id_seq; --used for both voip and internet rules

create table charge_rules (
    charge_id integer references charges,
    charge_rule_id integer primary key,
    start_time time,
    end_time time,
    time_limit integer, -- in minutes
    ras_id integer references ras
);


create table internet_charge_rules (
    transfer_limit integer, -- in kbytes
    cpm numeric(12,2),
    cpk numeric(12,2),
    assumed_kps integer,
    bandwidth_limit_kbytes integer default -1
) inherits (charge_rules);


create table charge_rule_ports (
    charge_rule_id integer,
    ras_port text
);

create table charge_rule_day_of_weeks (
    charge_rule_id integer,
    day_of_week integer
);

-- ******************
create table groups (
    group_id integer primary key,
    group_name text,
    owner_id integer references admins,
    comment text
);

create sequence groups_group_id_seq;

create table group_attrs (
    group_id integer references groups,
    attr_name text,
    attr_value text
);

-- *************** USERS
create table users (
    user_id bigint primary key,
    owner_id integer references admins,
    credit numeric(12,2),
    group_id integer ,
    creation_date timestamp without time zone default CURRENT_TIMESTAMP
);

create table normal_users (
    user_id integer references users,
    normal_username text primary key, 
    normal_password text
);

create sequence add_user_save_id_seq;

create table add_user_saves(
    add_user_save_id integer primary key,
    add_date	timestamp without time zone default CURRENT_TIMESTAMP,
    admin_id	integer references admins,
    type	integer, --1:Normal 2:VoIP
    comment	text
);

create table add_user_save_details(
    add_user_save_id integer references add_user_saves,
    user_id bigint,
    username text,
    password text
);

create table voip_users (
    user_id bigint references users,
    voip_username text primary key, 
    voip_password text
);

create sequence users_user_id_seq;

create table user_locks(
    lock_id bigint primary key,
    admin_id integer references admins,
    user_id bigint references users,
    reason text
);

create sequence user_locks_lock_id_seq;

--    dayusage integer default 0,
--    daylimit integer default -1,
--    mail_quota_kbytes integer default 0,
--    has_email bool default 'f',
--    multi_login integer default -1,
--    rel_exp_date integer default -1,
--    first_login timestamp without time zone default null,
--    abs_exp_date timestamp without time zone not null,
--    has_normal bool,
--    has_voip bool,
--    has_mail bool,
--    name  text,
--    tel text ,
--    comment text ,
--    email_address text ,
--    charge id

create table user_attrs (
    user_id integer references users,
    attr_name text,
    attr_value text
);

create index user_attrs_user_id_index on user_attrs(user_id);
-- ************************ CONFIGURATION

create table defs (
    name text unique,
    value text,
    type text    
);

create table ibs_states(
    name text unique,
    value text
);

-- *********************** LOGS


create table credit_change (
    credit_change_id bigint primary key,
    admin_id integer,
    action smallint,
    per_user_credit numeric(12,2),
    admin_credit numeric(12,2),
    change_time timestamp without time zone default CURRENT_TIMESTAMP,
    remote_addr inet,
    comment text
);

create table credit_change_userid (
    credit_change_id bigint references credit_change,
    user_id integer
);

create index credit_change_userid_index on credit_change_userid (user_id);
create sequence credit_change_id;




create table connection_log (
    connection_log_id bigint primary key,
    user_id integer,
    credit_used numeric(12,2),
    login_time timestamp,
    logout_time	timestamp,
    successful bool,
    service smallint,--1 internet , 2- voip
    ras_id integer
);

create table connection_log_details (
    connection_log_id bigint references connection_log,
    name text, 
    value text
);

create index connection_log_details_userid_index on connection_log_details (user_id);
create sequence connection_log_id;


-- ********************* TO BE CHECKED!
create table admin_deposit_log(
    admin_id integer,
    to_admin_id integer,
    credit numeric(12,2),
    paid_money numeric(12,2),
    change_time timestamp without time zone default CURRENT_TIMESTAMP,
    remote_addr inet,
    comment text
);

create table internet_connection_log (
    username text,
    ras_id integer,
    port text,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    caller_id text,
    credit_used numeric(12,2),
    in_bytes	bigint,
    out_bytes   bigint,
    successful boolean,
    reason text
);


