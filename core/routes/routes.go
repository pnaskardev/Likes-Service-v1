package routes

import "github.com/gofiber/fiber/v2"

func InitialiseNewRoutes(App *fiber.App) {

	App.Get("/health-check", func(ctx *fiber.Ctx) error {
		return ctx.Send([]byte("Hello From the Monolith"))
	})

	// api := App.Group("/api")

}
