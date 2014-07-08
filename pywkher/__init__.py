from os import environ, path
from subprocess import call as call_subprocess
from tempfile import NamedTemporaryFile


def generate_pdf(html='', url=''):
    # Validate input
    if not html and not url:
        raise ValueError('Must pass HTML or specify a URL')
    if html and url:
        raise ValueError('Must pass HTML or specify a URL, not both')

    current_directory = path.abspath(path.dirname(__file__))
    wkhtmltopdf_default = path.join(
        current_directory,
        '..',
        'bin',
        'wkhtmltopdf-heroku'
    )

    # Reference command
    wkhtmltopdf_cmd = environ.get('WKHTMLTOPDF_CMD', wkhtmltopdf_default)

    if url:
        with NamedTemporaryFile(suffix='.pdf', mode='rwb+') as pdf_file:
            call_subprocess([wkhtmltopdf_cmd, '-q', url, pdf_file.name])
            pdf_file.seek(0)
            return pdf_file.read()

        # Save the HTML to a temp file
    with NamedTemporaryFile(suffix='.html', mode='w') as html_file:
        html_file.write(html.encode('utf-8'))
        html_file.flush()
        html_file.seek(0)
        with NamedTemporaryFile(suffix='.pdf', mode='rwb+') as pdf_file:
            # wkhtmltopdf
            call_subprocess(
                [wkhtmltopdf_cmd, '-q', html_file.name, pdf_file.name],
            )
            pdf_file.seek(0)
            return pdf_file.read()
