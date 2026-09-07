<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}
include("../config.php");
$publication = $_POST['publication'];
$title = $_POST['title'];
$type = $_POST['type'];
$year = $_POST['year'];
$sql = "INSERT INTO publications (publication, title, type, year)
		VALUES ('$publication', '$title','$type', '$year')";
$conn->query($sql);
$conn->close();

header ("Location: publications.php");

?>