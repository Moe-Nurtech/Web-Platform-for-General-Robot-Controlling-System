<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}



?>

<!DOCTYPE html>

<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="shortcut icon" href="assets/images/keepass_256x256.png" type="image/x-icon">







<style>

.loader {

  border: 16px solid #f3f3f3;

  border-radius: 50%;

  border-top: 16px solid #e83235;

  width: 120px;

  height: 120px;

  -webkit-animation: spin 2s linear infinite; /* Safari */

  animation: spin 2s linear infinite;

}



/* Safari */

@-webkit-keyframes spin {

  0% { -webkit-transform: rotate(0deg); }

  100% { -webkit-transform: rotate(360deg); }

}



@keyframes spin {

  0% { transform: rotate(0deg); }

  100% { transform: rotate(360deg); }

}

</style>

</head>

<body style ="background-color:#eeeeee">

<br><br><br><br>

<h2 style="font-family: Arial, Helvetica, sans-serif;" align="center"><font color="#e83235">UAEU</font> Robotics Lab</h2>

<br>

<br>

<div align="center">

<div class="loader"></div>

</div>

<br>

<p align ="center">One moment please ...</p>







<form method="post" action="checkfacialexpression.php" id="registerform">



	

<input type="hidden" name="userid" value="test">









</form>

<script>

document.getElementById("registerform").submit();

</script>



</body>

</html>
