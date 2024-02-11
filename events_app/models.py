"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum


class EventType(enum.Enum):
    PARTY = 1
    STUDY = 2
    NETWORKING = 3
    ALL = 4


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(10))

    events = db.relationship("Event", secondary="guest_event", back_populates="guests")


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description = db.Column(db.String(280))
    date_and_time = db.Column(db.DateTime)

    event_type = db.Column(db.Enum(EventType), default=EventType.ALL)

    guests = db.relationship("Guest", secondary="guest_event", back_populates="events")


guest_event_table = db.Table(
    "guest_event",
    db.Column("guest_id", db.Integer, db.ForeignKey("guest.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
)
