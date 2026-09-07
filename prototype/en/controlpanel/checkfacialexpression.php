<?php

$command = 'start /B startfacialexpression.bat  > NUL';
pclose( popen( $command, 'r' ) );
//sleep(9);


header("Location: facialexpression.php");

?>
