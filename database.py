
import datetime
import random
import sqlite3 as sql

conn = sql.connect('database.db')


conn.execute("CREATE TABLE branch ( \
	branch_id	TEXT NOT NULL, \
	location	TEXT,  \
	PRIMARY KEY(branch_id) \
);")


conn.execute("CREATE TABLE stakeholder ( \
	customer_id	TEXT, \
	name	TEXT, \
	contact_no	TEXT NOT NULL, \
	Type	TEXT, \
	password	TEXT, \
	PRIMARY KEY(contact_no)  \
);")



    

branch_insertion = [
"INSERT INTO branch (branch_id , location) values \
('b0000','Girinagar');",
"INSERT INTO branch (branch_id , location) values \
('b0001','Kathripugge');",
"INSERT INTO branch (branch_id , location) values \
('b0002','Hosakerehalli');",
"INSERT INTO branch (branch_id , location) values \
('b0003','Arekere');",
"INSERT INTO branch (branch_id , location) values \
('b0004','Silk Board');",
"INSERT INTO branch (branch_id , location) values \
('b0005','Ashok Nagar');",
"INSERT INTO branch (branch_id , location) values \
('b0006','Jayanagar');",
"INSERT INTO branch (branch_id , location) values \
('b0007','Marathalli');",
"INSERT INTO branch (branch_id , location) values \
('b0008','Koramangala');",
"INSERT INTO branch (branch_id , location) values \
('b0009','HRBR Layout');"
]


for i in branch_insertion:
    conn.execute(i)
    conn.commit()

