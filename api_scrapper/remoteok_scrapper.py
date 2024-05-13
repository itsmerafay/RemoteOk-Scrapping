# # import requests
# # import xlwt
# # from xlwt import Workbook
# # import smtplib
# # from os.path import basename
# # from email.mime.application import MIMEApplication
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # from email.utils import COMMASPACE, formatdate


# # BASE_URL = 'https://remoteok.com/api/'
# # USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
# # REQUEST_HEADER = {
# #     'User-Agent' : USER_AGENT,
# #     'Accept-Language' : 'en-US, en;q=0.5'
# # }

# # def get_job_postings():
# #     response = requests.get(url=BASE_URL,headers=REQUEST_HEADER)
# #     return response.json()

# # def output_jobs_to_xls(data):

# #     wb =  Workbook()
# #     job_sheet = wb.add_sheet("JOBS")
# #     headers = list(data[0].keys())

# #     for i in range(0, len(headers)):
# #         # 0 is excel first line
# #         # i is first 0 
# #         # headers [0] is slug
# #         job_sheet.write(0, i, headers[i])

# #     for i in range(0, len(data)):
# #         job = data[i]                   # first dictionary for the job
# #         print(job)
# #         values = list(job.values())
# #         for x in range(0, len(values)):
# #             job_sheet.write(i+1, x, values[x])

# #     wb.save("remote_jobs.xls")


# # def send_email(send_from, send_to, subject, text , files=None):

# #     # assert to check for assertion error if x=5 , then assert x==5 "x should be equal to 5"
# #     assert isinstance(send_to, list)  # send_to should carry list of send_to objects.
# #     msg = MIMEMultipart()
# #     msg['From'] = send_from
# #     msg['To'] = COMMASPACE.join(send_to)
# #     msg["Date"] = formatdate(localtime=True)
# #     msg['Subject'] = subject

# #     msg.attach(MIMEText(text))

# #     for f in files or []:
# #         with open(f, "rb") as fil:
# #             part = MIMEApplication(fil.read(), Name=basename(f))
# #         part["Content-Disposition"] = f'attachment; filename="{basename(f)}"'
# #         msg.attach(part)

# #     smtp = smtplib.SMTP('smtp.gmail.com: 587')
# #     smtp.starttls()
# #     smtp.login(send_from, 'agio shth cyos rjtq')
# #     smtp.sendmail(send_from, send_to, msg.as_string())
# #     smtp.close()




# # if __name__=="__main__":
# #     json = get_job_postings()[1:]
# #     output_jobs_to_xls(json)
# #     send_email(
# #         'abdulrafayatiq.03@gmail.com', ["samscoutt.03@gmail.com"],
# #         'Job Posting', 'Please find the attach file with this mail',
# #         files=["remote_jobs.xls"]
# #     )

# import requests
# import xlwt
# from xlwt import Workbook
# import smtplib
# from os.path import basename
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import COMMASPACE, formatdate


# BASE_URL = 'https://remoteok.com/api/'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
# REQUEST_HEADER = {
#     'User-Agent' : USER_AGENT,
#     'Accept-Language' : 'en-US, en;q=0.5'
# }

# def get_job_postings():
#     response = requests.get(url=BASE_URL,headers=REQUEST_HEADER)
#     return response.json()

# def output_jobs_to_xls(data):

#     wb =  Workbook()
#     job_sheet = wb.add_sheet("JOBS")
#     headers = list(data[0].keys())

#     for i in range(0, len(headers)):
#         # 0 is excel first line
#         # i is first 0 
#         # headers [0] is slug
#         job_sheet.write(0, i, headers[i])

#     for i in range(0, len(data)):
#         job = data[i]                   # first dictionary for the job
#         print(job)
#         values = list(job.values())
#         for x in range(0, len(values)):
#             job_sheet.write(i+1, x, values[x])

#     wb.save("remote_jobs.xls")


# def send_email(send_from, send_to, subject, text , files=None):

#     # assert to check for assertion error if x=5 , then assert x==5 "x should be equal to 5"
#     assert isinstance(send_to, list)  # send_to should carry list of send_to objects.
#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = COMMASPACE.join(send_to)
#     msg["Date"] = formatdate(localtime=True)
#     msg['Subject'] = subject

#     msg.attach(MIMEText(text))

#     for f in files or []:
#         with open(f, "rb") as fil:
#             part = MIMEApplication(fil.read(), Name=basename(f))
#         part["Content-Disposition"] = f'attachment; filename="{basename(f)}"'
#         msg.attach(part)

#     smtp = smtplib.SMTP('smtp.gmail.com: 587')
#     smtp.starttls()
#     smtp.login(send_from, 'agio shth cyos rjtq')
#     smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.close()




# if __name__=="__main__":
#     json = get_job_postings()[1:]
#     output_jobs_to_xls(json)
#     send_email(
#         'abdulrafayatiq.03@gmail.com', ["samscoutt.03@gmail.com"],
#         'Job Posting', 'Please find the attach file with this mail',
#         files=["remote_jobs.xls"]
#     )

import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Language' : 'en-US, en;q=0.5'
}

def get_job_postings():
    response = requests.get(url=BASE_URL,headers=REQUEST_HEADER)
    return response.json()

def output_jobs_to_xls(data):

    wb =  Workbook()
    job_sheet = wb.add_sheet("JOBS")
    headers = list(data[0].keys())

    for i in range(0, len(headers)):
        # 0 is excel first line
        # i is first 0 
        # headers [0] is slug
        job_sheet.write(0, i, headers[i])

    for i in range(0, len(data)):
        job = data[i]                   # first dictionary for the job
        print(job)
        values = list(job.values())
        for x in range(0, len(values)):
            job_sheet.write(i+1, x, values[x])

    wb.save("remote_jobs.xls")


def send_email(send_from, send_to, subject, text , files=None):

    # assert to check for assertion error if x=5 , then assert x==5 "x should be equal to 5"
    assert isinstance(send_to, list)  # send_to should carry list of send_to objects.
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg["Date"] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        part["Content-Disposition"] = f'attachment; filename="{basename(f)}"'
        msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(send_from, 'agio shth cyos rjtq')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

if __name__=="__main__":
    json = get_job_postings()[1:]
    output_jobs_to_xls(json)
    send_email(
        'abdulrafayatiq.03@gmail.com', ["samscoutt.03@gmail.com"],
        'Job Posting', 'Please find the attach file with this mail',
        files=["remote_jobs.xls"]
    )
