# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import requests

# # Twilio credentials (replace with your values)
# account_sid = 'AC91d2411192e18f6a11fbece08400b5e3'  # Your Account SID from Twilio Console
# auth_token = '8f29309aae58b0008dc2626e3b4ac80e'   # Your Auth Token from Twilio Console
# verify_service_sid = 'VAbc3183296d9cc91f6ba430b1c71f02fc'  # Your Verify Service SID

# # Initialize FastAPI application
# app = FastAPI()

# # Data model for incoming request
# class PhoneNumber(BaseModel):
#     phone_number: str  # Field for phone number

# # Route for sending verification code
# @app.post("/send_verification_code")
# async def send_verification_code(data: PhoneNumber):
#     try:
#         # Extract phone number from the request
#         phone_number = data.phone_number

#         # Parameters for the Verify API request
#         url = f"https://verify.twilio.com/v2/Services/{verify_service_sid}/Verifications"
#         auth = (account_sid, auth_token)
#         payload = {
#             'To': phone_number,  # Your confirmed phone number
#             'Channel': 'sms'     
#         }

#         # Sending POST request to Twilio Verify API
#         response = requests.post(url, data=payload, auth=auth)

#         # Check the response from the API
#         if response.status_code == 201:
#             return {"message": f"Verification code sent to {phone_number}"}
#         else:
#             raise HTTPException(status_code=response.status_code, detail=response.text)

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error while sending message: {e}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
