(setq markdown-xhtml-header-content
      "<style type='text/css'>
*{
    text-align: justify;
}
.centerimage{
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.signimage{
    margin-top: 24px;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    vertical-align: middle;
}
.signimage2{
            font-size: 10px;
            font-style: italic;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
            vertical-align: middle;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
</style>")


# <b>SYMULATOR MRÓWKI LANGTONA</b>
##### Autor: ŁUKASZ STANISZEWSKI
<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209633-c37a6900-7e8d-11eb-9539-5c0467d69758.png" width="80%" align="center"></img>

## <u>SPIS TREŚCI:</u>
- <b>ROZDZIAŁ I. OPIS PROJEKTU</b>
   - WSTĘP
   - ZASADY DZIAŁANIA
   - WYMAGANIA PROJEKTU
- <b>ROZDZIAŁ II. STRUKTURA PROJEKTU</b>
   - OGÓLNY PODZIAŁ
   - SCHEMAT DZIAŁANIA
   - NAJWAŻNIEJSZE UŻYTE BIBLIOTEKI
   - STRUKTURA MODUŁÓW I KLAS
   - NAJISTOTNIEJSZE FUNKCJE
   - ALGORYTMIKA
      - FAZA WSTĘPNA
      - FAZA SYMULACJI
- <b>ROZDZIAŁ III. INSTRUKCJA UŻYTKOWNIKA</b>
   - WSTĘP
   - START KONSOLOWY
   - START GUI
   - OPCJA TWORZENIA PLIKU
   - OPCJA ŁADOWANIA PLIKU
   - OPCJA TWORZENIA PLIKU Z PRAWDOPODOBIEŃSTWEM
   - WYNIK SYMULACJI
- <b>ROZDZIAŁ IV. PRZEPROWADZONE TESTY</b>
   - TESTY JEDNOSTKOWE
   - WAŻNY PRZYKŁAD
   - TEST SYMULACJI
- <b>ROZDZIAŁ V. EWENTUALNY ROZWÓJ</b>
- <b>ROZDZIAŁ VI. WYKORZYSTANE ZASOBY</b>


## <b><u>ROZDZIAŁ I. OPIS PROJEKTU</u></b>

### <i>WSTĘP</i>

Projekt polega na implementacji automatu komórkowego, tzw. Mrówki Langtona.

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209525-5f57a500-7e8d-11eb-9ad7-afc07e8d4346.jpg" width="40%">

<p class="signimage">Rys 1 - trasa mrówki po wykonaniu 7000 kroków</p>

### <i>ZASADY DZIAŁANIA</i>

1. Mrówka porusza się na planszy o określonych wymiarach, podzielonej na kwadratowe
    komórki (pola) w dwóch możliwych kolorach: czarnym i białym
2. Jeśli mrówka znajduje się na polu białym to obraca się w lewo (o kąt prosty), zmienia
    kolor pola na czarny i przechodzi na następną komórkę.
3. Jeśli mrówka znajduje się na polu czarnym to obraca się w prawo (o kąt prosty),
    zmienia kolor pola na biały i przechodzi na następną komórkę.
4. Jeśli mrówka doszła do końca planszy i próbuje za nią wyjść to przechodzi na losowo
    wybraną sąsiednią komórkę, która leży na planszy (np. jeśli mrówka znajduje się w
    dolnym lewym rogu planszy i próbuje przejść jedną komórkę w dół, to powinna wykonać
    losowy ruch w górę, lub w prawo).

### <i>WYMAGANIA PROJEKTU</i>

1. Mrówka porusza się po obrazie, którego wartość początkowa to jedna z następujących możliwości:
    + biały obraz o wymiarach podanych przez użytkownika,
    + obraz ładowany przez użytkownika (powinien być czarno-biały),
    + czarno-biała obraz, gdzie czarne piksele zostały losowo wygenerowane z zadanym prawdopodobieństwem.
2. Wyjściem programu jest zapisana seria obrazów obrazująca wynik 'spaceru' mrówki -
    jeden obraz na każdy ruch. Liczba kroków określona jest przez użytkownika.

## <b><u>ROZDZIAŁ II. STRUKTURA PROJEKTU</u></b>

### <i>OGÓLNY PODZIAŁ</i>

##### Strukturę omawianego projektu najwygodniej podzielić na kilka punktów:

1. DOKUMENTACJA – folder doc
2. TESTY – folder tests i zawarte w nim testy (czyt. rozdział IV)
3. WYJĄTKI – pliki ConsoleExceptions.py i GuiExceptions.py
4. KLASY ODPOWIEDZIALNE ZA SYMULACJE – pliki Ant.py, BoardReader.py i Simulator.py
5. FUNKCJE KONWERTUJACE NA LINII PROJEKT-OBRAZ – pliki ImageInput.py i
    ImageOutput.py
6. CZĘŚĆ INTERFEJSOWĄ – folder gui_files, plik LangtonGui.py
7. FOLDER WYNIKOWY – folder Steps

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209533-6bdbfd80-7e8d-11eb-8fa9-481294b118eb.png" width="70%"></img>

<div class="signimage">Rys 2 - końcowy wygląd folderu z projektem </div>

### <i>SCHEMAT DZIAŁANIA</i>

#### <i>Schemat działania projektu obrazuje lista kroków:</i>

1. Uruchom projekt
2. Wybierz opcje
3. Wprowadź potrzebne dane
4. Program wykonuje symulacje
5. KONIEC


### <i>NAJWAŻNIEJSZE UŻYTE BIBLIOTEKI</i>

Użyte w projekcie biblioteki:


1) <b>Numpy</b> - korzystanie z klas do wygodnej pracy z wektorami dwuwymiarowymi
2) <b>Pillow</b> - biblioteka do obsługi obrazów
3) <b>Pygame</b> – biblioteka do tworzenia interfejsu graficznego
4) Dodatkowo częściej spotykane biblioteki typu <b>time</b>, <b>os</b>, <b>math</b> czy <b>sys</b>

