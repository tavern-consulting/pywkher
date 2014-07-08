# coding: utf8

from unittest import TestCase

from pywkher import generate_pdf


class PywkherTestCase(TestCase):
    def test_generate_pdf_with_html(self):
        pdf_content = generate_pdf(
            html='<html><body>Is this thing on?</body></html>',
        )
        assert pdf_content[:4] == '%PDF'

    def test_generate_pdf_with_url(self):
        pdf_content = generate_pdf(
            url='http://google.com',
        )
        assert pdf_content[:4] == '%PDF'

    def test_unicode(self):
        pdf_content = generate_pdf(
            html=u'<html><body>Schrödinger</body></html>',
        )
        assert pdf_content[:4] == '%PDF'

    def test_no_arguments(self):
        try:
            generate_pdf()
        except ValueError:
            pass
        else:
            raise AssertionError('Should have raised a ValueError')

    def test_too_many_arguments(self):
        try:
            generate_pdf(
                html='foo',
                url='bar',
            )
        except ValueError:
            pass
        else:
            raise AssertionError('Should have raised a ValueError')
