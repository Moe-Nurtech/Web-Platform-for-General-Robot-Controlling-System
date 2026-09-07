<?php
exec("./joystick.sh > /dev/null &");
header("Location: simulation_ws/src/robot_gui_bridge/gui/gui.php");
?>

