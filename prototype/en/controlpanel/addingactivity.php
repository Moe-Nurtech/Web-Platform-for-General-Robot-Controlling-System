<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}
include("../config.php");
$activity = $_POST['activity'];
$year = $_POST['year'];
$sql = "INSERT INTO activities (activity, type, year)
		VALUES ('$activity','activity', '$year')";
$conn->query($sql);
$conn->close();

header ("Location: publications.php");

?>