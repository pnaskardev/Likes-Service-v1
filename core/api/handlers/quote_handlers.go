package handlers

import (
	"likes-service/core/api/presenters"
	"likes-service/core/services/entities"
	"likes-service/core/services/quote"

	"github.com/gofiber/fiber/v2"
)

func AddQuote(service quote.Service) fiber.Handler {
	return func(c *fiber.Ctx) error {

		var req entities.Quote
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
				"success": false,
				"message": "Invalid request body",
			})
		}

		result, err := service.InsertQuote(&req)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
				"success": false,
				"message": err.Error(),
			})
		}
		response := presenters.QuoteResponse{
			ID:        result.ID,
			Quote:     result.Quote,
			CreatedAt: result.CreatedAt,
			UpdatedAt: result.UpdatedAt,
		}

		return c.Status(fiber.StatusCreated).JSON(fiber.Map{
			"success": true,
			"data":    response,
		})
	}
}
