package quote

import (
	"likes-service/core/services/entities"

	"gorm.io/gorm"
)

type Repository interface {
	InsertQuote(quote *entities.Quote) (*entities.Quote, error)
	UpdateQuote(quote *entities.Quote) (*entities.Quote, error)
	RemoveQuote(ID string) error
}

type repository struct {
	Database *gorm.DB
}

func NewRepo(db_instance *gorm.DB) Repository {
	return &repository{Database: db_instance}
}

func (r *repository) InsertQuote(quote *entities.Quote) (*entities.Quote, error) {
	return quote, r.Database.Create(quote).Error
}

func (r *repository) UpdateQuote(quote *entities.Quote) (*entities.Quote, error) {
	return quote, r.Database.Update(quote.ID.String(), quote).Error
}

func (r *repository) RemoveQuote(ID string) error {
	return r.Database.Delete(ID).Error
}
