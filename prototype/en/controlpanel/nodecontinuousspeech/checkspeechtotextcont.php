<?php
#echo shell_exec('azuresend.bat > NUL');
$command = 'start /B runnodejs.bat > NUL';
pclose( popen( $command, 'r' ) );
sleep(1);
$command = 'start /B cont.bat > NUL';
pclose( popen( $command, 'r' ) );
header("Location: ../speechtotextcont.php");

?>