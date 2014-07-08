# coding: utf8

from unittest import TestCase

from pywkher import generate_pdf


class PywkherTestCase(TestCase):
    def test_generate_pdf(self):
        pdf_content = generate_pdf(
            html='<html><body>Is this thing on?</body></html>',
        )
        assert pdf_content[:4] == '%PDF'

    def test_unicode(self):
        pdf_content = generate_pdf(
            html=u'<html><body>Schrödinger</body></html>',
        )
        assert pdf_content[:4] == '%PDF'
