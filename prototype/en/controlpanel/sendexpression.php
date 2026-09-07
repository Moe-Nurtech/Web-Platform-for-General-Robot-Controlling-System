<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}

$host = "127.0.0.1";
$port = 12346;

$f = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_set_option($f, SOL_SOCKET, SO_SNDTIMEO, array('sec' => 1, 'usec' => 500000));
$s = socket_connect($f, $host, $port);

$msg = $_GET['expression'];
$len = strlen($msg);
socket_sendto($f, $msg, $len, 0, $host, $port);

socket_close($f);

//$command = 'start /B starttexttospeech.bat  > NUL';
//pclose( popen( $command, 'r' ) );
//sleep(9);

sleep(10);



header("Location: facialexpression.php");


?>