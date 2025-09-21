from typing import Type

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models.profile import Profile
from app.models.schemas.profile import ProfileDTO, ProfileUpdate


class ProfileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def profile_create(self, profile: ProfileDTO):
        db_profile = Profile(**profile.dict())
        self.session.add(db_profile)
        await self.session.commit()
        await self.session.refresh(db_profile)
        return db_profile

    async def profile_update(self, profile: ProfileUpdate) -> Type[Profile]:
        update_data = profile.model_dump(exclude_unset=True)
        profile_id = update_data.pop("id")
        db_profile = await self.session.get(Profile, profile_id)

        if not db_profile:
            raise HTTPException(status_code=400, detail="profile not created")

        for field, value in update_data.items():
            setattr(db_profile, field, value)

        await self.session.commit()
        await self.session.refresh(db_profile)
        return db_profile
