from flask.ext.wtf import Form
from wtforms import BooleanField, StringField, SelectField, validators
from wtforms.validators import Required
from wtforms.widgets import (CheckboxInput, HiddenInput, Select, SubmitInput, TextInput, Option)

class SegmentPrototypeForm(Form):
    ipa_name = StringField(u'IPA Name', [validators.InputRequired()])
    ipa_symbol = StringField(u'IPA Symbol', [validators.Length(min=1, max=3)])
    ipa_group = SelectField(u'IPA Group', choices=[('', '--'),
        ('pulmonic consonant', 'pulmonic consonant'),
        ('pulmonic affricate', 'pulmonic affricate'),
        ('co-articulated consonant', 'co-articulated consonant'),
        ('non-pulmonic consonant', 'non-pulmonic consonant'),
        ('vowel', 'vowel')])
    ipa_manner = SelectField(u'IPA Manner', choices=[('', '--'),
        ('nasal', 'nasal'),
        ('stop', 'stop'),
        ('sibilant_fricative', 'sibilant_fricative'),
        ('fricative', 'fricative'),
        ('non-sibilant_fricative', 'non-sibilant_fricative'),
        ('approximant', 'approximant'),
        ('flap_or_tap', 'flap_or_tap'),
        ('trill', 'trill'),
        ('lateral_fricative', 'lateral_fricative'),
        ('lateral_approximant', 'lateral_approximant'),
        ('lateral_flap', 'lateral_flap'),
        ('affricate', 'affricate'),
        ('sibilant_affricate', 'sibilant_affricate'),
        ('non-sibilant_affricate', 'non-sibilant_affricate'),
        ('lateral_affricate', 'lateral_affricate'),
        ('click', 'click'),
        ('pulmonic-contour_click', 'pulmonic-contour_click'),
        ('ejective-contour_click', 'ejective-contour_click'),
        ('implosive', 'implosive'),
        ('ejective', 'ejective'),
        ('ejective_fricative', 'ejective_fricative'),
        ('lateral_ejective_fricative', 'lateral_ejective_fricative'),
        ('ejective_affricate','ejective_affricate'),
        ('lateral_ejective_affricate', 'lateral_ejective_affricate'),
        ('unrounded','unrounded'),
        ('rounded', 'rounded'),
 ('central', 'central')])
    ipa_major_place = SelectField(u'IPA Major Place', choices=[('', '--'),
        ('labial', 'labial'),
        ('coronal', 'coronal'),
        ('dorsal', 'dorsal'),
        ('radical', 'radical'),
        ('glottal', 'glottal'),
        ('labial-dorsal', 'labial-dorsal')])
    ipa_minor_place = SelectField(u'IPA Minor Place', choices=[('', '--'),
        ('bilabial', 'bilabial'),
        ('labiodental', 'labiodental'),
        ('dental', 'dental'),
        ('alveolar', 'alveolar'),
        ('postalveolar', 'postalveolar'),
        ('retroflex', 'retroflex'),
        ('alveolo-palatal', 'alveolo-palatal'),
        ('palatal', 'palatal'),
        ('velar', 'velar'),
        ('uvular', 'uvular'),
        ('epiglottal', 'epiglottal'),
        ('glottal', 'glottal'),
        ('pharyngeal', 'pharyngeal'),
        ('labio-velar','labio-velar'),
        ('labio-palatal', 'labio-palatal'),
        ('close-front', 'close-front'),
        ('close-central', 'close-central'),
        ('close-back', 'close-back'),
        ('near-close-near-front', 'near-close-near-front'),
        ('near-close-central', 'near-close-central'),
        ('near-close-near-back', 'near-close-near-back'),
        ('close-mid-front', 'close-mid-front'),
        ('close-mid-central', 'close-mid-central'),
        ('close-mid-back', 'close-mid-back'),
        ('mid-front', 'mid-front'),
        ('mid-central', 'mid-central'),
        ('mid-back', 'mid-back'),
        ('open-mid-front', 'open-mid-front'),
        ('open-mid-central', 'open-mid-central'),
        ('open-mid-back', 'open-mid-back'),
        ('near-open-front', 'near-open-front'),
        ('near-open', 'near-open'),
        ('open-front', 'open-front'),
        ('open-central', 'open-central'),
        ('open-back', 'open-back')])
    ipa_voice = SelectField(u'IPA Voicing', choices=[('', '--'), ('voiced','voiced'), ('voiceless', 'voiceless')])
    syllabic = BooleanField(u'± syllabic', false_values=None)
    consonantal = BooleanField(u'± consonantal', false_values=None)
    approximant = BooleanField(u'± approximant', false_values=None)
    sonorant = BooleanField(u'± sonnorant', false_values=None)
    voice = BooleanField(u'± voice', false_values=None)
    spread_glottis = BooleanField(u'± spread_glottis', false_values=None)
    constricted_glottis = BooleanField(u'± constr_glottis', false_values=None)
    continuant = BooleanField(u'± continuant', false_values=None)
    nasal = BooleanField(u'± nasal', false_values=None)
    strident = BooleanField(u'± strident', false_values=None)
    lateral = BooleanField(u'± lateral', false_values=None)
    labial = BooleanField(u'± labial', false_values=None)
    round = BooleanField(u'± round', false_values=None)
    coronal = BooleanField(u'± coronal', false_values=None)
    anterior = BooleanField(u'± anterior', false_values=None)
    distributed = BooleanField(u'± distributed', false_values=None)
    dorsal = BooleanField(u'± dorsal', false_values=None)
    back = BooleanField(u'± back', false_values=None)
    low = BooleanField(u'± low', false_values=None)
    tense = BooleanField(u'± tense', false_values=None)
    radical = BooleanField(u'± radical', false_values=None)
    laryngeal = BooleanField(u'± laryngeal', false_values=None)
    high = BooleanField(u'± high', false_values=None)