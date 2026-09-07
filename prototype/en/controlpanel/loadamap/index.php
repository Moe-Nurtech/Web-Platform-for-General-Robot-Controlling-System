<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}
?>
<!DOCTYPE html>
<html  >
<head>
  <!-- Site made with Mobirise Website Builder v4.11.4, https://mobirise.com -->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v4.11.4, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" type="image/x-icon">
  <meta name="description" content="">
  
  <title>Load A Map</title>
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/datatables/data-tables.bootstrap4.min.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="preload" as="style" href="assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  
  
  
</head>
<body>
  <section class="menu cid-rSknZJrHWX" once="menu" id="menu2-0">

    

    <nav class="navbar navbar-expand beta-menu navbar-dropdown align-items-center navbar-fixed-top collapsed bg-color transparent">
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </button>
        <div class="menu-logo">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="../">
                        <img src="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" alt="UAEU" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-4" href="../">Admin: <font color="#e83235"><?php echo $_SESSION['adminid']; ?></font></a></span>
            </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-dropdown" data-app-modern-menu="true"><li class="nav-item">
                    <a class="nav-link link text-black display-4" href="../">Navigation Home</a>
                </li><li class="nav-item"><a class="nav-link link text-black display-4" href="../savedmaps" target="_blank">Saved Maps</a></li>
				
				<li class="nav-item"><a class="nav-link link text-black display-4" href="../gps" target="_blank">GPS</a></li>
                <li class="nav-item">
                    <a class="nav-link link text-black display-4" href="../livecamera" target="_blank">Live Camera</a>
                </li>
				<li class="nav-item">
                    <a class="nav-link link text-black display-4" href="../webshell" target="_blank">Web Shell</a>
                </li>
				<li class="nav-item"><a class="nav-link link text-black display-4" href="../voicetotextcommands" target="_blank">Voice To Text Commands</a></li></ul>
            <div class="navbar-buttons mbr-section-btn"><a class="btn btn-sm btn-secondary-outline display-4" href="../logout.php">
                    Logout</a></div>
        </div>
    </nav>
</section>

<section class="engine"><a href="https://mobirise.info/w">html5 templates</a></section><section class="section-table cid-rWopdr2RAg" id="table1-l">

  
  
  <div class="container container-table">
      
      <div align = "center">
	  <h3>Load a map</h3>
	  </div>
      <div class="table-wrapper">
        <div class="container">
          <div class="row search">
            <div class="col-md-6"></div>
            <div class="col-md-6">
                <div class="dataTables_filter">
                  <label class="searchInfo mbr-fonts-style display-7">Search:</label>
                  <input class="form-control input-sm" disabled="">
                </div>
            </div>
          </div>
        </div>

        <div class="container scroll">
          <table class="table isSearch" cellspacing="0">
            <thead>
              <tr class="table-heads ">
                  
                  
                  
                  
              <th class="head-item mbr-fonts-style display-7">
                      MAP TITLE</th><th class="head-item mbr-fonts-style display-7">
                      Navigation Type</th><th class="head-item mbr-fonts-style display-7">
                      LOAD</th></tr>
            </thead>

            <tbody>
              
<?php		
include("../../config.php");
$sql = "select * from projects";
$result = mysqli_query($conn, $sql);
//$row = mysql_fetch_array($result);
if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
		echo "<tr><td class='body-item mbr-fonts-style display-7'>"; echo $row['title'];
		echo "</td><td class='body-item mbr-fonts-style display-7'>"; ?>
		
		<?php
		$mylink = "http://www.nur-tech.net/masters/masters/en/projects/".$row['projectname'];
		echo "02 SLAM Navigation";?>
		<?php
		echo "</td><td class='body-item mbr-fonts-style display-7'>";
		?>
			<form action="#" method="get">
			<input type="hidden" name="x" value="#">
			<input type="submit" value="START">
			</form>
		<?php
		echo "</td></tr>";
			//start html design for table inside the loop
}}



$conn->close();
?>	
			  
			  </tbody>
          </table>
        </div>
        <div class="container table-info-container">
          <div class="row info">
            <div class="col-md-6">
              <div class="dataTables_info mbr-fonts-style display-7">
                <span class="infoBefore">Showing</span>
                <span class="inactive infoRows"></span>
                <span class="infoAfter">entries</span>
                <span class="infoFilteredBefore">(filtered from</span>
                <span class="inactive infoRows"></span>
                <span class="infoFilteredAfter"> total entries)</span>
              </div>
            </div>
            <div class="col-md-6"></div>
          </div>
        </div>
      </div>
    </div>
</section>


  <script src="assets/web/assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/dropdown/js/nav-dropdown.js"></script>
  <script src="assets/dropdown/js/navbar-dropdown.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/datatables/jquery.data-tables.min.js"></script>
  <script src="assets/datatables/data-tables.bootstrap4.min.js"></script>
  <script src="assets/theme/js/script.js"></script>
  
  
</body>
</html>