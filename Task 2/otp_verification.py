import random
import smtplib

# Step 1: Generate a 6-digit random number
otp = random.randint(100000, 999999)

# Step 2: Store the OTP in a variable
otp_variable = str(otp)

# Step 3: Write a program to send emails
def send_email(receiver_email, message):
    sender_email = "zaids3529@gmail.com"
    password = "9826094601zaiD"
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    
    subject = "OTP Verification"
    
    email_text = f"Subject: {subject}\n\n{message}"
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_text)
        print("OTP email sent successfully.")
    except Exception as e:
        print("An error occurred while sending the email.")
        print(str(e))
    finally:
        server.quit()

# Step 4: Send OTP as a message in the email
user_email = input("Enter your email address: ")
message = f"Your OTP is: {otp_variable}"
send_email(user_email, message)

# Step 5: Request user inputs for email and OTP verification
user_input_email = input("Enter the email address where you received the OTP: ")
user_input_otp = input("Enter the OTP you received: ")

if user_input_email == user_email and user_input_otp == otp_variable:
    print("OTP verification successful.")
else:
    print("OTP verification failed.")
