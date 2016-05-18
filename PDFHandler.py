import webapp2
import logging
import traceback
import ast
from datetime import *

from google.appengine.ext import vendor

# Add any libraries installed in the "pdf" folder.
vendor.add('pdf')

from xhtml2pdf import pisa
from cStringIO import StringIO
from ConnectDB import *
import json
       
        
class DownloadLeadReport(webapp2.RequestHandler):
    def post(self):  
        try:
            logging.info("DownloadLeadReport")
            
            parameters = ast.literal_eval(self.request.body)

            reportName  = str(parameters["reportName"])
            
            argsValue = [parameters["customerName"],parameters["serialKey"],parameters["email"],parameters["phoneMobile"],str(parameters["isLead"]),str(parameters["columnNames"]),
            str(parameters["count"]),str(parameters["sortOrder"]),str(parameters["sortBy"]),str(parameters["pageNo"]),str(parameters["token"]),str(parameters["customerId"]),
            str(parameters["sourceId"]), str(parameters["ratingId"]), str(parameters["startDate"]),str(parameters["endDate"]),str(parameters["productId"]),parameters["callOrderId"],
            parameters["macAdress"],parameters["status"],parameters["agentLocation"],parameters["assignedToIds"]]

            queryList = []
            query = makeQuery("dim_get_customers",argsValue)
            queryList.append(query)
            queryList.append("select found_rows() as total_records")
            procedureResult = TalkWithDB().executeMulQueries(queryList)
            records = procedureResult[0]   
            totalRecords = procedureResult[1]
            resultValue = records[0]
            
            if resultValue.has_key("Error"):
                self.response.headers['Content-Type'] = 'application/json'
                self.response.write(json.dumps({"status":[{"code":"1500" , "message":resultValue['Error']}]}))
                return
                
            logging.info("s")
            reportHtml = "<html><head><style type='text/css'>@page {size: A1;margin: 1cm;}</style><body><h4>" + reportName + "</h4> <h5 style='float:right'> Total Records : " + str(totalRecords[0]['total_records']) + "</h5><table border='1' cellpadding='10'><tr bgcolor='gray'>" 
            reportField =[]
            resultValue = records[0]
