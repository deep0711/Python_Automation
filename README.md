# Python_Automation
A small module builded in Python that can automate the work of an Uploading Content manually to Website.Apart from this it also convert the images (if there in uploading files) to required format and Size. Finally after Uploading the content it make a PDF report of uploaded content and send it to the Responsible one by Email.That's it

Content of the Module:
1.mod4emails.py : Responsible for creating a Email with attachment,Confugiring the SMTP Server and sending it.
2.mod4reports.py : Responsible for creating PDF Report from the content provided.
3.mod4reportemail.py : This is the srcipt which calls the above two scripts on requirement.It collects all the information( that has been                        uploaded to the server),store it and sends this Information to mod4reports.py for making a PDF report out of it and                        receiving a PDF report.Finally sending this PDF report to mod4emails.py which attach this PDF report as attachment                        and sends them to destination email.
4.mod4images.py : It converts the images to required format and size that can be uploaded easily!
5.mod4imageupload.py : It uploads the images (only) to the server.Everything else is uploaded through different REST API
6.mod4uploaddesc.py : It uploads the description part of the inventory on the server.

For any qurey:contact me at deepakait5090@gmail.com
