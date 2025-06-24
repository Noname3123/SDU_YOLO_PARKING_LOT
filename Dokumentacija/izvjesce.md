# Detekcija slobodnih i zauzetih mjesta na parkingu pomoću YOLO modela

## Motivacija

Cilj je bio doraditi YOLO model koji je napravljen za kolegij "Analitika podataka velikog obujma". Model je izrađen za distribuirani sustav ParkMan.
Jedna od funkcionalnosti ParkMan-a uključuje "brojanje" zauzetih mjesta na parkinzima, temeljem slike sigurnosne kamere na parkirnim mjestima. Kako bi se to implementiralo, korišten je YOLO model koji je treniran nad PKLOT skupom podataka. PKLOT skup podataka nastoji detektirati parkirna mjesta na parkinzima te ih klasificirati u "slobodno" i "zauzeto".

Inicijalni model je treniran sa 20 epoha nad PKLOT skupom podataka. Trenirani model je prikazivao visoke performanse detekcije, koje su vidljive na grafovima ispod.

#TODO: UBACI SLIKE REZULTATA S APVO-a.

Kao što se vidi na grafovima iznad, model je pretreniran te postiže savršene rezultate za parkinge iz PKLOT skupa. Budući da PKLOT sadržava iste parkinge sa različitim korištenostima u trening, validacijskom i test setu, model nije u mogućnosti generalizirati i prepoznati mjesta na novim parkinzima. Razlog proizlazi iz toga što je model učio detektirati parkirna mjesta te ih klasificirati u odgovarajuće kategorije (slobodno i zauzeto). Budući da različiti parkinzi imaju različit raspored mjesta, treniranje generaliziranog modela je zahtjevan proces koji uključuje doradu skupa podataka sa neviđenim parkinzima.

Kako bi se olakšao proces i poboljšala sposobnost generaliziranja, promijenjen je pristup klasifikaciji. Umjesto da se detektiraju parkirna mjesta i klasificiraju u slobodno i zauzeto, model detektira objekte na slici te ih klasificira u vozila (automobili, motorcikli, kamioni, busevi) i ostale objekte. Promjena pristupu klasifikaciji je olakšala sposobnost generalizacije modela uz zadržavanje funkcionalnosti potrebnih za ParkMan sustav - brojanje zauzetih mjesta na parkingu.

## Tim 
Treniranje modela je bilo implementirano u paru te su zadaci bili podijeljeni.

### Damjan Đekić
- Augmentacija i proširenje skupa podataka za treniranje pomoću dodatnih efekata na slici
- Treniranje YOLO11 medium modela sa različitim kombinacijama parametara



### Benjamin Jakupović
- Prilagodba skupa podataka za treniranje (usklađivanje klasa iz VisDrone skupa podataka kako bi se uskladilo za potrebe zadatka) 
- Prilagodba skupa podatka za validaciju i testiranje (usklađivanje klasa iz PKLOT skupa podataka kako bi se uskladilo sa train podacima)
- Treniranje YOLO11 large modela sa različitim kombinacijama parametara

## Pregled područja

#TODO: OPIŠI YOLO I RAČUNALNI VID

## Opis skupa podataka 

#TODO: opiši skup podataka i augmentiranje te baci licence na skup podataka

## Opis primijenjenih metoda

## Opis eksperimenta

## Validacija i objašnjenje rezultata

## Zaključak