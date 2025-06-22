# Prepare lokalnog envirnomenta:
  1. Skini CUDA Toolkit 12.8 (da python moze pristupit GPU-u ako bude trebalo trainat lokalno)
  2. CMD u dir-u projekta, napisat `python -m venv .venv` pa `.\venv\Scripts\activate`
  3. Onda `pip install -r requirements.txt`
  4. `pip cache purge` da se izbrišu skinuti install fileovi

NOTE: .venv folder će bit nekih 7GB velik nakon installa.

# Download link za dataset
U zip-u je na Onedrive-u. Zip zadrži samo VisDrone/train folder (labeli su već prilagođeni). 

[Link](https://uniri-my.sharepoint.com/:u:/g/personal/benjamin_jakupovic_uniri_hr1/EQBM7BfXOxNNgzyhu1hAooIBJNMTV6NSp90_9Dc4VGRJ2A?e=0zQf7x)

# Download link za cijeli dataset (augmentiran + train + validation)
[Link](https://uniri-my.sharepoint.com/:u:/g/personal/benjamin_jakupovic_uniri_hr1/EWGQQ5-CCXZOs-B2MoFNo68Bh8col_ZwImz1UxQPVOw7LQ?e=WCXard)

# Struktura za editiranje slika
Direktorij u kojem će se kreirati editirane slike za treniranje modela je organiziran ovako:

```
ImageEditor/
    ---- ImageEditor.py

VisDrone/
    ---- train/
            ---- images/
                      ---- image_name.jpg

            ---- labels/
                      ---- image_name.txt

            ---- annotations/
                      ---- image_name.txt
```

# Struktura dataseta
Direktorij s fileoveima nad kojim model uči i testira su organizirane ovako:

```
VisDrone/
    ---- train/
            ---- images/
                      ---- image_name.jpg

            ---- labels/
                      ---- image_name.txt
   ---- test/
              ---- images/
                        ---- image_name.jpg
  
              ---- labels/
                        ---- image_name.txt


   ---- valid/
              ---- images/
                        ---- image_name.jpg
  
              ---- labels/
                        ---- image_name.txt

  ---- data.yml
  ---- annotationConverter.py


```

# Data.yml

U data yml se definiraju direktoriji u kojim će model učiti te klase koje postoje (uz odgovarajuće ID-eve)

```yaml
train: ./train/images # train images (relative to 'path')  6471 images
#TODO: add val and test path to here when they are created
#val: ./valid/images 
#test: ./test/images 

# Classes
names:
  0: non-vehicle
  1: vehicle 


```

# annotationConverter.py

Ima dvije metode - prva converta anotacije iz visdrone formata u yolo format

metoda filterClassAnnotations -> uzima parent direktorij u kojem su direktoriji `images` i `labels` i listu class id-eva koji će se mapirati u class id 1 (vehicle). Metoda prodje kroz sve label.txt ove i primjeni "renaming klasa"

