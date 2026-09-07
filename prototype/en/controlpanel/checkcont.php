<?php

$cmd = 'taskkill /IM "python.exe" /F';
exec($cmd);
$cmd = 'taskkill /F /im node.exe';
exec($cmd);
header("Location: index.php");

?>
