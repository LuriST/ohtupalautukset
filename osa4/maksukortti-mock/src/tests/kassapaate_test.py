import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_myytyjen_lounaiden_maara_kasvaa_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

        self.kassa.osta_lounas(maksukortti_mock)

        self.assertEqual(self.kassa.myytyja_lounaita, 1)

    def test_myytyjen_lounaiden_maara_ei_kasva_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4

        self.kassa.osta_lounas(maksukortti_mock)

        self.assertEqual(self.kassa.myytyja_lounaita, 0)        


    def test_lataa_kutsuu_kortin_lataa_metodia_positiivisella_summalla(self):
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, 10)

        maksukortti_mock.lataa.assert_called_with(10)        


    def test_lataa_ei_kutsu_kortin_lataa_metodia_negatiivisella_summalla(self):
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, -10)

        maksukortti_mock.lataa.assert_not_called()        