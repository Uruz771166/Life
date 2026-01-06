"""
Seed all data into the database.

Run with: python -m app.seed.seed_all
"""
from app.database import SessionLocal, engine
from app.models.base import Base
from app.seed.domains import seed_domains
from app.seed.spiral_dynamics import seed_spiral_dynamics


def seed_all():
    """Seed all data into the database."""
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Check if already seeded
        from app.models.domain import Domain
        from app.models.framework import DevelopmentalFramework

        existing_domains = db.query(Domain).first()
        existing_frameworks = db.query(DevelopmentalFramework).first()

        if existing_domains or existing_frameworks:
            print("Database already seeded. Skipping...")
            print(f"  Domains exist: {existing_domains is not None}")
            print(f"  Frameworks exist: {existing_frameworks is not None}")
            return

        print("Seeding database...")
        print()

        # Seed domains
        print("Seeding MECE domain hierarchy...")
        seed_domains(db)
        print()

        # Seed Spiral Dynamics
        print("Seeding Spiral Dynamics framework...")
        seed_spiral_dynamics(db)
        print()

        print("Database seeding complete!")

    finally:
        db.close()


if __name__ == "__main__":
    seed_all()
