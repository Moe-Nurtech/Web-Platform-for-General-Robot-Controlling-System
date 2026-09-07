<?php

$cmd = 'taskkill /IM "python.exe" /F';
exec($cmd);

header("Location: index.php");

?>
