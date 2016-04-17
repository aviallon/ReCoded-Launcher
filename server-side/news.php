<!DOCTYPE html>
<?php
$files = glob("*.json");

if ($files === false) {
    $files = [];
}

$modpacks = array();
foreach ($files as $file) {
    $data = json_decode(file_get_contents($file));
    if (isset($data->name) && isset($data->version)) {
        $modpacks[] = [
            'name' => $data->name,
            'title' => isset($data->title) ? $data->title : $data->name,
            'version' => $data->version
        ];
    }
}
?>
<html>
    <head>
        <title>News Page</title>
        <meta charset="utf-8">
        <style>
        body {
            color: #ffffff;
            font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            font-size: 12pt;
        }
        .logo {
            padding: 0 0 12px 0;
        }
        .block {
            width: 90%;
            padding: 12px;
            margin: 0 0 10px 0;
        }
        h1 {
            font-size: 110%;
            color: #4bb7b9;
            margin: 0 0 8px 0;
            padding: 0;
        }
        ul {
            margin: 0;
            padding: 0 0 0 15px;
        }
        li {
            margin: 0;
            padding: 0;
        }
        a {
            text-decoration: none;
            color: #999999;
        }
        a:hover {
            text-decoration: underline;
            color: #999999;
        }
        </style>
    </head>
    <body>
        <div class="logo">
            <img src="logo.png" width="480" height="63">
        </div>

        <div class="block">
            <h1>Les différents packs de mods</h1>
            <ul>
<?php
foreach($modpacks as $pack) {
    $url = 'http://leroyaumedestards420.cloudcraft.fr/#' . urlencode($pack['name']);
    echo '<li><b>' . $pack['title'] . '</b> (' . $pack['version'] . ') : <a href="' . $url . '">Voir la liste des mods...</a></li>';
}
?>
            </ul>
        </div>
    </body>
</html>
