# RODO-CV [Polish only]

RODO-CV to aplikacja konsolowa służąca do dodawania klauzury RODO do CV.

# Prolog

Każde ogłoszenie o prace dawniej było opatrzone klauzurą o ochronie danych osobowych, od momentu wejścia w życie RODO ogłoszenia o pracę posiadają specjalną formułkę, którą przed wysłaniem CV do pracodawcy musimy wkleić na końcu naszego dokumentu. Dla wielu ogłoszeń może być użyta uniwersalna reguła RODO, jednak wiele firm w ogłoszeniach prezentuje swoje indywidualne klauzury, które musimy wpisać do naszego dokumentu. Jeśli jej nie wkleimy to osoba rekrutująca z automatu odrzuca naszą aplikację. Postanowiłem zatem stworzyć aplikację, która do gotowego CV zapisanego w pliku PDF będzie dodawać wybraną przez nas regułę RODO.

# Jak to działa?

Podajemy w pliku tekstowym treść klauzury RODO, kopiujemy nasze CV, aplikacja generuje nowy plik PDF z samą klauzurą RODO a następnie łączy ten plik PDF z naszym CV.

# Jak uruchomić aplikację?

Aplikacja była testowana na systemie operacyjnym Linux. Takie systemy jak Windows oraz macOS nie są oficjalnie wspierane.

- upewnij się, że posiadasz zainstalowane na swoim komputerze następujące oprogramowanie:
  - python3
  - virtualenv dla pythona3
  - wget
  - fpdf
  - PyPDF3

- utwórz wirtualne środowisko dla Pythona 3 i zainstaluj wyżej wymienione oprogramowanie. Aplikację wget zainstaluj z repozytorium.
- wejdź na [tę stronę](https://github.com/DocBox12/RODO-CV/releases) i pobierz najnowszą wersją **stabilną.**
- rozpakuj pobrane archiwum do katalogu z utworzonym wirtualnym środowiskiem i aktywuj wirtualne środowisko
- przejdź do katalogu src
- skopiuj swoje CV zmieniając jego nazwę na cv.pdf
- otwórz plik klauzura.txt i wpisz tam klauzurę RODO, która zostanie dodana do twojego CV.
- uzupełnij plik config.ini
- wykonaj polecenie `chmod +x rodocv.py`
- uruchom plik **rodocv.py**
- twoje CV zostanie wygenerowane i zapisane w tym katalogu, w którym jest aplikacja

# Konfiguracja

## config.ini

Przed uruchomieniem aplikacji musisz odpowiednio skonfigurować plik **config.ini**. 

- `document_format = A4` - format dokumentu. Domyślnie jest A4.
- `font_text = arial` - krój czcionki. Listę dostępnych czcionek znajdziesz [na tej stronie](https://github.com/DocBox12/RODO-CV/wiki/Czcionki)
- `font_size = 10` - rozmiar czcionki
- `align_font = L` - rodzaj wyrównania tekstu
- `maring_left = 10` - ustawienie lewego marginesu
- `margin_right = 190` - ustawienie prawego marginesu
- `line_spacing = 5` - ustawienie interlinii
- `new_file_cv_name = newcv2.pdf` - nazwa nowego pliku CV które zostanie wygenerowane.

# O mnie

Jeśli chcesz dowiedzieć się czegoś więcej o mnie to wejdź na [tę stronę](http://aboutme.morfiblog.pl/). Możesz mnie również wesprzeć przelewają dobrowolną sumę kryptowalut. [Tutaj znajdziesz moje portfele.](http://aboutme.morfiblog.pl/cryptocurrency.html)