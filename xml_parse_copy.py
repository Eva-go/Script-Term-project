def mail():
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    msg = MIMEText('메일 본문')                   # 메일 본문 첨부
    msg['Subject'] = Header('메일 제목', 'utf-8') # 메일 제목 첨부
    msg['From'] = 'sendermail@example.com'       # 송신 메일
    msg['To'] = 'whdudghks123@naver.com'        # 수신 메일
    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp: # (*)
        smtp.login('whdudghks22@gmail.com','dudghks12')           # (**)
        smtp.send_message(msg)