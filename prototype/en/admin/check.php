<?php
if(empty($_POST['userid'])){
	header ("Location: index.php");
} 
session_start();
include("../config.php");
$error = 1;
$userid = $_POST['userid'];
$mypassword= $_POST['mypassword'];


$sql = "select * from admin where userid ='$userid'";
$result = mysqli_query($conn, $sql);

	if(mysqli_num_rows($result)!=0) {
		$row = mysqli_fetch_assoc($result);
		if($row['password']== $mypassword){		
			$error = 0;
		}
	}
  

if ($error == 0){
//start session
$_SESSION['adminid']= $userid;
}


$conn->close();

if ($error == 1){
	header ("Location: index.php?c=0");
}
else{
	header ("Location: ../controlpanel");
}

?>