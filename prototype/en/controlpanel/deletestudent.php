<html>
<body>
<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}
include("../config.php");

$studentnumber = $_GET['deleteuser'];
$sql = "DELETE FROM students where studentnumber ='$studentnumber'";
$conn->query($sql);

$sql2 = "DROP USER '$studentnumber'@localhost";
$conn->query($sql2);

$sql3 = "DROP DATABASE ".$studentnumber;
$conn->query($sql3);

$sql4 = "INSERT INTO pendingstudentsdeletion (studentnumber)
		VALUES ('$studentnumber')";
$conn->query($sql4);

 function rrmdir($dir) { 
   if (is_dir($dir)) { 
     $objects = scandir($dir);
     foreach ($objects as $object) { 
       if ($object != "." && $object != "..") { 
         if (is_dir($dir. DIRECTORY_SEPARATOR .$object) && !is_link($dir."/".$object))
           rrmdir($dir. DIRECTORY_SEPARATOR .$object);
         else
           unlink($dir. DIRECTORY_SEPARATOR .$object); 
       } 
     }
     rmdir($dir); 
   } 
 }


$deldir = "C:/xampp/htdocs/".$studentnumber."/";
rrmdir($deldir);

$conn->close();

header('Location: students.php');
?>

</body>
</html>