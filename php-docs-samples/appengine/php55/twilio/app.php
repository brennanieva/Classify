<?php

use Silex\Application;
$app = new Application();
$app->get('/', function () use ($app) {
    if ($app['twilio.account_sid'] == 'TWILIO_ACCOUNT_SID') {
        return 'set your Twilio SID and Auth Token in <code>index.php</code>';
    }
    $sid = $app['twilio.account_sid'];
    $token = $app['twilio.auth_token'];
    $fromNumber = $app['twilio.from_number'];
    $toNumber = $app['twilio.to_number'];
    # [START send_sms]
    $client = new Services_Twilio($sid, $token);
    $sms = $client->account->messages->sendMessage(
        $fromNumber, // From this number
        $toNumber,   // Send to this number
        'kill me now plz i want to stab my eye out with a fork idc if i die thank you and goodnight'
    );
    return sprintf('Message ID: %s, Message Body: %s', $sms->sid, $sms->body);
    # [END send_sms]
});
$app->post('/twiml', function () {
    # [START twiml]
    $response = new Services_Twilio_Twiml();
    $response->say('Hello Monkey');
    return (string) $response;
    # [END twiml]
});
return $app;
