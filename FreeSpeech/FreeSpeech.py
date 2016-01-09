from faker import Faker     # for generating random text
import subprocess           # for using espeak (converting text to speech)


# generate random text
def generateText(lines_number = 10):
    text = ""
    fake = Faker()
    for _ in range(lines_number):
        text += fake.text() + "\n"
    return text


# save random text
def saveText(lines_number = 10, output = "./random.txt"):
    text = generateText(lines_number)
    with open(output, "a") as output_file:
        output_file.write(text)


# save random mp3 speech
def generateSpeech(text, language = "en", speed = 100,
                    output = "./random.mp3"):
    # call espeak
    subprocess.call(["espeak", text, "-s", str(speed), "-v", language, "-w",
                        output])


# main function
if __name__ == "__main__":
    text = generateText(10)
    print text
    saveText(10)
    generateSpeech(text, "en")
