package quote

import (
	"likes-service/core/services/entities"
)

type Service interface {
	InsertQuote(quote *entities.Quote) (*entities.Quote, error)
	UpdateQuote(quote *entities.Quote) (*entities.Quote, error)
	RemoveQuote(ID string) error
}

type service struct {
	repository Repository
}

func NewService(r Repository) Service {
	return &service{repository: r}
}

func (s *service) InsertQuote(quote *entities.Quote) (*entities.Quote, error) {
	return s.repository.InsertQuote(quote)
}

func (s *service) UpdateQuote(quote *entities.Quote) (*entities.Quote, error) {
	return s.repository.UpdateQuote(quote)
}

func (s *service) RemoveQuote(ID string) error {
	return s.repository.RemoveQuote(ID)
}