### <i>STRUKTURA MODUŁÓW I KLAS</i>

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209535-6ed6ee00-7e8d-11eb-9822-0b7bdd8600ae.png" width="90%"></img>
<div class="signimage">Rys 3 - struktura klas </div>

### <i>NAJISTOTNIEJSZE FUNKCJE</i>

1. <b>Ant.go(kierunek)</b> – porusza mrowke w dany kierunek
2. <b>BoardReader.create_board_from_picture(obrazek)</b> – tworzy tablice dwuwymiarowa
    z danego obrazka
3. <b>ImageOutput.create_picture_from_board(tablica)</b> – tworzy obrazek z danej tablicy
4. <b>Simulator.take_step()</b> – funkcja odpowiedzialna za pojedynczy krok symulacji


### <i>ALGORYTMIKA</i>

##### FAZA WSTĘPNA

Omówmy teraz dokładniej całe działanie projektu. Użytkownik uruchamiając plik run.py włącza
symulator. W zależności od parametru w pliku run.py może uruchomić grę za pomocą:

+ KONSOLI
+ GRAFICZNEGO INTERFEJSU UŻYTKOWNIKA (GUI)

Teraz ma do wyboru wybranie 1 z 3 opcji:

+ STWORZENIA BIAŁEGO OBRAZKA (podaje wysokość i szerokość oczekiwanej grafiki)
+ ZAŁADOWANIA SWOJEGO OBRAZKA O MAX WIELKOSCI 300x300 (podaje ścieżkę do niego)
+ STWORZENIA BIAŁEGO OBRAZKA Z PRAWDOPODOBIENESTWEM WYSTAPIENIA CZARNYCH
PIXELI NA NIM (zarówno wysokość i szerokość jak i prawdopodobieństwo jest podawane przez użytkownika)

Dodatkowo w każdej z 3 tych opcji musi podać również liczbę kroków jaką ma wykonać mrówka (jeżeli poda więcej niż 30000, mrówka wykona 30000 kroków). Następnie program sprawdza poprawność wprowadzonych danych – odpowiednie typy, wielkości itd. Gdy nie wystąpi żaden wyjątek, przechodzimy do następnej fazy projektu.

##### FAZA SYMULACJI

Fazę tę rozpoczyna program od skonwertowania wygenerowanego obrazka do tablicy
dwuwymiarowej. Przedstawia ona plansze po jakiej się mrówka porusza – to właśnie w jej centrum
zostaje umieszczona mrówka. W pętli wykonującej się N-krotnie (N – liczba kroków podana przez
użytkownika we wcześniejszej fazie) mrówka robi kolejne kroki według algorytmu zawartego w I
rozdziale dokumentacji. W międzyczasie każdy stan planszy jest przerabiany za pomocą odpowiedniej
funkcji na czarno-biały obrazek, który jest zapisywany do folderu Steps z odpowiednia nazwa w
postaci step_[nr kroku]. Po wykonaniu pętli, następuje koniec programu.

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209537-71d1de80-7e8d-11eb-9ab9-3b9084dd6e73.png" width="50%"></img>
<div class="signimage"> Rys 4 – fragment przykładowego wyglądu folderu Steps po zakończonym
programie </div>

