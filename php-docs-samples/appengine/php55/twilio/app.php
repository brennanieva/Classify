<?php
$client = new Services_Twilio($sid, $token);
$sms = $client->account->messages->sendMessage(
    $fromNumber, // From this number
    $toNumber,   // Send to this number
    'Hello monkey!!'
);

return sprintf('Message ID: %s, Message Body: %s', $sms->sid, $sms->body);

?>
