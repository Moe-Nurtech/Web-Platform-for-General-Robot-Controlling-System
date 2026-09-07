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
  
  <title>projects</title>
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
                    <a href="../controlpanel">
                        <img src="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" alt="UAEU" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-4" href="../controlpanel">Admin: <font color="#e83235"><?php echo $_SESSION['adminid']; ?></font></a></span>
            </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-dropdown" data-app-modern-menu="true"><li class="nav-item">
                    <a class="nav-link link text-black display-4" href="../controlpanel">Home</a>
                </li><li class="nav-item"><a class="nav-link link text-black display-4" href="students.php">Students</a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="projects.php">Projects</a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="publications.php">Publications</a></li>
                <li class="nav-item">
                    <a class="nav-link link text-black display-4" href="vms.php">Virtual Machines</a>
                </li><li class="nav-item"><a class="nav-link link text-black display-4" href="containers.php">Containers</a></li></ul>
            <div class="navbar-buttons mbr-section-btn"><a class="btn btn-sm btn-secondary-outline display-4" href="logout.php">
                    Logout</a></div>
        </div>
    </nav>
</section>





<section class="engine"><a href="https://mobirise.info/s">bootstrap theme</a></section>
<section class="header15 cid-rWs1WV6Gik mbr-fullscreen" id="header15-q">

    

    

    <div class="container align-center">
        

            <h3> Add a project </h3>
			<br>
			
                <div class="form-container">
                    <div class="media-container-column" data-form-type="formoid">
                        <!---Formbuilder Form--->
                        <form action="tempaddingproject.php" method="POST" class="mbr-form form-with-styler" data-form-title="Mobirise Form"><input type="hidden" name="email" data-form-email="true" value="gJx9mYTDCqc5wiV+1ThQbFtpaaAAD8BSYL1293Dr7SnEfZIxWy/1rGw82f99s7sB1D1O/ar9yeMjr0yOMiW4aN394acAJBb95cJFIxzbtANNqbPKSYgvqP+6H1HnxeGX">
                            <div class="row">
                                <div hidden="hidden" data-form-alert="" class="alert alert-success col-12">Thanks for filling out the form!</div>
                                <div hidden="hidden" data-form-alert-danger="" class="alert alert-danger col-12">
                                </div>
                            </div>
                            <div class="dragArea row">
                                <div class="col-md-12 form-group " data-for="name">
                                    <input type="text" name="project" placeholder="project name (no spaces)" data-form-field="Name" required="required" class="form-control px-3 display-7" id="name-header15-q">
                                </div>
                                <div class="col-md-12 form-group " data-for="email">
                                    <input type="text" name="title" placeholder="Project title" data-form-field="Email" required="required" class="form-control px-3 display-7" id="email-header15-q">
                                </div>
                                <div data-for="phone" class="col-md-12 form-group ">
                                    <input type="text" name="shortdesc" placeholder="Short description" data-form-field="Phone" required="required" class="form-control px-3 display-7" id="phone-header15-q">
                                </div>
                         
								
                                <div class="col-md-12 input-group-btn"><button type="submit" class="btn btn-form btn-primary-outline display-4">Add Project</button></div>
							
							
							
                        </form><!---Formbuilder Form--->
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