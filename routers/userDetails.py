from fastapi.routing import APIRouter
from schemas import PostUserDetails, PutUserDetails
from config import connection,cursor
import json



router = APIRouter(prefix='/userDetails', tags=['userDetails'])

@router.get('')
async def getUserDetails():
    query = "SELECT * FROM UserDetails"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    if rows:
        return {"statusCode":1,"response":json.loads(rows)}
    else:
        return {"statusCode":0,"response":"No Data Found"}

    

@router.post('')
async def postUserDetails(request:PostUserDetails):
    try:
        query=(f"""INSERT INTO UserDetails(DealDate,SecurityCode,SecurityName,ClientName,DealType,Quantity,Price)
                        VALUES(?,?,?,?,?,?,?)""",(request.DealDate,request.SecurityCode,request.SecurityName,request.ClientName,request.DealType,request.Quantity,request.Price))
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
        return {"statusCode":1,"response":"Data Added Successfully"}
    
    except Exception as e:
        return {"statusCode":0,"response":str(e)}
    
@router.put('')
async def putUserDetails(request:PutUserDetails):
    try:
        query=f"""UPDATE UserDetails SET DealDate={request.DealDate},SecurityCode={request.SecurityCode},SecurityName={request.SecurityName},ClientName={request.ClientName},DealType={request.DealType},Quantity={request.Quantity},Price={request.Price}
                  WHERE UniqueId={request.UniqueId}"""
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
        return {"statusCode":1,"response":"Data Updated Successfully"}
    except Exception as e:
        return {"statusCode":0,"response":str(e)}
    
    
@router.delete('')
async def deleteUserDetails(UniqueId:int):
    try:
        query=f"""DELETE FROM UserDetails WHERE UniqueId={UniqueId}"""
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
        return {"statusCode":1,"response":"Data Deleted Successfully"}
    except Exception as e:
        return {"statusCode":0,"response":str(e)}

