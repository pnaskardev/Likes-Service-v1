package entities

import (
	"time"

	"github.com/google/uuid"
	"gorm.io/gorm"
)

type Base struct {
	ID        uuid.UUID `gorm:"type:uuid;primary_key;"`
	CreatedAt time.Time
	UpdatedAt time.Time
	DeletedAt *time.Time `sql:"index"`
}

func (base *Base) BeforeCreate(transaction *gorm.DB) (err error) {
	uuid, err := uuid.NewV7()
	if err != nil {
		return err
	}
	transaction.Statement.SetColumn("ID", uuid)
	return nil
}
