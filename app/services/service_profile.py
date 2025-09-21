from typing import Type

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.db_models.profile import Profile
from app.models.schemas.profile import ProfileDTO, ProfileUpdate
from app.repo.repo_profile import ProfileRepository


class ProfileService:
    def __init__(self, repo: ProfileRepository):
        self.repo = repo

    async def profile_create(self, profile_info: ProfileDTO) -> Profile:
        try:
            profile = await self.repo.profile_create(profile_info)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="profile already exist")
        except Exception as e:
            raise HTTPException(status_code=405, detail=str(e))
        return profile

    async def profile_update(self, profile_info: ProfileUpdate) -> Type[Profile]:
        return await self.repo.profile_update(profile_info)
