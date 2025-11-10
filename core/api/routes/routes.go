package routes

import (
	"likes-service/core/services/quote"

	"github.com/gofiber/fiber/v2"
	"gorm.io/gorm"
)

func InitialiseNewRoutes(App *fiber.App, db_instance *gorm.DB) {

	App.Get("/health-check", func(ctx *fiber.Ctx) error {
		return ctx.Send([]byte("Hello From the Monolith"))
	})

	quoteRepo := quote.NewRepo(db_instance)
	quoteService := quote.NewService(quoteRepo)

	api := App.Group("/api")
	api.Get("/quote", qu)
}
