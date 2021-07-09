<?php
$con=mysqli_connect("localhost","root","","pharmacy") or die("Cannot connect to server");
session_start();
$user = $_POST["user"];
$pass = $_POST["pass"];

$res = mysqli_query($con,"select * from retailer_register WHERE email = '$user'  and password = '$pass' ")
          or die("CANNOT ACCESS DATABASE".mysqli_error());
$row = mysqli_fetch_array($res);
$re = mysqli_query($con,"select * from custregister WHERE Email = '$user'  and password = '$pass' ")
          or die("CANNOT ACCESS DATABASE".mysqli_error());
$ro = mysqli_fetch_array($re);


$_SEESION["yes"] = 0;
if (($row["email"] == $user && $row["password"] == $pass )||($ro["Email"] == $user && $ro["Password"] == $pass))
{
  header('Location: /mini/retailer_details.php');
  $_SEESION["yes"] = 1;
}
else
{
  echo("INVALID LOG IN");
}

?>
