<?php
require('sanitizept.inc.php');


class DB extends SQLite3
{

    function __construct()
    {
            $this->open('duke.db');
    }
         
    
}

if (isset($_POST['device']) && isset($_POST['temp'])) {

    $device = sanitize_paranoid_string($_POST['device']);
    $temp = sanitize_float($_POST['temp']);

    
} else {
    
die("Not allowed.\n");    
}

$db = new DB();


$sql="INSERT INTO cputemp (device,temp,date,ip) values ('". $device ."', " . $temp .",'".date('c') . "','". $_SERVER["REMOTE_ADDR"]."' )";
$result=$db->exec($sql);

if (!$result) {
        echo $db->lastErrorMsg();
} else {
    
        echo "Records created successfully";
}

$db->close();





?>