#            logging.info(str(resultValue))
            
            if resultValue.has_key('customer_id'):
                reportHtml += "<th>Customer Id</th>";
                reportField.append('customer_id')
            
            if resultValue.has_key('first_name'):
                reportHtml += "<th>First Name</th>";
                reportField.append('first_name')
                
            if resultValue.has_key('user_middle_name'):
                reportHtml += "<th>Middle Name</th>";
                reportField.append('user_middle_name')
            
            if resultValue.has_key('last_name'):
                reportHtml += "<th>Last Name</th>";
                reportField.append('last_name')
            
            if resultValue.has_key('company_name'):
                reportHtml += "<th>Company Name</th>";
                reportField.append('company_name')
            
            if resultValue.has_key('birthdate'):
                reportHtml += "<th>Birthdate</th>";
                reportField.append('birthdate')
            
            if resultValue.has_key('email'):
                reportHtml += "<th>Email</th>";
                reportField.append('email')
            
            if resultValue.has_key('alt_email'):
                reportHtml += "<th>Alt Email</th>";
                reportField.append('alt_email')
            
            if resultValue.has_key('phone_mobile'):
                reportHtml += "<th>Phone Mobile</th>";
                reportField.append('phone_mobile')
                
            if resultValue.has_key('primary_address'):
                reportHtml += "<th>Primary Address</th>";
                reportField.append('primary_address')
                
            if resultValue.has_key('city'):
                reportHtml += "<th>City</th>";
                reportField.append('city')
            
            if resultValue.has_key('state'):
                reportHtml += "<th>State</th>";
                reportField.append('state')
            
            if resultValue.has_key('country'):
                reportHtml += "<th>Country</th>";
                reportField.append('country')
            
            if resultValue.has_key('zip'):
                reportHtml += "<th>Zip</th>";
                reportField.append('zip')
            
            if resultValue.has_key('alt_address'):
                reportHtml += "<th>Alt Address</th>";
                reportField.append('alt_address')
                
            if resultValue.has_key('alt_address_city'):
                reportHtml += "<th>Alt Address City</th>";
                reportField.append('alt_address_city')
                
            if resultValue.has_key('alt_address_state'):
                reportHtml += "<th>Alt Address State</th>";
                reportField.append('alt_address_state')
            
            if resultValue.has_key('alt_address_country'):
                reportHtml += "<th>Alt Address Country</th>";
                reportField.append('alt_address_country')
            
            if resultValue.has_key('alt_address_zip'):
                reportHtml += "<th>Alt Address Zip</th>";
                reportField.append('alt_address_zip')    
                
            if resultValue.has_key('source'):
                reportHtml += "<th>Source</th>";
                reportField.append('source')
            
            if resultValue.has_key('rating'):
                reportHtml += "<th>Rating</th>";
                reportField.append('rating')
            
            if resultValue.has_key('description'):
                reportHtml += "<th>Description</th>";
                reportField.append('description')
            
            if resultValue.has_key('created_on'):
                reportHtml += "<th>Created On</th>";
                reportField.append('created_on')
            
            if resultValue.has_key('time_zone'):
                reportHtml += "<th>Time Zone</th>";
                reportField.append('time_zone')
            
            if resultValue.has_key('assigned_to'):
                reportHtml += "<th>Assigned To</th>";
                reportField.append('assigned_to')
        
            if resultValue.has_key('campaign_id'):
                reportHtml += "<th>Campaign Id</th>";
                reportField.append('campaign_id')
        
            if resultValue.has_key('campaign_name'):
                reportHtml += "<th>Campaign Name</th>";
                reportField.append('campaign_name')
        
            if resultValue.has_key('assistent'):
                reportHtml += "<th>Assistent</th>";
                reportField.append('assistent')
        
            if resultValue.has_key('assistent_phone'):
                reportHtml += "<th>Assistent Phone</th>";
                reportField.append('assistent_phone')
            
            if resultValue.has_key('bttr'):
                reportHtml += "<th>BTTR</th>";
                reportField.append('bttr')
            
            if resultValue.has_key('do_not_call'):
                reportHtml += "<th>Do Not Call</th>";
                reportField.append('do_not_call')
                
            if resultValue.has_key('is_lead'):
                reportHtml += "<th>Is Lead</th>";
                reportField.append('is_lead')
                
            if resultValue.has_key('is_deleted'):
                reportHtml += "<th>Is Deleted</th>";
                reportField.append('is_deleted')
            
            if resultValue.has_key('created_by_name'):
                reportHtml += "<th>Created By</th>";
                reportField.append('created_by_name')
            
            if resultValue.has_key('agent_location'):
                reportHtml += "<th>Agent Location</th>";
                reportField.append('agent_location')
            
            if resultValue.has_key('agent_email'):
                reportHtml += "<th>Agent Email</th>";
                reportField.append('agent_email')
                
            reportHtml += "</tr>"
                
            for record in records:
                reportHtml += "<tr>"
                for field in reportField:
                    if record[field] is None:
                        value = "" 
                    else:
                        if isinstance(record[field], (int,long,datetime)):
                            value = str(record[field])
                        else:
                            value = record[field]
                    reportHtml += "<td>" + value + "</td>"
                
                reportHtml += "</tr>"
                
            reportHtml += "</table></body></html>"
            
#            logging.info(reportHtml)
#            content = StringIO(reportHtml)
            output = StringIO()
            pdf = pisa.CreatePDF(reportHtml, output, encoding='utf-8')
            pdf_data = pdf.dest.getvalue()

            self.response.headers['Content-Type'] = 'application/pdf'
            self.response.headers['Content-Disposition'] = 'attachment;filename=LeadReport'
            self.response.write(pdf_data)
        except Exception, err:
            logging.info (traceback.format_exc())
        
app = webapp2.WSGIApplication([('/reports/downloadleadreport', DownloadLeadReport)], debug=True)
