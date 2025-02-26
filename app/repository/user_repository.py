from sqlalchemy.orm import Session
from app.models.user import User
from typing import Optional

class UserRepositoryInterface:
    def get_user_by_uuid(self, db: Session, uuid: str) -> Optional[User]:
        pass

    def create_user(self, db: Session, user: User) -> User:
        pass


class UserRepository(UserRepositoryInterface):
    def get_user_by_uuid(self, db: Session, uuid: str) -> Optional[User]:
        return db.get(User).filter(User.uuid == uuid).first()

    def create_user(self, db: Session, user: User) -> User:
        db_user = User(
            uuid=user.uuid,
            name=user.name,
            job_type=user.job_type,
            job=user.job
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user