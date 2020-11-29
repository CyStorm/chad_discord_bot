CREATE TABLE IF NOT EXISTS members (
	global_id bigint unsigned NOT NULL PRIMARY KEY,
    display_name varchar(255),
    smooth_counter int unsigned
)