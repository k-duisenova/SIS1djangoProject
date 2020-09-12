# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.test import Client


class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test1(self):
        # home page as a main response
        response = self.client.get('')
        # inputs: amount = 5 and type is Ethereum
        r1 = self.client.get('/calculate?eths=5&eth=ethe')
        # all two pages status code should be equal to 200
        self.assertEqual(response.status_code, r1.status_code)

    def test2(self):
        response = self.client.get('')
        # inputs: amount = 10 and type is Ethereum Classic
        r2 = self.client.get('/calculate?eths=10&eth=ethec')
        self.assertEqual(response.status_code, r2.status_code)
