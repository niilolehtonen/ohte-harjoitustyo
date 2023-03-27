import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_ja_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_riittava_edullinen(self):
        riittävä_edullinen = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(riittävä_edullinen, 60)

    def test_kateisosto_riittava_maukas(self):
        riittava_maukas = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(riittava_maukas, 100)
    def test_kateisosto_ei_riittava_edullinen(self):
            ei_riittava_edullinen = self.kassapaate.syo_edullisesti_kateisella(200)
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
            self.assertEqual(self.kassapaate.edulliset, 0)
            self.assertEqual(ei_riittava_edullinen, 200)

    def test_kateisosto_ei_riittava_maukas(self):
        ei_riittava_maukas = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(ei_riittava_maukas, 300)

    def test_korttiosto_riittava_edullinen(self):
        kortti = Maksukortti(300)
        korttiosto = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(korttiosto, True)
        self.assertEqual(kortti.saldo, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_riittava_maukas(self):
        kortti = Maksukortti(500)
        korttiosto = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(korttiosto, True)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_riittava_edullinen(self):
        kortti = Maksukortti(100)
        korttiosto = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(korttiosto, False)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_ei_riittava_maukas(self):
        kortti = Maksukortti(100)
        korttiosto = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(korttiosto, False)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahan_lataus_kortille(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_negatiivisen_summan_lataus_kortille(self):
        kortti = Maksukortti(100)
        negatiivinen_lataus = self.kassapaate.lataa_rahaa_kortille(
            kortti, -100)
        self.assertEqual(negatiivinen_lataus, None)