<?php
exec("./joystick.sh > /dev/null &");
header("Location: joystick/gui.php");
?>

