<?php
$cmddata = exec('netsh interface ip show address "Wi-Fi" | findstr "IP Address"');
$ip = str_replace("IP Address: ", "",$cmddata);
echo $ip;
?>