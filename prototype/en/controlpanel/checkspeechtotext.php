<?php
#echo shell_exec('azuresend.bat > NUL');
$command = 'start /B azuresend.bat > NUL';
pclose( popen( $command, 'r' ) );
header("Location: listenspeech.php");

?>