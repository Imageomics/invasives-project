mkdir build
cd build
cp ../build_files/buildozer.spec .
cp -r ../app .
cp ../app/main.py .
cp -r ../src .
cp ../pyproject.toml .
cp ../README.md .
buildozer -v android debug