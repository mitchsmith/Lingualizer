from app import db

class SegmentPrototype(db.Model):

    __tablename__ = "segment_prototype"
    id = db.Column(db.Integer, primary_key=True)
    ipa_group = db.Column(db.String, nullable=False)    
    ipa_name = db.Column(db.String, nullable=True)
    ipa_symbol = db.Column(db.String, nullable=True)
    ipa_manner = db.Column(db.String, nullable=True)
    ipa_major_place = db.Column(db.String, nullable=True)
    ipa_minor_place = db.Column(db.String, nullable=True)
    ipa_voice = db.Column(db.String, nullable=True)
    syllabic = db.Column(db.Boolean, nullable=True)
    consonantal = db.Column(db.Boolean, nullable=True)
    approximant = db.Column(db.Boolean, nullable=True)
    sonorant = db.Column(db.Boolean, nullable=True)
    voice = db.Column(db.Boolean, nullable=True)
    spread_glottis = db.Column(db.Boolean, nullable=True)
    constricted_glottis = db.Column(db.Boolean, nullable=True)
    continuant = db.Column(db.Boolean, nullable=True)
    nasal = db.Column(db.Boolean, nullable=True)
    strident = db.Column(db.Boolean, nullable=True)
    lateral = db.Column(db.Boolean, nullable=True)
    labial = db.Column(db.Boolean, nullable=True)
    round = db.Column(db.Boolean, nullable=True)
    coronal = db.Column(db.Boolean, nullable=True)
    anterior = db.Column(db.Boolean, nullable=True)
    distributed = db.Column(db.Boolean, nullable=True)
    dorsal = db.Column(db.Boolean, nullable=True)
    back = db.Column(db.Boolean, nullable=True)
    low = db.Column(db.Boolean, nullable=True)
    tense = db.Column(db.Boolean, nullable=True)
    radical = db.Column(db.Boolean, nullable=True)
    laryngeal = db.Column(db.Boolean, nullable=True)
    high = db.Column(db.Boolean, nullable=True) 

    def __init__(self,
        ipa_group,
        ipa_name,
        ipa_symbol,
        ipa_manner,
        ipa_major_place,
        ipa_minor_place,
        ipa_voice,
        syllabic,
        consonantal,
        approximant,
        sonorant,
        voice,
        spread_glottis,
        constricted_glottis,
        continuant,
        nasal,
        strident,
        lateral,
        labial,
        round,
        coronal,
        anterior,
        distributed,
        dorsal,
        back,
        low,
        tense,
        radical,
        laryngeal,
        high):

        self.ipa_group = ipa_group
        self.ipa_name = ipa_name
        self.ipa_symbol = ipa_symbol
        self.ipa_manner = ipa_manner
        self.ipa_major_place = ipa_major_place
        self.ipa_minor_place = ipa_minor_place
        self.ipa_voice = ipa_voice
        self.syllabic = syllabic
        self.consonantal = consonantal
        self.approximant = approximant
        self.sonorant = sonorant
        self.voice = voice
        self.spread_glottis = spread_glottis
        self.constricted_glottis = constricted_glottis
        self.continuant = continuant
        self.nasal = nasal
        self.strident = strident
        self.lateral = lateral
        self.labial = labial
        self.round = round
        self.coronal = coronal
        self.anterior = anterior
        self.distributed = distributed
        self.dorsal = dorsal
        self.back = back
        self.low = low
        self.tense = tense
        self.radical = radical
        self.laryngeal = laryngeal
        self.high = high

    def __repr__(self):
        return '<ipa_symbol {}> <ipa_name {}>'.format(self.ipa_symbol, self.ipa_name)
