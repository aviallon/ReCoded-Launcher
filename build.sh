#!/bin/sh

version=4.3.2

# Compiling
bash ./gradlew -Pversion=$version clean build
cp launcher-bootstrap/build/libs/launcher-bootstrap-$version-all.jar build/dobbylauncher.jar

# Creating the .jar.pack
pack200 --no-gzip "build/launcher/launcher.jar.pack" "launcher-fancy/build/libs/launcher-fancy-$version-all.jar"
echo '{"version": "'$version'", "url": "http://leroyaumedestards420.cloudcraft.fr/launcher/launcher.jar.pack"}' > build/launcher/latest.json

echo "You should now send build/launcher directory to your personnal server."

read -p "Press any key to continue..."
