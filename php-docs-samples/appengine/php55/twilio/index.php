<?php
/**
 * Copyright 2016 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Install composer dependencies with "composer install"
// @see http://getcomposer.org for more information.
require __DIR__ . '/vendor/autoload.php';

$app = require __DIR__ . '/app.php';

$app['twilio.account_sid'] = 'AC7e9f588ceaacd9b14a9aa1a53547bf95';
$app['twilio.auth_token']  = '150970e8331a550d4438eeee3d23ed04';
$app['twilio.from_number'] = '13603835503';
$app['twilio.to_number']   = '12538885523';

// Run the app!
// use "gcloud app deploy" or run "php -S localhost:8080"
// and browse to "index.php"
$app['debug'] = true;
$app->run();