## <b><u>ROZDZIAŁ III. INSTRUKCJA UŻYTKOWNIKA</u></b>

### <i>WSTĘP</i>

Aby uruchomić program, należy wejść do folderu z projektem, za pomocą edytora
tekstowego otworzyć plik <b>run.py</b> i w funkcji <b>start()</b> wpisać odpowiednio 1 lub 2:

```python
ImageInput.start(1)   # open in gui
```

```python
ImageInput.start(2)   # open in console
```

### <i>START KONSOLOWY</i>

Następnie po zapisaniu pliku run.py możemy go uruchomić. W konsoli powita nas ekran taki
jak na zdjęciu.

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209571-97f77e80-7e8d-11eb-815b-80e565edfa45.png" width="50%"></img>

<div class="signimage">
Rys 5 - ekran startowy w wersji konsolowej
</div>

### <i>START GUI</i>

Po uruchomieniu pliku run.py z parametrem 1, pojawi nam się następujące okno.

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209575-9a59d880-7e8d-11eb-834a-a0ba99e8e207.png" width="50%"></img> 
<div class="signimage">
Rys 6 - ekran startowy w wersji gui
</div>

### <i>OPCJA TWORZENIA PLIKU</i>

Pierwszą z wybranych opcji, jest opcja tworzenia białego obrazka. Po wybraniu jej, należy
wpisać odpowiednie dane, tak jak na obrazkach. Dane mają też swoje ograniczenia:
1) Wysokość **[height]** obrazka powinna być liczbą całkowitą z zakresu **0-300**
2) Szerokość **[width]** obrazka powinna być liczbą całkowitą z zakresu **0-300**
3) Liczba kroków **[steps]** powinna być liczbą z zakresu **1-30000**


<div class="signimage">
<img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110209577-9cbc3280-7e8d-11eb-8818-e7815c66f115.png" width="40%"></img> 
<img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110209580-9e85f600-7e8d-11eb-8e40-2e2d3ed284c9.png" width="40%">
</div>

<div class="signimage">
Rys. 7.1, 7.2 - ekran 1 opcji w gui oraz w konsoli
</div>

### <i>OPCJA ŁADOWANIA PLIKU</i>

Drugą z możliwych opcji do wybrania jest **ładowanie własnego pliku**. Ładowany plik warto
umieścić w folderze **load**, specjalnie do tego przeznaczonym. Nie ma wymogów co do kolorów na
obrazku – zostanie on przekonwertowany na czarno-biały obiekt. Istotny jest jednak rozmiar obrazka.
Ładowany obrazek nie może mieć szerokości lub wysokości większej niż **300 pixeli**.

<div class="signimage">
</img> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110209584-a0e85000-7e8d-11eb-94f2-fc400b69869c.png" width="45%"></img> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110209589-a2b21380-7e8d-11eb-8d7e-e7018ce7d1f1.png" width="45%"></img>
</div>

<div class="signimage">
Rys. 8.1, 8.2 - ekran 2 opcji w gui oraz w konsoli
</div>

### <i>OPCJA TWORZENIA PLIKU Z PRAWDOPODOBIEŃSTWEM</i>

Trzecią z możliwych opcji do wybrania jest **tworzenie własnego pliku z prawdopodobieństwem
wystąpienia czarnego pixela na nim**. Poza atrybutami pojawiającymi się w opcji 1, występuje tu również
atrybut **probability** – wymaga podania **liczby rzeczywistej z zakresu (0, 1)**.

<div class="signimage">
</img> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110209592-a3e34080-7e8d-11eb-8be3-1502de7f6826.png" width="45%"></img> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110209595-a5ad0400-7e8d-11eb-92ce-29b83dc43d70.png" width="45%"></img></div>
<div class="signimage">
Rys. 9.1, 9.2 - ekran 3 opcji w gui oraz w konsoli
</div>

### <i>WYNIK SYMULACJI</i>

Po zakończeniu symulacji, należy wejść do folderu **steps**. Własnie tam znajduje się wynik całej
symulacji w postaci serii obrazków, tak jak pokazane to zostało na rys 4.

## <b><u>ROZDZIAŁ IV. PRZEPROWADZONE TESTY</u></b>

### <i>TESTY JEDNOSTKOWE</i>

Projekt ten zawiera liczne testy, sprawdzające prawidłowe działanie zawartych w nim klas,
metod, funkcji czy atrybutów. Zaczynając od sprawdzenia pozycji mrówki na planszy aż po całe jej
załadowanie z pliku.

