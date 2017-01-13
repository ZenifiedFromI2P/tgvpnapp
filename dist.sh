rm -rv dist-wp/*
cp *.css dist-wp
cp main.js dist-wp
cp app.js dist-wp
cp index.html dist-wp
cp bundle.js dist-wp
cp package.json dist-wp
electron-packager --overwrite dist-wp TGVPN
