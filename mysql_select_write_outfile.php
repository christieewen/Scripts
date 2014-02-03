// Author: Christie Ewen
<?php
$host="changeme_example.com";
$user="changeme_user_id";
$password="changeme_password";
$database="changeme_database_name";

$con = mysqli_connect($host,$user,$password, $database);
if (mysqli_connect_errno()) {
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$table = "changeme_table";
$query = "select * from $table";

$result = mysqli_query($con, $query);

if($result === FALSE) {
    die(mysql_error()); // TODO: better error handling
    echo "failed to get results";
}

$file=fopen("file.txt","w+") or exit("Unable to open file!");

// TODO: change the fields below
while($row = mysqli_fetch_array($result))
  {
  echo fwrite($file, $row['field_rest_link_title'] . " | " . $row['field_rest_since_value'] . " | " . $row['field_rest_price_value'] . " | " . $row['field_rest_cuisine_value'] . " | " . $r\
ow['field_rest_simple_loc_value'] . " | " . $row['field_rest_phone_value'] . " | " . $row['field_rest_review_value']);
  }

fclose($file);
mysqli_close($con);
?>
