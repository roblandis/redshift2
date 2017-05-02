#redhsift look at active tables
select distinct(tablename) from pg_table_def where schemaname = 'public';

#basic version set to keep live
select version();

#do this for slow loads
set wlm_query_slot_count to 2;