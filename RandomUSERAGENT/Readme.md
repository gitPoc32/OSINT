Libreria en php que crea un Ramdom User-agent from http://www.danmorgan.net/programming/php-programming/random-useragent-in-curl-and-php/

Use:

include("random-user-agent.php");
 
//.... some code
 
curl_setopt($ch, CURLOPT_USERAGENT,random_user_agent());
 
//.... lots more code
