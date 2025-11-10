package main

import (
	"log"

	routes "likes-service/core/routes"

	"github.com/gofiber/fiber/v2"
)

func main() {

	fiberConfig := fiber.Config{
		AppName: "Likes-Service/Core",
	}

	fiberApp := fiber.New(fiberConfig)

	routes.InitialiseNewRoutes(fiberApp)

	log.Fatal(fiberApp.Listen(":8000"))

}
