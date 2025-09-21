import bcrypt


class Password:
    @staticmethod
    async def create_hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    async def is_valid_password(password, hashed_password) -> bool:
        try:
            return bcrypt.checkpw(password.encode(), hashed_password.encode())
        except ValueError:
            return False
