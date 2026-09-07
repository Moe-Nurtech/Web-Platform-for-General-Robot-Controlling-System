<html>
<body>
<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}
include("../config.php");

$projectname = $_GET['deleteproject'];
$sql = "DELETE FROM projects where projectname ='$projectname'";
$conn->query($sql);


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


$deldir = "C:/xampp/htdocs/masters/masters/en/projects/".$projectname."/";
rrmdir($deldir);

$conn->close();

header('Location: projects.php');
?>

</body>
</html>