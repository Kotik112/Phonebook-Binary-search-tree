# BST (Binary Search Tree)
# uppgift 1 - Datastruktur & algorithmer

1. Uppgift
Uppgiften är att skriva en telefonbok, dvs ett program där man man sparar
namn och telefonnummer. Datastrukturen skall vara ett binärt sökträd, sorterat
efter namnet.

2. Krav för godkänt

  2.1. Allmänna krav
 
C/C++-kod skall kompilera utan varningar med -Wall.
Koden skall komma med en instruktion för hur man kompilerar/kör den. Det
kan vara en Makefile, ett shell-skript eller bara en textfil med instruktioner.
Dataflödena i programmet skall vara genomtänkta. Onödig minneskopieringskall undvikas.
Minnet skall hanteras korrekt, minne man har fått av malloc/new skall frias med free/delete.
Ni skall skriva era egna implementationer av datastrukturer/algoritmer, inte använda bibliotek.

2.2. Krav på lösningen

- Det skall gå att lägga till personer och söka efter personer. 
- Sökningen skall vara O(log n). 
- Det skall också gå att skriva ut en sorterad lista på alla namn/nummer. 
- Det skall gå att läsa in en fil på det här formatet:


firstName lastName
070XXXXXXX

firstName2 lastName2
073XXXXXX

osv...


3. Krav för väl godkänt

Det skall gå att ta bort personer ur trädet. Man skall kunna skriva ut trädet
på ett snygg sätt (med trädstruktur)
4 Extra uppgifter
Gör ett självbalanserande träd
