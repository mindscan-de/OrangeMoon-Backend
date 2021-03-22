# OrangeMoon-Backend
Japanese Dictionary App - Backend (based on fastapi and jamdict)

## Python Dependencies

* jamdict -- https://github.com/neocl/jamdict 
  * use the given installation guide to also have access to the collected dictionary data
  * then check the installation according to the installation guide

# The Idea

## The MVP

* Provide all Radicals (Ordered by Number of Strokes)
* Filter/Select Kanji by selecting Radicals
* Update the remaining Radicals according to previous selection (enable/disable) remaining radicals 
* Show filtered kanji ordered by number of strokes

* Show info for a given / selected kanji
 
## Nice to have

* Quiz
* Select for Quiz / Build a quiz
* Grade 1,2,3,4,5,6
* JLPT 5,4,3

* Verbs
* Adjectives

* Translation Memory for a book you read...

* Make a Quiz from the translation memory

* also detect negative/past/negative+past tense and other suffixes, which aren't part of the jamdict 
  e.g. tabemashou - let's eat together
* provide the reading of a sentence (for the Translation memory)
* input romaji support to just drop switching to the Japan-IME everytime

## TODO

* Don't know yet...