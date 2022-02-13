# RedBadger-MartianRobot exercise solution

## How to run
For my machine `export PYTHONPATH=.` needed to be run before python could work


`make run` runs *app/main.py*

`make test` runs *tests/test_board.py*

If needed, custom filenames can be passed as such
`python app/main.py -f moving_test.txt`

## Areas to improve
- CI/CD
- Better error handling
- Reading file line by line. Storing massive files in memory could become problematic