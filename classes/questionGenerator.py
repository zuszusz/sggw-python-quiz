from classes.answer import Answer
from classes.question import Question

class Generator(object):
    def __init__(self):
        pass

    @staticmethod
    def generateQuestions():
        questions = []

        questions.append(Question(
            "Który z poniższych elementów nie jest częścią komputera?", 
            [Answer("a) Klawiatura", "Klawiatura"), Answer("b) Monitor", "Monitor"), Answer("c) Silnik samochodowy", "Silnik samochodowy")], 
            [Answer("c) Silnik samochodowy", "Silnik samochodowy")]
        ))

        questions.append(Question(
            "Co oznacza skrót URL?", 
            [Answer("a) Universal Resource Locator", "Universal Resource Locator"), Answer("b) Uniform Resource Locator", "Uniform Resource Locator"), Answer("c) Unique Resource Locator", "Unique Resource Locator")], 
            [Answer("b) Uniform Resource Locator", "Uniform Resource Locator")]
        ))

        questions.append(Question(
            "Który z poniższych jest przykładem przeglądarki internetowej?", 
            [Answer("a) Adobe Photoshop", "Adobe Photoshop"), Answer("b) Google Chrome", "Google Chrome"), Answer("c) Microsoft Excel", "Microsoft Excel")], 
            [Answer("b) Google Chrome", "Google Chrome")]
        ))

        questions.append(Question(
            "Co to jest bootowanie?", 
            [Answer("a) Proces uruchamiania systemu", "Proces uruchamiania systemu"), Answer("b) Instalacja systemu", "Instalacja systemu"), Answer("c) Formatowanie dysku", "Formatowanie dysku")], 
            [Answer("a) Proces uruchamiania systemu", "Proces uruchamiania systemu")]
        ))


        questions.append(Question(
            "Który z poniższych języków służy do tworzenia stron internetowych?", 
            [Answer("a) Python", "Python"), Answer("b) HTML", "HTML"), Answer("c) C++", "C++")], 
            [Answer("b) HTML", "HTML")]
        ))

        questions.append(Question(
            "Które z poniższych to funkcje systemu operacyjnego?", 
            [Answer("a) Zarządzanie plikami", "Zarządzanie plikami"), Answer("b) Edytowanie zdjęć", "Edytowanie zdjęć"), Answer("c) Zarządzanie pamięcią", "Zarządzanie pamięcią")], 
            [Answer("a) Zarządzanie plikami", "Zarządzanie plikami"), Answer("c) Zarządzanie pamięcią", "Zarządzanie pamięcią")]
        ))

        questions.append(Question(
            "Które z poniższych urządzeń są używane do przechowywania danych?", 
            [Answer("a) Pendrive", "Pendrive"), Answer("b) Procesor", "Procesor"), Answer("c) Dysk twardy", "Dysk twardy")], 
            [Answer("a) Pendrive", "Pendrive"), Answer("c) Dysk twardy", "Dysk twardy")]
        ))

        questions.append(Question(
            "Które z poniższych są językami znaczników?", 
            [Answer("a) HTML", "HTML"), Answer("b) CSS", "CSS"), Answer("c) XML", "XML")], 
            [Answer("a) HTML", "HTML"), Answer("c) XML", "XML")]
        ))

        questions.append(Question(
            "Które z poniższych programów są używane do edycji tekstu?", 
            [Answer("a) Microsoft Word", "Microsoft Word"), Answer("b) Notepad", "Notepad"), Answer("c) Microsoft Excel", "Microsoft Excel")], 
            [Answer("a) Microsoft Word", "Microsoft Word"), Answer("b) Notepad", "Notepad")]
        ))

        questions.append(Question(
            "Które z poniższych są przykładami pamięci masowej?", 
            [Answer("a) HDD", "HDD"), Answer("b) SSD", "SSD"), Answer("c) RAM", "RAM")], 
            [Answer("a) HDD", "HDD"), Answer("b) SSD", "SSD")]
        ))

        return questions