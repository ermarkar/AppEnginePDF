import webapp2
import logging
import traceback
from google.appengine.ext import vendor

# Add any libraries installed in the "pdf" folder.
vendor.add('pdf')

from xhtml2pdf import pisa
from cStringIO import StringIO
      
        
class DownloadPDF(webapp2.RequestHandler):
    def post(self):  
        try:
            content = "<table><tr><th>Name</th></tr><tr><td>Sunil</td></tr></table>"
            output = StringIO()
            pdf = pisa.CreatePDF(content, output, encoding='utf-8')
            pdf_data = pdf.dest.getvalue()

            self.response.headers['Content-Type'] = 'application/pdf'
            self.response.headers['Content-Disposition'] = 'attachment;filename=Any_Name'
            self.response.write(pdf_data)
        except Exception, err:
            logging.info (traceback.format_exc())
        
app = webapp2.WSGIApplication([('/downloadpdf', DownloadPDF)], debug=True)
