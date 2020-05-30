[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/uuso/travis-ci-practice/master.png?style=flat-square

[build]: https://travis-ci.org/uuso/travis-ci-practice

Unit-test & Travis-CI practice
--
## Project idea:
Simple "guess-the-word" game. You see the word's length and trying to guess the letter it contains. If you asked for a wrong letter - you drop your attempt (four fails to lose the game). If the letter is in the word - try another one until the whole word is opened.

*Aaand I'm trying to cover the code with tests!*

## How to run:
Oh, it's easy! Just download the repo and run "python3 game.py".

*Executing "pip3 install -r requirements.txt" is required if you want to run tests with pytest.*


## TEST COVER RESULTS:
*coverage report -m*
Name|Stmts|Miss|Cover|Missing
---|---|---|---|---
conftest.py|9|0|100%
game.py|48|14|71%|34, 47-60, 64
tests.py|42|0|100%
TOTAL|99|14|86%