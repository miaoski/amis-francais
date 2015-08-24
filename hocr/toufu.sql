PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE toufu ( p int, par text, bbox text, words text, cnt int );
CREATE INDEX p_par on toufu (p, par);
CREATE TABLE log ( p int, par text, ans text );
COMMIT;
