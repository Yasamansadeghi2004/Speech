# yasaman sadeghi
import speech_recognition as sr
# برای افزودن رنگ به متن در خروجی خط فرمان
from colorama import init, Fore
#تعیین رنگ در خط فرمان
from termcolor import colored
from translate import Translator
# تبدیل متن به صدا
import pyttsx3
from vanna.base import VannaBase


def online_speech_to_text():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    # مجوز استفاده از رنگها در خط فرمان
    init(autoreset=True)

    with sr.Microphone() as source:

        print("Be silent...")
        # حذف نویزهای اطراف
        recognizer.adjust_for_ambient_noise(source)
        print("Now speak :")
        audio = recognizer.listen(source, timeout=5)

    try:
        # دریافت صدا
        text0 = recognizer.recognize_google(audio, language="fa-IR")

        # ترجمه صدای دریافتی از فارسی به انگلیسی
        def translate(text, source_language='fa-IR', target_language='en'):
            translator = Translator(from_lang=source_language, to_lang=target_language)
            translation = translator.translate(text)
            return translation

        persian_text = text0
        english_translate = translate(persian_text)
        print(colored(Fore.GREEN + f"You seid: {text0} "))
        print(colored(Fore.BLUE + f"English translate: {english_translate}"))
        # تشخیص متن
        engine.say(text0)
        # تبدیل به صدا
        engine.runAndWait()
    except sr.UnknownValueError:
        print(colored(Fore.RED + "I did not understand, repeat again"))
    except sr.RequestError as e:
        print(colored(Fore.RED + "Detection error,  check your internet connection"))

# فراخوانی تابع برای دریافت صدا


online_speech_to_text()
