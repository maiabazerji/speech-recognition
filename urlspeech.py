import speech_recognition as sr
import webbrowser as wb

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")

        try:
            dest = r.recognize_google(audio)
            print("You said: " + dest)

            #  open any URL mentioned (google, facebook..)
            wb.open("https://www." + dest.lower().replace(" ", "") + ".com")

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
