<?php

/*
 * Endpoint for Github Webhook URLs
 *
 * see: https://help.github.com/articles/post-receive-hooks
 * taken from: https://gist.github.com/gka/4627519
 *
 * sending emails doesn't seem to work on our server so just disable it
 *
 * the config.json file has to look somewhat like this:
 *
 * {
 *    "email": {
 *        "from": "devnull@darktable.org",
 *        "to": "me@houz.org"
 *    },
 *    "endpoints": [
 *        {
 *            "repo": "darktable-org/dtorg",
 *            "branch": "master",
 *            "action": "something has been changed on the server",
 *            "run": "/var/www/update_dtorg.sh",
 *            "logfile": "/var/www/dtorg_log.txt",
 *            "secret": "****"
 *        }
 *    ]
 * }
 *
 */

// script errors will be send to this email:
// $error_mail = "me@houz.org";
$error_logfile = "/var/www/dtorg_error_log.txt";

function run($postBody) {
    global $rawInput;

    // read config.json
    $config_filename = '../config.json';
    if (!file_exists($config_filename)) {
        throw new Exception("Can't find ".$config_filename);
    }
    $config = json_decode(file_get_contents($config_filename), true);

    $payload = json_decode($postBody);

//     if (isset($config['email'])) {
//         $headers = 'From: '.$config['email']['from']."\r\n";
//         $headers .= 'CC: ' . $payload->pusher->email . "\r\n";
//         $headers .= "MIME-Version: 1.0\r\n";
//         $headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
//     }

    foreach ($config['endpoints'] as $endpoint) {
        // check if the push came from the right repository and branch
        if ($payload->repository->url == 'https://github.com/' . $endpoint['repo']
            && $payload->ref == 'refs/heads/' . $endpoint['branch']) {

            // check if the payload is correctly signed
            if(isset($endpoint['secret']))
            {
                $hash = 'sha1=' . hash_hmac('sha1', $postBody, $endpoint['secret'], false);
                if (!hash_equals($hash, $_SERVER['HTTP_X_HUB_SIGNATURE'])) {
                    throw new Exception("Signature mismatch!\n");
                }
            }

            // execute update script, and record its output
            ob_start();
            passthru($endpoint['run']);
            $output = ob_get_contents();
            ob_end_clean();

            // prepare and send the notification email
//             if (isset($config['email'])) {
//                 // send mail to someone, and the github user who pushed the commit
//                 $body = '<p>The Github user <a href="https://github.com/'
//                 . $payload->pusher->name .'">@' . $payload->pusher->name . '</a>'
//                 . ' has pushed to ' . $payload->repository->url
//                 . ' and consequently, ' . $endpoint['action']
//                 . '.</p>';
//
//                 $body .= '<p>Here\'s a brief list of what has been changed:</p>';
//                 $body .= '<ul>';
//                 foreach ($payload->commits as $commit) {
//                     $body .= '<li>'.$commit->message.'<br />';
//                     $body .= '<small style="color:#999">added: <b>'.count($commit->added)
//                         .'</b> &nbsp; modified: <b>'.count($commit->modified)
//                         .'</b> &nbsp; removed: <b>'.count($commit->removed)
//                         .'</b> &nbsp; <a href="' . $commit->url
//                         . '">read more</a></small></li>';
//                 }
//                 $body .= '</ul>';
//                 $body .= '<p>What follows is the output of the script:</p><pre>';
//                 $body .= $output. '</pre>';
//                 $body .= '<p>Cheers, <br/>Github Webhook Endpoint</p>';
//
//                 mail($config['email']['to'], $endpoint['action'], $body, $headers);
//             }

            // also log to disk
            if (isset($endpoint['logfile'])) {
                $date = date('Y-m-d H:i:s');
                $pre  = $date . ' (' . $_SERVER['REMOTE_ADDR'] . '): ';
                file_put_contents($endpoint['logfile'], $pre . $output . "\n", FILE_APPEND);
            }

            return true;
        }
    }
    throw new Exception("This does not appear to be for a configured repo.\n");
}

try {
    $postBody = file_get_contents('php://input');
    if ($postBody && $_SERVER['CONTENT_TYPE'] === 'application/json') {
        run($postBody);
    } else {
        echo "Works fine.";
    }
} catch ( Exception $e ) {
    $msg = $e->getMessage();
//     mail($error_mail, $msg, ''.$e);
    $date = date('Y-m-d H:i:s');
    $pre  = $date . ' (' . $_SERVER['REMOTE_ADDR'] . '): ';
    file_put_contents($error_logfile, $pre . $msg . "\n", FILE_APPEND);
}
