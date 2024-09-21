from typing import List
from fastapi import APIRouter, Query, HTTPException, Depends
from sqlmodel import Session
from app.api.deps import SessionDep
from app.models import UserBusiness, UserPublic
from app.crud import get_all_records, get_record_by_id, create_record, update_record, delete_record

router = APIRouter()

@router.get("/user-businesses/", response_model=List[UserBusiness])
def read_user_businesses(
    session: SessionDep,
    skip: int = Query(0, alias="page", ge=0),
    limit: int = Query(10, le=100)
):
    """
    Retrieve a paginated list of user businesses.
    - **skip**: The page number (starting from 0)
    - **limit**: The number of items per page
    """
    return get_all_records(session, UserBusiness, skip=skip, limit=limit)

@router.get("/user-businesses/{user_business_id}", response_model=UserBusiness)
def read_user_business(
    user_business_id: int,
    session: SessionDep
):
    """
    Retrieve a single user business by ID.
    - **user_business_id**: The ID of the user business to retrieve
    """
    return get_record_by_id(session, UserBusiness, user_business_id)

@router.post("/user-businesses/", response_model=UserBusiness)
def create_user_business(
    user_business: UserBusiness,
    session: SessionDep
):
    """
    Create a new user business.
    - **user_business**: The user business data to create
    """
    return create_record(session, UserBusiness, user_business)

@router.put("/user-businesses/{user_business_id}", response_model=UserBusiness)
def update_user_business(
    user_business_id: int,
    user_business: UserBusiness,
    session: SessionDep
):
    """
    Update an existing user business.
    - **user_business_id**: The ID of the user business to update
    - **user_business**: The updated user business data
    """
    return update_record(session, UserBusiness, user_business_id, user_business)

@router.delete("/user-businesses/{user_business_id}", response_model=UserBusiness)
def delete_user_business(
    user_business_id: int,
    session: SessionDep
):
    """
    Delete a user business by ID.
    - **user_business_id**: The ID of the user business to delete
    """
    delete_record(session, UserBusiness, user_business_id)
    return {"message": f"UserBusiness with ID {user_business_id} has been deleted."}

@router.get("/user-publics/", response_model=List[UserPublic])
def read_user_publics(
    session: SessionDep,
    skip: int = Query(0, alias="page", ge=0),
    limit: int = Query(10, le=100)
):
    """
    Retrieve a paginated list of user publics.
    - **skip**: The page number (starting from 0)
    - **limit**: The number of items per page
    """
    return get_all_records(session, UserPublic, skip=skip, limit=limit)

@router.get("/user-publics/{user_public_id}", response_model=UserPublic)
def read_user_public(
    user_public_id: int,
    session: SessionDep
):
    """
    Retrieve a single user public by ID.
    - **user_public_id**: The ID of the user public to retrieve
    """
    return get_record_by_id(session, UserPublic, user_public_id)

@router.post("/user-publics/", response_model=UserPublic)
def create_user_public(
    user_public: UserPublic,
    session: SessionDep
):
    """
    Create a new user public.
    - **user_public**: The user public data to create
    """
    return create_record(session, UserPublic, user_public)

@router.put("/user-publics/{user_public_id}", response_model=UserPublic)
def update_user_public(
    user_public_id: int,
    user_public: UserPublic,
    session: SessionDep
):
    """
    Update an existing user public.
    - **user_public_id**: The ID of the user public to update
    - **user_public**: The updated user public data
    """
    return update_record(session, UserPublic, user_public_id, user_public)

@router.delete("/user-publics/{user_public_id}", response_model=UserPublic)
def delete_user_public(
    user_public_id: int,
    session: SessionDep
):
    """
    Delete a user public by ID.
    - **user_public_id**: The ID of the user public to delete
    """
    delete_record(session, UserPublic, user_public_id)
    return {"message": f"UserPublic with ID {user_public_id} has been deleted."}