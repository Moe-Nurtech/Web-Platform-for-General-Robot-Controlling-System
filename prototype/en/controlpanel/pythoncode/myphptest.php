<?php
$x= "السلام عليكم";
//echo $x;
#echo shell_exec('python C:\xampp\htdocs\abusaif\prototype1\en\controlpanel\pythoncode\mymaintest.py');
//$command = 'python myargtest.ph '.$x;
$command = 'start /B runtest.bat  > NUL';
pclose( popen( $command, 'r' ) );
?>