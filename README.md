# Web-Scraping-Supermarket-Prices
## Pràctica 1 - Tipologia i cicle de vida de les dades 
### Màster U. en Ciència de Dades - UOC

### Integrants del grup.
- Carlos Romero Matarin
- Enric Sintes Arguimbau
### Estructura del repositori

Aquest repositori inclou els components principals següents:
- `dataset/`
  - `productos.csv` - El fitxer CSV que conté les dades dels productes raspats.
- `source/`
  - `Consum.py`: Script de web scraping per a la botiga en línia de Consum.
  - `Dia.py`: Script per extracció de dades de la botiga en línia de DIA.
  - `Supermercadosmas.py`: Script per extracció de dades de Supermercados Más.
  - `main.py`: Fitxer principal que executa les funcions de scraping i desa els resultats.
  - `requirements.txt`: Un fitxer que llista totes les biblioteques necessàries per executar els scripts.
- `README.md`: Documentació del projecte.
- `.gitignore` - Especifica els fitxers intencionadament no seguïts per ignorar.


### Cómo utilizar el código
**Instalación de dependencias:**
Instal·leu les dependències amb la següent comanda:

```bash
pip install -r requirements.txt
```

**Executeu l'script principal:**
Executeu l'script principal amb la següent comanda:

```bash
python main.py
```

L'script `main.py` realitzarà el raspall de totes els supermercats configurats i guardarà les dades raspades a `productos.csv`.

**Paràmetres**
Els scripts no accepten paràmetres a través de la línia de comandes tal com estan estructurats actualment; totes les configuracions es realitzen dins dels fitxers de codi ells mateixos.

**Exemples**
Per raspar dades de tots els supermercats i compilar-les en un fitxer CSV:

## DOI del Conjunt de Dades
El DOI per al conjunt de dades generat a Zenodo és: `10.5281/zenodo.XXXXXXX` [Substituir amb el DOI real]

Assegureu-vos que teniu els permisos adequats per raspar i redistribuir dades dels llocs web dels supermercats.

