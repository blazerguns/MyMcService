<?php

// autoloader for Composer
require 'vendor/autoload.php';

// instanciate Slim
$app = new Slim\App();

// grouping the /api route, see Slim's group() method documentation for more
$app->group('/api', function () use ($app) {

    $dataForApi = ['ds', 'secret value'];

    // api route "test" which just gives back some demo data
    $app->get('/test', function ($request, $response, $args) use ($dataForApi) {
        $rid = $request->getQueryParam('rid', $default = 'yo');
        return $response->withJson([
            'demoText' => $rid, // "yo"
            'demoNumbers' => $dataForApi[1] // "777"
        ]);
    });
});

$app->run();
