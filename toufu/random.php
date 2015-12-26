<?php	// Randomly select a toufu and return JSON
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:toufu.sq3");


$rets = array();
$st = $pdo->prepare("SELECT * FROM toufu WHERE cnt < 3 LIMIT 1000");
$st->execute();
$rows = $st->fetchAll(PDO::FETCH_ASSOC);
shuffle($rows);
for($i = 0; $i < 10; $i++) {
	$row = $rows[$i];
	$row['img_url'] = sprintf("%03d/%s.jpg", $row['p'], $row['par']);
	$rets[] = $row;
}

echo json_encode($rets);
