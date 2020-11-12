rm -rf  dist/*.gz
rm -rf  dist/*.whl
rm -rf  build/*
rm -rf  freehub.egg-info/*
python3 setup.py sdist bdist_wheel