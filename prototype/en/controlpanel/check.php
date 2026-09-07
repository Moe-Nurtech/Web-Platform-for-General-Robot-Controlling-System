<?php
//exec("./nav02.sh > /dev/null &");
//header("Location: navigation.php");
//echo shell_exec('python pythoncode/main.py');


//$locale = 'en_US.utf-8';
//setlocale(LC_ALL, $locale);
//putenv('LC_ALL='.$locale);



//echo shell_exec('python pythoncode/main.py');


//WORK BUT NOT IN THE BACKGROUND
//echo shell_exec('run2.bat > NUL');


$command = 'start /B run2.bat  > NUL';
pclose( popen( $command, 'r' ) );
sleep(9);





header("Location: operation.php");

//system('python pythoncode/main.py');
//system('run2.bat');

//error_reporting(E_ALL);

/* Add redirection so we can get stderr. */
//$handle = popen('run2.bat 2>&1', 'r');
//echo "'$handle'; " . gettype($handle) . "\n";
//$read = fread($handle, 2096);
//echo $read;
//pclose($handle);
?>
