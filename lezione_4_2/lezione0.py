'''
Per rimuovere le restrizioni che impediscono l'esecuzione degli script in **PowerShell**,
è necessario modificare la **Execution Policy**. Puoi farlo utilizzando il comando 
`Set-ExecutionPolicy`. Ecco cosa fare:

---

### Passaggi:
1. **Aprire PowerShell come amministratore**:
   - Cerca "PowerShell" nel menu Start.
   - Clicca con il tasto destro e seleziona **Esegui come amministratore**.

2. **Impostare la Execution Policy**:
   - Digita il seguente comando per impostare una policy meno restrittiva:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy Unrestricted
     ```
     Questo consente l'esecuzione di tutti gli script, ma fai attenzione perché riduce la sicurezza.

3. **Confermare la modifica**:
   - Ti verrà chiesto se vuoi confermare la modifica. Digita `Y` (Yes) e premi Invio.

4. **Verificare la policy corrente (opzionale)**:
   - Usa questo comando per verificare l'attuale policy:
     ```powershell
     Get-ExecutionPolicy
     ```

---

### Alternative meno permissive:
Se preferisci un'opzione più sicura, puoi usare **RemoteSigned**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
- Questo consente l'esecuzione di script locali senza firma, ma richiede una firma 
digitale per gli script scaricati da internet.

---

### Nota importante:
Se stai eseguendo lo script su una macchina di sviluppo o locale, modificare la policy 
è accettabile. Tuttavia, su server di produzione o ambienti sensibili, **modifica la
policy solo se strettamente necessario**, e considera di ripristinarla successivamente:
```powershell
Set-ExecutionPolicy -ExecutionPolicy Restricted
```



'''