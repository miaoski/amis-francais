PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE toufu ( p int, par text, bbox text, words text, cnt int );
CREATE INDEX p_par on toufu (p, par);
COMMIT;
