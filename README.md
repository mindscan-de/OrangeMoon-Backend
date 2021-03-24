# OrangeMoon-Backend
Japanese Dictionary App - Backend (based on fastapi and jamdict)

## Python Dependencies

* jamdict -- https://github.com/neocl/jamdict 
  * use the given installation guide to also have access to the collected dictionary data
  * then check the installation according to the installation guide

# The Idea

Because I'm interested in the japanese language, I'm using different kind of apps and websites.
Either to learn the japanese language or to read japanese texts. I usually switch between the
"Simple Kanji Quiz" to learn new kanji and to repeat known kanji - either sorted by grade or by
JLPT level. Then my second use-case is that I use Jisho to look up some kanji and their 
meaning. Then the third use-case is to select some japanese text and put it into g**gle
translate. But this is somehow like cheating, because I really look for something in between.
I look for something that will annotate and group the kanji and the kana in a kind of western 
way, to identify where something starts and where something ends. I find that especially hard 
but very useful - to be able to subconciously start to identify phrases more easily. Also for 
convenience I want to type in romaji but the shown input should be kana, not because I lack 
skill but, I don't want to switch back and forth between the IME and the "normal" layout. But
it should be able to work all ways for doing queries (romaji, kana, kana+ime->kanji).

This grouping thing i often encountered in learning apps e.g. with content from the NHK website.

And the last use case is to remember translations (and record and provide references) and turn 
them into a quiz, so I can reuse the made effort to hone my japanese language skills. E.g. for
assistence when reading a japanese book. It would be totally cool when a japanese sentence can
be recalled, and i can just hoover over a word i forgot, and it will show me the meaning again.
or explain what is meant by "BGM" if you have no idea... (background music). Also it should show
the correct reading in a given context. Just because you can recognize kanji it doesn't mean you
can read them out loud correctly.

And last but not least I want to use such a thing off-grid, because the internet is not every
where yet. So these are different motivations to begin to implement a japanese dictionary app.
I'm fine with using this thing in a local browser, with a local webserver. 

That is the setup. A browser-based Angular App with a python based backend.

## The MVP

* Provide all Radicals **[done]**
* Filter/Select Kanji by selecting Radicals **[done]**
* Provide remaining Radicals for kanji by selecting Radicals **[done]** 
* Provide all Radicals (with additional info strokes etc.) (Ordered by Number of Strokes)
* Update the remaining Radicals according to previous selection (enable/disable) remaining radicals 
* Show filtered kanji (Ordered by number of strokes)

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