<div class="signimage" style="margin-left:10%;">
</img> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/59453698/110211777-75b72e00-7e98-11eb-8c9f-55c86802ec1a.png" width="25%"></img> 
<img style="vertical-align: middle; margin-left: 20%" src="https://user-images.githubusercontent.com/59453698/110209600-a9d92180-7e8d-11eb-9909-50ed2ffac101.png" width="25%"></img>
</div>

<div class="signimage" style="font-size: 80%">
<span style="margin-right: 5%">Rys. 10 - wszystkie przeprowadzone
testy (działają!)</span>
<span style="margin-left: 5%">Rys 11 - pliki z testami</span>
</div>

### <i>WAŻNY PRZYKŁAD</i>

Istotną właściwością mrówki Langtona jest trasa, jaką wykonuje ona po zrobieniu **10000**
kroków. Tworzy ona wtedy charakterystyczny kształt nazwany **„autostradą”**, nie inaczej jest w tym
projekcie.

<img class="centerimage" src="https://user-images.githubusercontent.com/59453698/110209614-b198c600-7e8d-11eb-89f2-b2cb015d74c8.png" width="40%"></img> 

<div class="signimage">
Rys 12 - droga wykonana
przez mrówkę po 11000
krokach
</div>

### <i>TEST SYMULACJI</i>

Podjąłem w projekcie próbę przeprowadzenia krótkiej symulacji na małym obrazku (np. o
wymiarach 5x3), w której mogłem przewidzieć pierwsze 4 kroki mrówki. Następny krok program ze
względu na mały obszar wybiera już losowo (stąd dalsze testy nie mają sensu – nie da się przewidzieć
następnego kroku).

<div class="signimage">
        <div class="signimage" style="width: 60%; float:left;">
            <img src="https://user-images.githubusercontent.com/59453698/110209617-b3fb2000-7e8d-11eb-9d60-61dc4988e592.png"></img>
            <div class="signimage">
                Rys 13. - test symulacji
            </div>
        </div>
        <div>
            <div class="signimage">
                <img src="https://user-images.githubusercontent.com/59453698/110209620-b5c4e380-7e8d-11eb-8e86-07736865d316.png" width="8%"></img>
                <div class="signimage2">
                    Rys 14.1 - załadowany obrazek jako tablica 0-1
                </div>
            </div>
            <div class="signimage">
                <img src="https://user-images.githubusercontent.com/59453698/110209622-b78ea700-7e8d-11eb-9fda-556ce8b70279.png" width="8%"></img>
                <div class="signimage2">
                    Rys 14.2 - zmiana pozycji środkowego pixela
                </div>
            </div>
            <div class="signimage">
                <img src="https://user-images.githubusercontent.com/59453698/110209625-b9586a80-7e8d-11eb-95f3-66c2ac945072.png" width="8%"></img>
                <div class="signimage2">
                    Rys 14.3 - mrówka skręca w lewo, idzie na pixel w 3 kolumnie i 2 wierszu
                </div>
            </div>
            <div class="signimage">
                <img src="https://user-images.githubusercontent.com/59453698/110209626-bb222e00-7e8d-11eb-82b0-c403bcdfb25b.png" width="8%"></img>
                <div class="signimage2">
                    Rys 14.4 - mrówka skręca w lewo, idzie na pixel w 3 kolumnie i 3 wierszu
                </div>
            </div>
            <div class="signimage">
                <img src="https://user-images.githubusercontent.com/59453698/110209628-bcebf180-7e8d-11eb-8f11-75c89a999327.png" width="8%"></img>
                <div class="signimage2">
                    Rys 14.5 - mrówka skręca w prawo, idzie na pixel w 2 kolumnie i 3 rzędzie
                </div>
            </div>
        </div>
    </div>

Podobne symulacje przeprowadziłem również dla ładowanego obrazka 5x5 (4 kroki) i
stworzonego białego obrazka 5x5 (10 kroków). **Wszystkie symulacje wyszły prawidłowo**.

## <b>ROZDZIAŁ V. EWENTUALNY ROZWÓJ</b>

Projekt można by było udoskonalić w możliwość pojawienia się kilku mrówek naraz na
obrazie. O ile założenie te zostałoby sformułowane już w początkowej fazie projektowania (a tak
naprawdę to w fazie planowania algorytmiki), zaimplementowanie pomysłu mogłoby dojść do
skutku. Na obecnym etapie wdrożone algorytmy stworzone są z przeznaczeniem dla automatu
jednej mrówki i ewentualna modyfikacja spowodowałaby zmianę struktury większości programu.
Dlatego też kwestię tą postanowiłem umieścić w tym rozdziale dokumentacji.

## <b>ROZDZIAŁ VI. WYKORZYSTANE ZASOBY</b>

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
