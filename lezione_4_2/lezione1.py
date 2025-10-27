
"""
Per i corsi è auspicabile tenere 4 lezioni esclusivamente
sulla teoria di base della programmazione quindi seguire i 
link (aggiornati al 10.9.24) del file lezione2.
-----------------------
-----------------------
Installazioni:
VSCode
Python
estensioni (in VSCode)
------------------------
------------------------
Variabili di sistema:
Aggiungere alla variabile path (variabili di sistema),
se non è stato fatto durante l'installazione dei pacchetti,
i seguenti valori:
C:\Users\azien\AppData\Local\Programs\Python\Python311
C:\Users\azien\AppData\Local\Programs\Python\Python311\Scripts
------------------------
------------------------
Ambiente Virtuale:
creare una nuova dir (md ...)
nella nuova dir:  (cd ...)

python -m venv env

cd env\Scripts
activate
oppure .\activate

oppure(nel pc della cefi):
cd env\bin
activate
------------------------
------------------------
sempre nella nuova dir, per installare le librerie:

pip install ...

**ATTENZIONE**
Prestiamo anche attenzione agli eventuali conflitti con altri moduli già installati
infatti l'installazione di un nuovo modulo potrebbe non andare a buon fine.
Se il problema è di questa natura conviene realizzare un nuovo
ambiente virtuale dove installare il modulo.
------------------------
------------------------
per disattivare l'ambiente virtuale:

deactivate (da qualsiasi dir)
-------------------------
-------------------------
ricordarsi di attivare l'ambiente virtuale altrimenti 
non si scaricano i pacchetti nel giusto spazio del
nostro progetto.
------------------------
------------------------
Se dovessero apparire problemi di policy: L'esecuzione di script è disabilitata nel sistema in uso...:

https://www.robadainformatici.it/abilitare-esecuzione-script-powershell/

Assicurarsi di aver acceduto come amministratore a VSC.

Sempre con VSC in terminal: Set-ExecutionPolicy Unrestricted
-----------------------
-----------------------
Se dovessero esserci problemi con: "Per impostazione predefinita, Windows PowerShell non carica comandi 
dal percorso corrente. Se si considera il comando attendibile, digitare invece ".\activate"."
Digitare dunque nel terminal:
.\activate
----------------------
----------------------
Come usare python:
sicuramente con VSC altrimenti con la shell di python
(nel prompt dei comandi digitare python)e scrivere
direttamente il codice.
Inoltre c'è Anaconda...,Colab...et.etc.
----------------------



per esercitarsi:
https://codegrind.it/esercizi/python


per teoria ed esercizi:
https://www.w3schools.com/python/python_operators.asp

per teoria:
https://omeguide.altervista.org/python/pagina2.html


"""


'''
L'importanza dell'ambiente virtuale...

Installare le librerie con **pip** direttamente sull'interprete Python globale, senza utilizzare un ambiente virtuale, 
può creare diversi problemi.

Quando installi una libreria in questo modo, questa finisce nella directory globale dell'interprete Python (nel mio caso,
`C:\Users\azien\AppData\Local\Programs\Python\Python311\Lib\site-packages`). Questo significa che:

1. **Condivisione tra progetti**: La libreria installata sarà disponibile per **tutti gli script Python** 
    che usano quell'interprete. Se un altro progetto richiede una versione diversa della stessa libreria, 
    potrebbe causare conflitti.
   
2. **Aggiornamenti non controllati**: Se aggiorni o reinstalli Python, potresti perdere tutte le librerie globali, 
    a meno che non le reinstalli manualmente.

3. **Indipendenza del progetto**: Se il tuo script viene condiviso con altri o spostato su un altro sistema, 
     potrebbe non funzionare correttamente perché dipende da librerie installate globalmente e non specificate
      direttamente all'interno del progetto.

4. **Ambiguità nelle dipendenze**: Quando aggiorni una libreria globale, potresti accidentalmente rompere script 
    esistenti che si aspettano una versione diversa di quella libreria.

### Soluzione consigliata: Usare ambienti virtuali

Un **ambiente virtuale** consente di creare un'installazione di Python isolata per il tuo progetto. 
Le librerie installate in un ambiente virtuale saranno separate da quelle globali e utilizzate solo 
all'interno del progetto.

Ripetiamo dunque i vari passaggi:

1. **Creare un ambiente virtuale**:
   ```bash
   python -m venv nome_ambiente
   ```

   Questo creerà una directory `nome_ambiente` contenente una copia isolata di Python.

2. **Attivare l'ambiente virtuale**:
   - Su **Windows**:
     ```bash
     nome_ambiente\Scripts\activate
     ```
   - Su **macOS/Linux**:
     ```bash
     source nome_ambiente/bin/activate
     ```

   Quando l'ambiente è attivo, noterai un prefisso con il nome dell'ambiente nella shell (ad esempio: `(nome_ambiente)`).

3. **Installare le librerie**:
   Con l'ambiente attivo, usa **pip** per installare le librerie. Queste verranno installate solo nell'ambiente virtuale e non interferiranno con l'interprete globale.

   ```bash
   pip install nome_libreria
   ```

4. **Disattivare l'ambiente virtuale**:
   Quando hai finito di lavorare, puoi disattivare l'ambiente con:
   ```bash
   deactivate
   ```

5. **Condividere il tuo progetto**:
   Includi un file `requirements.txt` con l'elenco delle dipendenze:
   ```bash
   pip freeze > requirements.txt
   ```

   Chi riceve il tuo progetto può ricreare l'ambiente virtuale e installare le dipendenze con:
   ```bash
   pip install -r requirements.txt
   ```

Seguendo questa metodologia, il tuo script sarà indipendente dagli aggiornamenti o cambiamenti nel sistema globale.


'''