stakeholder_insertion = [
"INSERT INTO stakeholder values        ('ei','gfvma','9999900001','A','lk6i5oh');",
"INSERT INTO stakeholder values        ('nw','rpsfn','9999900002','A','fy3k7zi');",
"INSERT INTO stakeholder values        ('hu','xgrve','9999900003','A','bs9d4ac');",
"INSERT INTO stakeholder values        ('kt','dozqy','9999900004','L','uu5v0au');",
"INSERT INTO stakeholder values        ('ic','qydpo','9999900005','L','dw8w7hi');",
"INSERT INTO stakeholder values        ('xo','xnbdl','9999900006','B','lu2n6eo');",
"INSERT INTO stakeholder values        ('co','bseuo','9999900007','B','oz1r9cn');",
"INSERT INTO stakeholder values        ('js','sqzhq','9999900008','A','rc3j5yp');",
"INSERT INTO stakeholder values        ('pc','uweqe','9999900009','B','sz4b3px');",
"INSERT INTO stakeholder values        ('mf','julri','9999900010','A','qx1b2vw');",
"INSERT INTO stakeholder values        ('sw','loplg','9999900011','L','cz0v1hv');",
"INSERT INTO stakeholder values        ('cz','nfnev','9999900012','B','lf2b3dq');",
"INSERT INTO stakeholder values        ('dg','tfszr','9999900013','O','oq8e8pl');",
"INSERT INTO stakeholder values        ('df','jckuk','9999900014','L','mm2p6zc');",
"INSERT INTO stakeholder values        ('ng','xjrkg','9999900015','B','mb9q2ih');",
"INSERT INTO stakeholder values        ('kg','cdnmz','9999900016','O','qh7p2ni');",
"INSERT INTO stakeholder values        ('ib','qwfrq','9999900017','L','xj6d2at');",
"INSERT INTO stakeholder values        ('lb','noisc','9999900018','O','cl1q5ml');",
"INSERT INTO stakeholder values        ('no','sodgr','9999900019','L','ih0d4xk');",
"INSERT INTO stakeholder values        ('fi','eearn','9999900020','O','gq2x9le');",
"INSERT INTO stakeholder values        ('ki','xrdor','9999900021','A','rb7p6hn');",
"INSERT INTO stakeholder values        ('fn','ghzsq','9999900022','L','kw7q7ye');",
"INSERT INTO stakeholder values        ('kz','yotba','9999900023','L','us2o0zk');",
"INSERT INTO stakeholder values        ('of','uphvr','9999900024','O','yq7v4in');",
"INSERT INTO stakeholder values        ('ke','kdcik','9999900025','B','rv7o8xu');",
"INSERT INTO stakeholder values        ('wp','znzpa','9999900026','O','ka6p6hw');",
"INSERT INTO stakeholder values        ('sv','rrwva','9999900027','B','pq0g2wg');",
"INSERT INTO stakeholder values        ('ul','qhegm','9999900028','O','lc0k5zh');",
"INSERT INTO stakeholder values        ('lq','gmtpr','9999900029','B','vt9i4xa');",
"INSERT INTO stakeholder values        ('sz','beain','9999900030','B','zf8c8bt');",
"INSERT INTO stakeholder values        ('dd','anptu','9999900031','B','qg2w3np');",
"INSERT INTO stakeholder values        ('fl','zvmso','9999900032','L','dd3n9qf');",
"INSERT INTO stakeholder values        ('yp','wcqyg','9999900033','B','ak3q8rc');",
"INSERT INTO stakeholder values        ('dx','agyxs','9999900034','B','pj5v9av');",
"INSERT INTO stakeholder values        ('zs','zwjil','9999900035','O','gh3e7tc');",
"INSERT INTO stakeholder values        ('km','zzgvp','9999900036','O','nb2d3to');",
"INSERT INTO stakeholder values        ('ay','htkvg','9999900037','B','jl8h7uz');",
"INSERT INTO stakeholder values        ('px','bfwlm','9999900038','L','ql6c0rr');",
"INSERT INTO stakeholder values        ('db','clajc','9999900039','B','gh2o9mf');",
"INSERT INTO stakeholder values        ('pl','uzzvi','9999900040','L','rm0d0bj');",
"INSERT INTO stakeholder values        ('fc','drqqe','9999900041','A','mu3i5uz');",
"INSERT INTO stakeholder values        ('ge','oorvp','9999900042','O','qa8v3xj');",
"INSERT INTO stakeholder values        ('zy','urxrf','9999900043','B','vt5u7sq');",
"INSERT INTO stakeholder values        ('uc','kkxjm','9999900044','A','km6b7yu');",
"INSERT INTO stakeholder values        ('kj','teqgn','9999900045','L','eh3h9dp');",
"INSERT INTO stakeholder values        ('wj','oiptq','9999900046','O','hk0a9dk');",
"INSERT INTO stakeholder values        ('dj','lcnau','9999900047','L','fa4b1md');",
"INSERT INTO stakeholder values        ('oj','kufma','9999900048','B','qj0s1fc');",
"INSERT INTO stakeholder values        ('aa','bkxof','9999900049','A','cj3n8tf');",
"INSERT INTO stakeholder values        ('dr','hgtva','9999900050','A','pm8w5gu');",
"INSERT INTO stakeholder values        ('ar','szlmf','9999900051','L','kb8o9yt');",
"INSERT INTO stakeholder values        ('pw','qildt','9999900052','A','ym4z5uz');",
"INSERT INTO stakeholder values        ('ij','lrxky','9999900053','A','ti1x8tq');",
"INSERT INTO stakeholder values        ('ks','xhsmy','9999900054','L','re1k1aa');",
"INSERT INTO stakeholder values        ('qn','crqdt','9999900055','O','et5w5po');",
"INSERT INTO stakeholder values        ('yx','szhlh','9999900056','B','is4c6hz');",
"INSERT INTO stakeholder values        ('te','kvwfm','9999900057','A','iz9r2qa');",
"INSERT INTO stakeholder values        ('fk','avpll','9999900058','B','gi7k3jc');",
"INSERT INTO stakeholder values        ('cs','xehoe','9999900059','L','xh9e9iw');",
"INSERT INTO stakeholder values        ('bu','artui','9999900060','A','li4k7uj');",
"INSERT INTO stakeholder values        ('qf','ysifo','9999900061','O','dp9a2rh');",
"INSERT INTO stakeholder values        ('ww','edtpd','9999900062','O','ls6x5ud');",
"INSERT INTO stakeholder values        ('dj','hvife','9999900063','A','fm2b8fi');",
"INSERT INTO stakeholder values        ('qe','rjfbz','9999900064','L','mf8w8pw');",
"INSERT INTO stakeholder values        ('vz','dujfu','9999900065','B','ix4q3vm');",
"INSERT INTO stakeholder values        ('sk','oemzj','9999900066','A','yu5q3mi');",
"INSERT INTO stakeholder values        ('sp','jnedu','9999900067','O','jc2q2hz');",
"INSERT INTO stakeholder values        ('gh','cqyik','9999900068','A','wf2e2tf');",
"INSERT INTO stakeholder values        ('gn','sxdtx','9999900069','B','qw6u6xs');",
"INSERT INTO stakeholder values        ('fb','haxxx','9999900070','O','zq7s2bg');",
"INSERT INTO stakeholder values        ('ty','wqtdk','9999900071','L','jf8k9ax');",
"INSERT INTO stakeholder values        ('us','pyeqp','9999900072','B','gs4s5ux');",
"INSERT INTO stakeholder values        ('rc','bfgdw','9999900073','O','tp7o5nf');",
"INSERT INTO stakeholder values        ('up','txlte','9999900074','L','xc0x1dk');",
"INSERT INTO stakeholder values        ('pq','xwbql','9999900075','B','gb8t5yg');",
"INSERT INTO stakeholder values        ('go','fnlvh','9999900076','B','cm6p2ge');",
"INSERT INTO stakeholder values        ('ts','vbamm','9999900077','O','ex7c2kc');",
"INSERT INTO stakeholder values        ('hw','ejzuh','9999900078','A','ga5w3nu');",
"INSERT INTO stakeholder values        ('ji','hopie','9999900079','A','kh3z5ui');",
"INSERT INTO stakeholder values        ('vp','rktmi','9999900080','A','xr5b7va');",
"INSERT INTO stakeholder values        ('tk','lqvse','9999900081','L','uj7s7mu');",
"INSERT INTO stakeholder values        ('ki','zogut','9999900082','B','yk4g7bt');",
"INSERT INTO stakeholder values        ('mp','blfos','9999900083','L','wm1g1ub');",
"INSERT INTO stakeholder values        ('ry','zxjjj','9999900084','O','gt2t6ew');",
"INSERT INTO stakeholder values        ('ny','wyyqm','9999900085','O','ix6d3xr');",
"INSERT INTO stakeholder values        ('rt','fcnin','9999900086','L','wl4s7wh');",
"INSERT INTO stakeholder values        ('zb','zyefo','9999900087','L','mw3p0rx');",
"INSERT INTO stakeholder values        ('ne','tgnfg','9999900088','O','hj5j0ay');",
"INSERT INTO stakeholder values        ('um','bhhwz','9999900089','O','dj9z4qj');",
"INSERT INTO stakeholder values        ('ud','ynrok','9999900090','B','bz4z4ii');",
"INSERT INTO stakeholder values        ('hy','xrzzc','9999900091','A','uc1c4zv');",
"INSERT INTO stakeholder values        ('ui','nvfta','9999900092','B','cl0z5ak');",
"INSERT INTO stakeholder values        ('ts','gkcsq','9999900093','A','rv2k5dj');",
"INSERT INTO stakeholder values        ('kz','tuiau','9999900094','A','bw5i0oa');",
"INSERT INTO stakeholder values        ('vc','pgrkx','9999900095','O','at9h8iy');",
"INSERT INTO stakeholder values        ('de','iraou','9999900096','B','ej3t5xq');",
"INSERT INTO stakeholder values        ('mb','iyypu','9999900097','O','yf0a0ze');",
"INSERT INTO stakeholder values        ('dy','edbol','9999900098','B','oi9b7kn');",
"INSERT INTO stakeholder values        ('sa','nxhtq','9999900099','B','pz8a6iw');",
"INSERT INTO stakeholder values        ('lv','qrisk','9999900100','B','oa9p8xe');"]


for i in stakeholder_insertion:
    conn.execute(i)
    conn.commit()
    

