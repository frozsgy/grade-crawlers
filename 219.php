<?php
$DBHost = 'localhost';
$DBUser = 'root';
$DBPass = '';
$DBName = 'metu_219';
$link=mysqli_connect($DBHost, $DBUser, $DBPass, $DBName);
function httpPost($url,$params) {
  $postData = '';
    foreach($params as $k => $v) {
      $postData .= $k . '='.$v.'&';
    }
  $postData = rtrim($postData, '&');
  $ch = curl_init();
  curl_setopt($ch,CURLOPT_URL,$url);
  curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
  curl_setopt($ch,CURLOPT_HEADER, false);
  curl_setopt($ch, CURLOPT_POST, count($postData));
  curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
  $output=curl_exec($ch);
  curl_close($ch);
  return $output;
}
function tr_strtolower($text) {
    $search=array("�","�","О","�","ޞ","�");
    $replace=array("C","I","G","O","S","U");
    $text=str_replace($search,$replace,$text);
    return $text;
}
function getData($id) {
  global $link;
  $params = array(
    "id" => $id,
    "Submit" => "Show Info");
  $return=httpPost("http://ma219.math.metu.edu.tr/SIS/sis.php",$params);
  preg_match_all('/<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td>/msi', $return, $output);
  $id=@$output[1][1];
  $ln=@$output[2][1];
  $ln=tr_strtolower($ln);
  $fn=@$output[3][1];
  $fn=tr_strtolower($fn);
  $mt1=@$output[11][1];
  $queery="INSERT INTO `2018` VALUES ('$id', '$ln', '$fn', '$mt1');";
  mysqli_query($link, $queery);
  if(strlen($fn) > 2) {
    print "$id - $fn $ln imported\n";
  }
}
#Honestly, I don't remember where I copied this function, but it's a basic implementation of Luhn's checksum. Apologies for the person who implemented this.
function Luhn($number, $iterations = 1) {
  while ($iterations-- >= 1) {
    $stack = 0;
    $number = str_split(strrev($number), 1);
    foreach ($number as $key => $value) {
      if ($key % 2 == 0) {
        $value = array_sum(str_split($value * 2, 1));
      }
      $stack += $value;
    }
    $stack %= 10;
    if ($stack != 0) {
      $stack -= 10;
    }
    $number = implode('', array_reverse($number)) . abs($stack);
  }
  return $number;
}

for($i=170000;$i<250000;$i++) {
  $j=Luhn($i);
  if($i % 100 == 0) {
    print 'Started new section: '.$i;
    print "\n";
  }
  getData($j);
}

print "Everything worked out just fine!";
mysqli_close($link);
