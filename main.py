from fastapi import FastAPI
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from pydantic import BaseModel
from postgrest.exceptions import APIError
import httpx

app = FastAPI()
load_dotenv()


url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

# Response models for Swagger documentation
class sbd_dept(BaseModel):
    sbd_dept: str | None

class error_response(BaseModel):
    error: str

@app.get("/check_sbd/{awsccid}")
def check_sbd(awsccid: str | None = None) -> sbd_dept | error_response:
    if awsccid is None:
        return error_response(error="No AWSCCID provided")
    
    try:
        response = (
            supabase
            .table("aws_members")
            .select("sbd_dept")
            .eq("awsccid", awsccid)
            .execute()
        )
    except APIError as e:
        return error_response(error=f"Database query failed: {str(e)}")
    except httpx.ConnectError:
        return error_response(error="Unable to connect to database")
    except httpx.TimeoutException:
        return error_response(error="Database request timed out")


    if not response.data:
        return error_response(error=f"No member found with AWSCCID: '{awsccid}'")

    # AWS member found. Automatically returns None if sbd_dept is null in database
    return sbd_dept(sbd_dept=response.data[0]["sbd_dept"])