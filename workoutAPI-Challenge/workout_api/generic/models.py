from uuid import uuid4
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy.orm import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Base(declarative_base()):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
