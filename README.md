# RODO-CV [Polish only]

RODO-CV to aplikacja konsolowa służąca do dodawania klauzury RODO do CV.

# Prolog

Każde ogłoszenie o prace dawniej było opatrzone klauzurą o ochronie danych osobowych, od momentu wejścia w życie RODO ogłoszenia o pracę posiadają specjalną formułkę, którą przed wysłaniem CV do pracodawcy musimy wkleić na końcu naszego dokumentu. Dla wielu ogłoszeń może być użyta uniwersalna reguła RODO, jednak wiele firm w ogłoszeniach prezentuje swoje indywidualne klauzury, które musimy wpisać do naszego dokumentu. Jeśli jej nie wkleimy to osoba rekrutująca z automatu odrzuca naszą aplikację. Postanowiłem zatem stworzyć aplikację, która do gotowego CV zapisanego w pliku PDF będzie dodawać wybraną przez nas regułę RODO.

# Jak to działa?

Podajemy w pliku tekstowym treść klauzury RODO, kopiujemy nasze CV, aplikacja generuje nowy plik PDF z samą klauzurą RODO a następnie łączy ten plik PDF z naszym CV.

# Jak uruchomić aplikację?

Aplikacja była testowana na systemie operacyjnym Linux. Takie systemy jak Windows oraz macOS nie są oficjalnie wspierane.

- upewnij się, że posiadasz zainstalowane na swoim komputerze następujące oprogramowanie:
  - git (wymagany tylko jeśli instalujesz program ze skryptu i chcesz korzystać z automatycznych aktualizacji)
  - python3
  - virtualenv dla pythona3
  - wget

**Instalacja ze skryptu**

- utwórz folder w którym ma zostać zainstalowana aplikacja
- uruchom konsolę i przejdź do nowo utworzonego folderu
- uruchom polecenie:
  -  `wget https://raw.githubusercontent.com/DocBox12/RODO-CV/version/install.sh && chmod +x install.sh && ./install.sh`
- skrypt pobierze program oraz utworzy wirtualne środowisko Pythona. Po zakończeniu wszystkich czynności aktywuj wirtualne środowisko Pythona i aplikacja jest gotowa do użycia

**Instalacja ręczna**

- utwórz wirtualne środowisko dla Pythona 3 i zainstaluj w nim następujące pakiety:
    - fpdf
    - PyPDF3
    - requests
- wejdź na [tę stronę](https://github.com/DocBox12/RODO-CV/releases) i pobierz najnowszą wersję **stabilną.**
- rozpakuj pobrane archiwum do katalogu z utworzonym wirtualnym środowiskiem
- aktywuj wirtualne środowisko
- przejdź do katalogu **src**
- wykonaj polecenie `chmod +x rodocv.py`

**Pierwsze uruchomienie aplikacji**

- skopiuj swoje CV zmieniając jego nazwę na **cv.pdf** do katalogu **src**
- uruchom konsolę, aktywuj wirtualne środowisko pythona i przejdź do w katalogu **src**
- wykonaj polecenie `./rodocv.py --default` aby dodać do swojego CV domyślną klauzurę RODO. Jeśli chcesz wstawić inną klazurę to wklej ją do pliku `klauzura.txt` i wykonaj polecenie `./rodocv.py`

# Konfiguracja

## config.ini

Przed uruchomieniem aplikacji możesz skonfigurować plik **config.ini** wedle własnych preferencji bądź też skorzystać z ustawień standardowych.

- `document_format = A4` - format dokumentu. Domyślnie jest A4.
- `font_text = arial` - krój czcionki. Listę dostępnych czcionek znajdziesz [na tej stronie](https://github.com/DocBox12/RODO-CV/wiki/Czcionki)
- `font_size = 10` - rozmiar czcionki
- `align_font = L` - rodzaj wyrównania tekstu
- `maring_left = 10` - ustawienie lewego marginesu
- `margin_right = 190` - ustawienie prawego marginesu
- `line_spacing = 5` - ustawienie interlinii
- `new_file_cv_name = newcv2.pdf` - nazwa nowego pliku CV które zostanie wygenerowane.

# Aktualizacja aplikacji (wersja eksperymentalna)

Aplikacja posiada automatyczny system sprawdzający czy pojawiła się nowa wersja aplikacji oraz istnieje możliwość przy jego pomocy wykonać aktualizację oprogramowania bez konieczności ręcznego pobierania plików. W katalogu znajduje się plik `install.py` który posiada następujące opcje:

- `--check_update`  Sprawdza czy jest dostępna nowa wersja programu, jeśli tak to proponuje aktualizacje
- `--force_update`  Przywraca stan aplikacji do oficjalnego wydania i pobiera najnowszą wersję z serwera. Wszystkie twoje ustawienia zostaną usunięte.
-`--reset` Przywraca aplikację do pierwotnego stanu. Wszystkie twoje ustawienia zostaną usunięte.

Aby móc skorzystać z aktualizatora należy
- uruchomić konsolę
- wejść do katalogu w którym mamy zainstalowany program
-  aktywować wirtualne środowisko Pythona
-  wykonać polecenie `./install.py --opcja`

Jest to opcja wysoko eksperymentalna, czyli może działać niestabilnie. Jeśli zauważysz jakieś problemy z funkcją aktualizacji to zgłoś je na [tej stronie](https://github.com/DocBox12/RODO-CV/issues)

# O mnie

Jeśli chcesz dowiedzieć się czegoś więcej o mnie to wejdź na [tę stronę](https://docbox12.github.io/). Możesz mnie również wesprzeć przelewają dobrowolną kwotą kryptowalut. [Tutaj znajdziesz moje portfele.](https://docbox12.github.io/cryptocurrency.html)