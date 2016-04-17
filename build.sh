#!/bin/sh

version=5.0

# Compiling
gradle clean build

# Construct
mkdir -p build/launcher
cp launcher-bootstrap/build/libs/launcher-bootstrap-$version-all.jar build/dobbylauncher.jar
pack200 --no-gzip "build/launcher/launcher.jar.pack" "launcher-fancy/build/libs/launcher-fancy-$version-all.jar"
echo '{"version": "'$version'", "url": "https://erdnaxe.iooss.fr/launcher/launcher.jar.pack"}' > build/launcher/latest.json

# End
echo "Send build/launcher directory to your personnal server."
