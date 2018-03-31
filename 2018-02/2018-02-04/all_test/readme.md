运行所有 case 的命令行：
python -m unittest discover
(-s, --start-directory; -p, --pattern)
python -m unittest discover -s alltests -p "test_*.py"
python -m unittest discover alltests "test_*.py"