<?php
if(strcmp($_GET['token'],"NhEKX6jwSPDSxVqMTLsqnzebhMVDchbPJPetFu3mEmWwLGmQTRRExdq4fLdvV8z6bQPxpNXrXeKpk7zktj7RyxZNgKxtEhk3q6CNGqDBDzKxspy5ZSVHxVUvxTCbJqy8yNKxpYs3jB8xN2LMGcT7esuqpZyuzLUv5xRTf3RxPHUU2QwaUfFpNU4Z5aGXNuYdqvfAfstyRZLCejgPZphrnHAUTnCkr42erDkyS5Nu89BQS6fF2Wv6sT5paKFQ8kqvkjwwCf9ZkDKNAWnsQGVeagZYDuuvgC6J9Bs6HEFPBBNRmawnx8DgE6xqpR3YcG7GGYsLMg3B5vWVpnasXd8CPnyWefctkeLpTUma2x6BradDV4rfrpaJHTrDyeuBa7uBcFq3beJLxDAVrTkZCvrJSShFU38ZhA4j9Yk8tLxf9VLRt23w55pBRKDjnvgZ2wQptZjL7sQ2KpMW4XR8zzed2zLkFQyTDXSCWwYe5Hag2JdxKw4SQKeNpLJHCF4ZT5EU")==0)
{
	echo "to: " . $_GET['to'] . "<br>";
	echo "subject: " . $_GET['subject'] . "<br>";
	echo "body: " . $_GET['body'] . "<br>";

	mail($_GET['to'], $_GET['subject'], $_GET['body'], "MIME-Version: 1.0\r\nContent-type: text/html; charset=iso-8859-1\r\nFrom: Billeasy <no-reply@billeasy.razzatech.com>\r\n");
}
?>

