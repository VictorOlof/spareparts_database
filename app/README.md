Projektuppgift Relationsdatabaser

Ni skall arbeta i grupp och er uppgift är följande:

Skapa en databas som skall användas av en firma som säljer reservdelar till bilar.

Följande krav har framkommit i möte med beställaren:

Kärnan i företagets verksamhet är resvdelar till bilar. En reservdel har

    ett namn
    produktnummer
    en tillverkare
    en leverantör
    en beskrivning
    en lagerplats
    ett lagerantal
    ett inpris
    ett utpris
    ett antal för kritisk nivå som skall göra att en beställning av nya reservdelar görs automatiskt
    ett antal som skall användas vid automatbeställningen
    ett datum när de beställda delarna förväntas hem, om vi har ett sådant.
    För en reservdel skall det även framgå
    vilka bilmärken och modeller som den passar för.

För tillverkare skall det framgå

    företagets namn
    huvudkontorets adress
    huvudkontorets telefonnummer
    kontaktperson om sådan finns
    namn på kontaktperson
    telefonnummer till kontaktperson
    epost till kontaktpersonen
     

För leverantör skall framgå

    namn
    adress
    kontaktperson
    telefon
    epost

Det skall även finnas information om vilka produkter som denna leverantör tillhandahåller.

Systemet skall hålla reda på kunder och ordrar (liknande det som finns i exempeldatabasen från mysqltutorial (http://www.mysqltutorial.org/mysql-sample-database.aspx). En kund kan antignen vara en privatperson eller ett företag. Om det är en företagskund så skall kontaktperson på företaget finnas med kontaktuppgifter.

Även den delen som innehåller personal skall finnas med, eftersom vi vill kunna se vilken personal som kunden köpt av, och i vilken butik som personalen arbetar. Det skall givetvis även framgå i vilken butik som ett visst köp har gjorts samt datum och tid för köpet.

För kunder skall även information om deras bilar lagras, alltså

    registreringsnummer
    tillverkare
    modell
    årsmodell
    färg

En kund kan ha flera bilar.

 
Steg att vidta:

1. Modellera en databasdesign i MySQL

2. Generera databasen automatiskt. Se till att även främmande nycklar och andra constraints blir rätt

3. Testa att ni kan föra in data och komma åt den och att reationerna mellan tabellerna fungerar

4. Radera databasen i MySQL och återskapa en databasmodell i Python med hjälp av SQLAlchemy

5. Gör ett enklare Pythonprogram där man kan se, ändra och uppdatera datat i databasen
