<?php
require('sanitizept.inc.php');


class DB extends SQLite3
{

    function __construct()
    {
            $this->open('ambient.db');
    }
         
    
}

if ( isset($_POST['device']) && isset($_POST['temp']) && isset($_POST['humidity']) ) {

    $device = sanitize_paranoid_string($_POST['device']);
    $temp = sanitize_float($_POST['temp']);
    $humidity = sanitize_float($_POST['humidity']);

    
} else {
    
die("Not allowed.\n");    
}

$db = new DB();


$sql="INSERT INTO ambienttemp (device,temp,humidity,date,ip) values ('". $device ."', " . $temp .",'" . $humidity ."','" .date('c') . "','". $_SERVER["REMOTE_ADDR"]."' )";
$result=$db->exec($sql);

if (!$result) {
        echo $db->lastErrorMsg();
} else {
    
        echo "Records created successfully";
}

$db->close();





?>
