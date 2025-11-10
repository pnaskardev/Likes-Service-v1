package presenters

import (
	"time"

	"github.com/google/uuid"
)

// This is what the API will accept when creating/updating a quote
type QuoteCreateRequest struct {
	Quote string `json:"quote" binding:"required"`
}

// This is what the API sends back in responses
type QuoteResponse struct {
	ID        uuid.UUID `json:"id"`
	Quote     string    `json:"quote"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}
