<html>
<body>
<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}
include("../config.php");

$id = $_GET['deleteactivity'];
$sql = "DELETE FROM activities where id ='$id'";
$conn->query($sql);
$conn->close();

header('Location: publications.php');
?>

</body>
</html>