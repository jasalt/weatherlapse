# TIEA207 Demo 2015
Esimerkkiprojekti aineopintojen projektityö-kurssille.
[MIT](LICENSE) lisensoitu.

## Synopsis
Mashup sovellus joka esittää Youtubesta saatavaa päivittäin kuvattua sääkamera-videomateriaalia ja esittää samassa näkymässä sääasemasta ladattua säähavainto-dataa.

![UI Proto](media/sketch.png) 

# Development guide

    mkvirtualenv tiea207-demo -p python3
    pip install -r requirements.txt
    python app/server.py

Browse to http://localhost:5000

# TODO
- Kaiva videolinkit Youtubesta
- Sää-datan lukeminen
- Näkymä eri päivien valintaan
- Päivä-näkymä
- Käppyrät Chartkick kirjastolla
- Deploy

# DONE
...
