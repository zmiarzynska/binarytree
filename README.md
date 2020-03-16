Rozwiązanie składa się z trzech plików w rozszerzeniu python (*.py) : node.py, calculations.py, testing.py. 

<h1>node.py</h1>
 
W pierwszym z nich (node.py) znajduje się implementacja struktury "Węzeł Drzewa" (Node). Mieści w sobie niezbędne dla tej struktury danych elementy czyli: 
* wartość w danym węźle
* referencja do dwóch innych węzłów (left i right)

        def __init__(self, data):
            if isinstance(data, int):
                self.left = None
                self.right = None
                self.value = data
            else:
                raise ValueError("Value of a node should be an Integer")

Referencja ta odwołuje się do tzw. dzieci, czyli węzłów niżej w hierarchi drzewa. Każdy węzeł może mieć maksymalnie dwie takie referencje (a więc dwoje dzieci) - a więc jest to drzewo binarne.

Ważne jest to, aby nie stosować tych samych węzłów (to znaczy tych samych referencji) kilkukrotnie w tworzeniu drzewa - wówczas stracimy strukturę drzewa,a w zamian za to stworzymy graf,
 dla którego nie zadziałają poprawnie metody z pliku <i>calculations.py</i>.
 

Wartość węzła musi być liczbą całkowitą, w innym przypadku zgłoszony zostanie błąd typu ValueError.


Po zaimplementowaniu kilku obiektów typu Node i po połączeniu ich 
zależnościami typu <i>jeden</i> wskazuje <i> na drugi</i> bez powtórzeń tych samych węzłów otrzymujemy strukturę drzewa.

<h1>calculations.py</h1>

W programie <i>calculations.py </i> znajduję się klasa TreeCalculations, zawierająca obliczenia na drzewach: obliczanie sumy, średniej i mediany
dla dowolnego poddrzewa. 
    
       def get_sum(self, node=None): pass
       def get_mean(self, node=None): pass
       def get_median(self, node=None): pass
       
Aby móc z nich skorzystać, należy wcześniej utworzyć obiekt klasy TreeCalculations. W konstruktorze należy podać obiekt typu Node,
w innym wypadku program zakończy się błędem typu TypeError.
    
    def __init__(self, node):
        if isinstance(node, Node):
            self.root = node
            self.numbers = []
            self.numbers.append(node.value)
        else:
            raise TypeError("To create instance of Treecalculations, Node type required") 
            
Poprzez utworzenie obiektu TreeCalculations przypisujemy podany 
węzeł na wartość "root" tej klasy. Później możemy ją zmienić poprzez funkcję 
change_root(node).

Dzięki temu możemy później używać funkcji do obliczania średniej, sumy i mediany bez podawania parametrów - 
wówczas obliczana jest dana wartość dla poddrzewa roota.

<h5>get_sum(node) </h5>
    
        def get_sum(self, node=None):
            if node is None:
                node = self.root
            if isinstance(node, Node):
                self.numbers.clear()
                amount = 0
                self.add_node_to_list(node)
                for i in range(len(self.numbers)):
                    amount += self.numbers[i]
                return amount
            else:
                raise TypeError("Node type required")

Funkcja obliczająca sumę czyści listę, w której następnie zapisze wszystkie węzły z drzewa. Następnie wywołuje funkcję 
rekurencyjną <i>add_node_to_list(node)</i>, które przechodzi przez wszystkie węzły, dopóki nie zapisze ich w liście.
Następnie korzystając z pętli przechodzi kolejno po elementach i sumuje je,
by na koniec zwrócić wartość sumy wszystkich węzłów.

        def add_node_to_list(self, node):
            if node is not None:
                self.numbers.append(node.value), self.add_node_to_list(node.right), self.add_node_to_list(node.left)
            else:
                pass
                
        
<h6>funkcja rekurencyjna, zapisująca wszystkie wartości całkowite węzła do listy </h6>

<h5>get_mean(node) </h5> 

        def get_mean(self, node=None):
            amount = self.get_sum(node)
            return amount/len(self.numbers)
        
Funkcja (tutaj skrócona wersja) zasadniczo wywołuje poprzednią funkcję, a po zwróceniu przez tamtą wyniku, dzieli go przez długość tablicy.
W ten sposób otrzymujemy średnią wartość wszystkich węzłów.

 <h5>get_median(node) </h5> 
 
    def get_median(self, node=None):
            self.numbers.clear()
            self.add_node_to_list(node)
            self.numbers.sort()
            if len(self.numbers) % 2 == 0:
                temp = self.numbers[len(self.numbers) // 2] + self.numbers[(len(self.numbers) // 2) - 1]
                return temp / 2
            else:
                return self.numbers[(len(self.numbers) - 1) // 2]
 <b>Mediana  </b> to wartość cechy w szeregu uporządkowanym, powyżej i poniżej której znajduje się jednakowa liczba obserwacji.
       
        
Ta funkcja również korzysta z listy, ale tym razem, aby wykonać niezbędne obliczenia, trzeba ją najpierw posortować.
Lista posiada wbudowaną funkcję sort, która jest dobrze zoptymalizowana. Warto więc korzystać z niej, zamiast brać się samemu za implementację sortowania.

Następnie sprawdzamy, czy mamy parzystą ilość węzłów; jeśli tak, to medianę tworzy średnia z dwóch węzłów znajdujących się w środkowej części
zbioru.
Jeśli ilość węzłów jest nieparzysta, to medianę tworzy jeden węzeł, znajdujący się dokładnie po środku zbioru.

<h1>testing.py</h1>
Ostatni plik to plik testowy. Utworzono w nim kilkanaście węzłów i dwa obiekty typu TreeCalculations. Każdy został użyty
do obliczeń wykonanych na drzewie ( a więc utworzyłam dwa drzewa).

Pierwsze z nich to drzewo z przykładu podanego w zadaniu. Drugie to inne, dowolne drzewo. Każde z nich zostało zbudowane
dzięki odwoływaniu się do pól <i>left </i> i <i>right</i>, z tym że w pierwszym przypadku jawną zmienną utworzyłam tylko dla korzenia, w drugim przypadku
każdy węzeł został wcześniej przypisany do zmiennej.
    
    # creating first tree
    root=Node(5)
    root.left=Node(3)
    root.left.left=Node(2)
    ...
    # creating second tree
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.left = node2
    node1.right = node3
    ...

W dalszej części programu znajdują się pliki testowe z modułu unittest.

Najpierw pojawiają się testy obliczające sumę wartości dla wszystkich poddrzew pierwszego i drugiego drzewa.
Następnie, testy obliczające średnią wartość dla wszystkich poddrzew pierwszego i drugiego drzewa.
Na końcu pojawiają się testy dla obliczeń mediany dla wszystkich poddrzew pierwszego i drugiego drzewa.

Do sprawdzenia wartości danego poddrzewa użyłam wbudowanej funkcji sum() oraz importowanych funkcji median() oraz mean().
Do sprawdzenia wyniku w testach najczęściej korzystamy z tej samej listy, która została zbudowana w trakcie wykonywania funkcji.
W niektórych testach jest ona tworzona od nowa. W jeszcze innych podany został wynik wyliczony ręcznie.
Pojawiają się również dwa testy na pojawienie wyjątku. 


