# FreeSpeech
Package used for generating random meaningless speech. Want to exercise
your right to free speech but don't want to bother with proper common
sense? Then this is the tool for you.  
It can also be used has a tool to combat solitude and deal with
isolation.
* [Instalation](#Instalation)
 * [Dependencies](#Dependencies)
* [Usage](#Usage)
 * [generateText](#generateText)
 * [saveText](#saveText)
 * [generateSpeech](#generateSpeech)

## <a name="Instalation"></a>Instalation
Tested only in Linux (Ubuntu). Use pip to install the python package:
```
sudo pip install FreeSeech
```

### <a name="Dependencies"></a>Dependencies
It depends on the text-to-speech software "espeak". It should be
installed before the package:
```
sudo apt-get install espeak
```

## <a name="Usage"></a>Usage
FreeSpeech is a set of functions.

### <a name="generateText"></a>generateText
It generates random and meaningless text. It has 1 optional argument:

#### lines_number
The number of paragraphs that compose the text. The default value is
10.

#### Example:
```
from FreeSpeech import generateText

lines_number = 20
text = generateText(lines_number)
```

### <a name="saveText"></a>saveText
It saves the random text into a file. It has 2 optional argument:

#### lines_number
The number of paragraphs that compose the text. The default value is
10.

#### output
The output directory of the text file. The default is "./random.txt".

#### Example:
```
from FreeSpeech import saveText

lines_number = 20
output = "./text.txt"
saveText(lines_number, text)
```

### <a name="generateSpeech"></a>generateSpeech
It saves a sound file with random speech. It has 4 arguments, 1
required, and 3 optional:

#### text
Required argument. The string of text that is going to be converted to
speech.

#### language
The language that is going to read the random text. It defaults to
English ("en").

#### speed
The speed rate of the speech in words per minute. The default is 100
words per minute.

#### output
The output directory of the speech file. The default is "./random.mp3".

#### Example:
```
from FreeSpeech import generateText
from FreeSpeech import generateSpeech

text = generateText()
language = "pt"
speed = 110
output = "./speech.mp3"
generateSpeech(text, language, speed, output)
```
